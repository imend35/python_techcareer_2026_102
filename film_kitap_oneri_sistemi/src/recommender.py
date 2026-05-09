import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def create_user_item_matrix(ratings_df):

    print("\n" + "=" * 50)
    print("USER-ITEM MATRIX OLUSTURMA ASAMASI")
    print("=" * 50)

    # Bu matrisi oluşturdum çünkü recommendation system algoritmaları
    # kullanıcı davranışlarını matris yapısında daha kolay analiz edebiliyor.
    # Satırlarda kullanıcılar, sütunlarda içerikler yer alacak.
    user_item_matrix = ratings_df.pivot_table(
        index="user_id",
        columns="item_id",
        values="rating"
    )

    # Boş kalan hücreleri 0 ile doldurdum çünkü bu kullanıcıların
    # ilgili içeriğe henüz puan vermediğini gösteriyor.
    # Ayrıca cosine similarity hesaplamasında NaN değerlerle uğraşmamı engelliyor.
    user_item_matrix = user_item_matrix.fillna(0)

    # Oluşturulan matrisin boyutunu kontrol ettim çünkü
    # kullanıcı ve içerik sayısının doğru oluştuğundan emin olmak istiyorum.
    print(f"\nMatrix Boyutu: {user_item_matrix.shape}")

    # İlk birkaç satırı görüntüledim çünkü pivot işleminin
    # beklediğim şekilde çalışıp çalışmadığını doğrulamak istedim.
    print("\nUser Item Matrix:")
    print(user_item_matrix.head())

    return user_item_matrix

def calculate_user_similarity(user_item_matrix):

    print("\n" + "=" * 50)
    print("KULLANICI BENZERLIK HESAPLAMA ASAMASI")
    print("=" * 50)

    # Bu adımda cosine similarity kullandım çünkü kullanıcıların puanlama davranışlarının yön olarak birbirine ne kadar benzediğini ölçmek istiyorum.
    # Yani amaç sadece aynı puanı vermeleri değil, genel tercih eğilimlerinin benzemesi.
    similarity_scores = cosine_similarity(user_item_matrix)

    # Cosine similarity sonucu numpy array olarak döndüğü için bunu DataFrame'e çevirdim.
    # Böylece satır ve sütunlarda user_id değerlerini görerek sonucu daha okunabilir hale getirdim.
    user_similarity_df = pd.DataFrame(
        similarity_scores,
        index=user_item_matrix.index,
        columns=user_item_matrix.index
    )

    # Benzerlik matrisinin boyutunu kontrol ettim çünkü her kullanıcının
    # diğer tüm kullanıcılarla karşılaştırıldığından emin olmak istiyorum.
    print(f"\nBenzerlik Matrisi Boyutu: {user_similarity_df.shape}")

    # İlk birkaç satırı yazdırarak kullanıcılar arası benzerlik skorlarını kontrol ettim.
    print("\nKullanıcı Benzerlik Matrisi:")
    print(user_similarity_df.head())

    return user_similarity_df

def recommend_items_for_user(
    target_user_id,
    user_item_matrix,
    user_similarity_df,
    items_df,
    top_n=5
):

    print("\n" + "="*50)
    print("HEDEF KULLANICI ICIN ONERI URETME ASAMASI")
    print("="*50)


    # Bu kontrolü ekledim çünkü sistemde olmayan bir kullanıcı için öneri üretmeye çalışırsam
    # kod hata verebilir. Önce kullanıcının veri setinde olup olmadığını doğruluyorum.
    if target_user_id not in user_item_matrix.index:
        print(f"{target_user_id} numaralı kullanıcı veri setinde bulunamadı.")
        return pd.DataFrame()


    # Hedef kullanıcının daha önce hangi içeriklere puan verdiğini aldım.
    # Böylece zaten izlediği ya da okuduğu içerikleri tekrar önermeyeceğim.
    target_user_ratings = user_item_matrix.loc[target_user_id]


    # Kullanıcının puan vermediği içerikleri buldum.
    # 0 değerini bu projede "henüz puanlanmamış içerik" olarak yorumluyorum.
    unrated_items = target_user_ratings[
        target_user_ratings == 0
    ].index


    # Hedef kullanıcıya benzeyen diğer kullanıcıları aldım.
    # Kendisiyle olan benzerlik skoru 1 olduğu için onu listeden çıkardım.
    similar_users = user_similarity_df[target_user_id].drop(
        target_user_id
    )


    # Benzer kullanıcıları en yüksek benzerlik skorundan en düşüğe doğru sıraladım.
    # Çünkü öneri üretirken hedef kullanıcıya en çok benzeyen kişilerin etkisi daha yüksek olmalı.
    similar_users = similar_users.sort_values(
        ascending=False
    )


    recommendation_scores = {}


    # Hedef kullanıcının puanlamadığı her içerik için skor hesaplıyorum.
    for item_id in unrated_items:

        weighted_score_sum = 0
        similarity_sum = 0


        # Her benzer kullanıcının bu içeriğe verdiği puanı kontrol ediyorum.
        for similar_user_id, similarity_score in similar_users.items():

            similar_user_rating = user_item_matrix.loc[
                similar_user_id,
                item_id
            ]


            # Sadece benzer kullanıcının gerçekten puan verdiği içerikleri dikkate aldım.
            # Çünkü 0 değeri burada gerçek puan değil, puan verilmediğini gösteriyor.
            if similar_user_rating > 0:

                # Puanı benzerlik skoru ile çarptım çünkü bana daha çok benzeyen kullanıcıların
                # verdiği puanların öneri sonucunda daha etkili olmasını istiyorum.
                weighted_score_sum += similarity_score * similar_user_rating

                # Son skoru normalize edebilmek için toplam benzerlik değerini tuttum.
                similarity_sum += similarity_score


        # Eğer bu içerik için benzer kullanıcılardan veri geldiyse skor hesaplıyorum.
        if similarity_sum > 0:

            recommendation_scores[item_id] = weighted_score_sum / similarity_sum


    # Hesaplanan skorları DataFrame'e çevirdim çünkü sonuçları tablo halinde göstermek daha okunabilir.
    recommendations_df = pd.DataFrame(
        recommendation_scores.items(),
        columns=["item_id", "recommendation_score"]
    )


    # Öneri skoruna göre büyükten küçüğe sıraladım.
    # Böylece kullanıcıya en güçlü öneriler en üstte gösterilecek.
    recommendations_df = recommendations_df.sort_values(
        by="recommendation_score",
        ascending=False
    ).head(top_n)


    # Öneri sonuçlarını item bilgileriyle birleştirdim.
    # Böylece sadece item_id değil; başlık, kategori, tür ve yıl bilgilerini de gösterebileceğim.
    recommendations_df = recommendations_df.merge(
        items_df,
        on="item_id",
        how="left"
    )


    print(f"\n{target_user_id} numaralı kullanıcı için öneriler:")
    print(recommendations_df)


    return recommendations_df
