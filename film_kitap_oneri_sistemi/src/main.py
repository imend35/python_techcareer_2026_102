from data_loader import load_data, check_data
from analysis import validate_data
from recommender import (
    create_user_item_matrix,
    calculate_user_similarity,
    recommend_items_for_user
)
def main():

    # Dosya yollarını burada tanımladım çünkü proje büyüdükçe
    # veri kaynaklarını merkezi olarak yönetmek daha kolay oluyor.
    ratings_path = "../data/ratings.csv"
    items_path = "../data/items.csv"


    # Veri setlerini belleğe alıyorum çünkü sonraki tüm analizler
    # bu dataframe'ler üzerinden ilerleyecek.
    ratings_df, items_df = load_data(
        ratings_path,
        items_path
    )


    # İlk genel veri kontrolünü yapıyorum.
    check_data(
        ratings_df,
        items_df
    )


    # Modelleme öncesi veri kalitesini doğruluyorum.
    validate_data(
        ratings_df,
        items_df
    )

    # Recommendation engine'in temelini oluşturacak
    # user-item matrisini burada oluşturuyorum.
    user_item_matrix = create_user_item_matrix(
        ratings_df
    )

    # Kullanıcılar arasındaki benzerliği hesaplıyorum.
    # Bu çıktı bir sonraki aşamada öneri üretmek için kullanılacak.
    user_similarity_df = calculate_user_similarity(
        user_item_matrix
    )

    target_user_id = 1

    # Bu projede örnek olarak 1 numaralı kullanıcı için öneri üretiyorum.
    # Daha sonra istersem bunu kullanıcıdan input alacak hale getirebilirim.
    recommendations_df = recommend_items_for_user(
        target_user_id,
        user_item_matrix,
        user_similarity_df,
        items_df,
        top_n=5
    )


if __name__ == "__main__":
    main()
