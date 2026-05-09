# Veri okuma ve ilk kontrol fonksiyonlarını import ediyorum.
from data_loader import load_data, check_data


# Veri temizliği ve doğrulama fonksiyonlarını import ediyorum.
from analysis import validate_data


# Recommendation engine için gerekli fonksiyonları import ediyorum.
from recommender_all import (
    create_user_item_matrix_all,
    calculate_user_similarity_all,
    recommend_for_all_users
)


def main_all():

    print("\n" + "="*50)
    print("FILM / KITAP ONERI SISTEMI BASLATILIYOR")
    print("="*50)


    # Dosya yollarını burada tanımladım çünkü veri kaynaklarını
    # merkezi bir noktadan yönetmek kodun bakımını kolaylaştırıyor.
    ratings_path = "../data/ratings.csv"
    items_path = "../data/items.csv"


    # CSV dosyalarını belleğe alıyorum çünkü tüm analizler
    # dataframe'ler üzerinden ilerleyecek.
    ratings_df, items_df = load_data(
        ratings_path,
        items_path
    )


    # İlk veri incelemesini yapıyorum.
    # Böylece dosyaların doğru okunup okunmadığını görebiliyorum.
    check_data(
        ratings_df,
        items_df
    )


    # Modelleme öncesinde veri kalitesini doğruluyorum.
    validate_data(
        ratings_df,
        items_df
    )


    # Kullanıcı davranışlarını matris formatına dönüştürüyorum.
    # Cosine similarity bu matris üzerinde çalışacak.
    user_item_matrix= create_user_item_matrix_all(
        ratings_df
    )


    # Kullanıcıların birbirine olan benzerliğini hesaplıyorum.
    user_similarity_df = calculate_user_similarity_all(
        user_item_matrix
    )


    # Bu geliştirmeyi yaptım çünkü recommendation system'in
    # sadece tek kullanıcıya değil tüm kullanıcılara hizmet vermesini istiyorum.
    recommendations_df = recommend_for_all_users(
        user_item_matrix,
        user_similarity_df,
        items_df,
        top_n=5
    )


    # Sonuçları terminalde görüntülüyorum.
    print("\n" + "="*50)
    print("FINAL RECOMMENDATION TABLE")
    print("="*50)

    print(recommendations_df)


    # Sonuçları dışarı aktarıyorum çünkü proje tesliminde
    # önerileri csv olarak göstermek profesyonel görünüm sağlar.
    recommendations_df.to_csv(
        "../outputs/recommendations.csv",
        index=False
    )


    print("\nrecommendations_all.csv basariyla olusturuldu.")


if __name__ == "__main__":
    main_all()
