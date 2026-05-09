import pandas as pd

def load_data(ratings_path, items_path):
    # Bu projede iki ayrı veri dosyası kullandım çünkü kullanıcı puanları ile içerik bilgilerini ayrı tutmak veri modelini daha anlaşılır hale getiriyor.
    ratings_df = pd.read_csv(ratings_path)

    # Film ve kitaplara ait başlık, kategori, tür ve yıl bilgilerini ayrı bir dosyadan okuyarak daha düzenli bir yapı kurmak istedim.
    items_df = pd.read_csv(items_path)

    return ratings_df, items_df


def check_data(ratings_df, items_df):
    # İlk 5 satırı inceleyerek verinin doğru okunup okunmadığını kontrol ettim.
    print("Ratings İlk 5 Satır:")
    print(ratings_df.head())

    print("\nItems İlk 5 Satır:")
    print(items_df.head())

    # Veri tiplerini kontrol ederek user_id, item_id ve rating gibi alanların analiz için uygun olup olmadığını görmek istedim.
    print("\nRatings Veri Tipleri:")
    print(ratings_df.dtypes)

    print("\nItems Veri Tipleri:")
    print(items_df.dtypes)

    # Eksik değer kontrolü yaptım çünkü öneri sisteminde boş veya hatalı kayıtlar sonuçları yanıltabilir.
    print("\nRatings Eksik Değer Kontrolü:")
    print(ratings_df.isnull().sum())

    print("\nItems Eksik Değer Kontrolü:")
    print(items_df.isnull().sum())

    # Projenin genel büyüklüğünü görmek için toplam kullanıcı, içerik ve puan sayısını hesapladım.
    print("\nToplam Kullanıcı Sayısı:", ratings_df["user_id"].nunique())
    print("Toplam İçerik Sayısı:", items_df["item_id"].nunique())
    print("Toplam Puan Kaydı:", len(ratings_df))
