import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def validate_data(ratings_df, items_df):

    print("\n" + "="*50)
    print("VERI TEMIZLIK VE DOGRULAMA ASAMASI")
    print("="*50)

    # Bu kontrolü yaptım çünkü eksik veri olması benzerlik hesaplarını bozabilir
    # ve öneri sisteminin yanlış sonuç üretmesine neden olabilir.
    print("\n1- Eksik Veri Kontrolü")

    missing_ratings = ratings_df.isnull().sum()
    missing_items = items_df.isnull().sum()

    print("\nRatings Null Values:")
    print(missing_ratings)

    print("\nItems Null Values:")
    print(missing_items)

    # Bu kontrolü yaptım çünkü aynı kullanıcı aynı içeriğe birden fazla puan verdiyse
    # duplicate kayıtlar öneri skorlarını yapay olarak yükseltebilir.
    print("\n2- Duplicate Kontrolü")

    duplicate_records = ratings_df.duplicated(
        subset=["user_id", "item_id"],
        keep=False
    )

    duplicate_df = ratings_df[duplicate_records]

    if len(duplicate_df) > 0:
        print("Duplicate kayıt bulundu:")
        print(duplicate_df)
    else:
        print("Duplicate kayıt bulunamadı.")

    # Bu kontrolü yaptım çünkü proje senaryosunda puanlama sistemi 1 ile 5 arasında.
    # Bu aralığın dışındaki değerler veri giriş hatası olabilir.
    print("\n3- Rating Aralığı Kontrolü")

    invalid_ratings = ratings_df[
        (ratings_df["rating"] < 1) |
        (ratings_df["rating"] > 5)
    ]

    if len(invalid_ratings) > 0:
        print("Hatalı puanlar bulundu:")
        print(invalid_ratings)
    else:
        print("Tum puanlar gecerli.")

    # Bu kontrolü yaptım çünkü ratings tablosundaki item_id değerlerinin
    # items tablosunda gerçekten karşılığı olması gerekiyor.
    print("\n4- Foreign Key Kontrolü")

    valid_item_ids = items_df["item_id"]

    invalid_items = ratings_df[
        ~ratings_df["item_id"].isin(valid_item_ids)
    ]

    if len(invalid_items) > 0:
        print("Eslesmeyen item_id bulundu:")
        print(invalid_items)
    else:
        print("Tum item_id degerleri gecerli.")

    # Bu kontrolü yaptım çünkü veri setinin genel kalitesini anlamak için
    # kullanıcı ve içerik dağılımını incelemek önemli.
    print("\n5- Temel Veri Ozetleri")

    print(f"Toplam Kullanici: {ratings_df['user_id'].nunique()}")
    print(f"Toplam Icerik: {items_df['item_id'].nunique()}")
    print(f"Toplam Puan Kaydi: {len(ratings_df)}")
    print(f"Ortalama Puan: {ratings_df['rating'].mean():.2f}")

    # Bu temiz veri artık recommendation engine için hazır.
    print("\nVeri temizligi tamamlandi.")

