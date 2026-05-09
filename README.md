# 🎬📚 Film / Kitap Öneri Sistemi

Kullanıcıların geçmiş puanlama davranışlarını analiz ederek kişiselleştirilmiş film veya kitap önerileri üreten **Makine Öğrenmesi tabanlı öneri sistemi projesidir.**

Bu projede kullanıcıların geçmişte verdikleri puanlar analiz edilerek benzer kullanıcılar tespit edilmiş, ardından **User-Based Collaborative Filtering (Kullanıcı Tabanlı İşbirlikçi Filtreleme)** ve **Cosine Similarity** algoritması kullanılarak öneriler üretilmiştir.

---

# 🚀 Projenin Amacı

Bu projenin temel amacı;

- Kullanıcıların geçmiş puanlama davranışlarını analiz etmek
- Benzer zevklere sahip kullanıcıları tespit etmek
- Kullanıcının henüz puanlamadığı film veya kitapları önermek
- Önerileri benzerlik skorlarına göre sıralamak

Bu proje aşağıdaki alanlar arasındaki ilişkiyi uygulamalı olarak göstermektedir:

- Veri Analizi
- Matris İşlemleri
- Benzerlik Algoritmaları
- Öneri Sistemleri
- Makine Öğrenmesi Temelleri

---

# 🛠 Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
|-----------|----------------|
| Python | Ana programlama dili |
| pandas | Veri okuma, temizleme ve analiz |
| numpy | Sayısal işlemler |
| scikit-learn | Cosine Similarity hesaplama |
| PyCharm | Geliştirme ortamı |

---

# 📂 Proje Klasör Yapısı

```text
film_kitap_oneri_sistemi/
│
├── data/
│   ├── ratings.csv
│   └── items.csv
│
├── src/
│   ├── main.py
│   ├── main_all.py
│   ├── data_loader.py
│   ├── analysis.py
│   ├── recommender.py
│   └── recommender_all.py
│
├── outputs/
│   └── recommendations.csv
│
└── README.md
```

---

# 📊 Veri Seti

## ratings.csv

Kullanıcıların geçmiş puanlama bilgilerini içerir.

| Sütun | Açıklama |
|-------|----------|
| user_id | Kullanıcı numarası |
| item_id | İçerik numarası |
| rating | Kullanıcının verdiği puan (1-5) |
| timestamp | Puanlama tarihi |

---

## items.csv

Film veya kitaplara ait içerik bilgilerini içerir.

| Sütun | Açıklama |
|-------|----------|
| item_id | İçerik numarası |
| title | İçerik adı |
| category | Kategori |
| type | Film / Kitap |
| year | Yayın yılı |

---

# 🔍 Proje İş Akışı

# 1️⃣ Verinin Yüklenmesi

Bu aşamada;

- CSV dosyaları okunmuştur
- Veri yapısı kontrol edilmiştir
- Eksik veriler analiz edilmiştir

---

# 2️⃣ Veri Temizliği

Bu aşamada aşağıdaki kontroller yapılmıştır:

✅ Eksik veri kontrolü  
✅ Duplicate kayıt kontrolü  
✅ Puan aralığı kontrolü  
✅ Foreign Key kontrolü  

---

# 3️⃣ User-Item Matrix Oluşturma

Kullanıcıların verdikleri puanlar Pivot Table kullanılarak matris yapısına dönüştürülmüştür.

Satırlar:

- Kullanıcılar

Sütunlar:

- Film / Kitaplar

Hücreler:

- Kullanıcı puanları

Örnek:

| Kullanıcı | Interstellar | 1984 | Dune |
|-----------|--------------|------|------|
| 1 | 5 | 4 | 0 |
| 2 | 4 | 0 | 5 |

---

# 4️⃣ Kullanıcı Benzerliği Hesaplama

Kullanıcıların puanlama davranışlarının birbirine ne kadar benzediği **Cosine Similarity** algoritması kullanılarak hesaplanmıştır.

Kullanılan matematiksel yaklaşım:

:contentReference[oaicite:0]{index=0}

Benzerlik skoru:

- **1'e yaklaştıkça → Kullanıcılar çok benzer**
- **0'a yaklaştıkça → Kullanıcılar farklı**

---

# 5️⃣ Öneri Üretimi

Her kullanıcı için aşağıdaki adımlar uygulanmıştır:

- Kullanıcının henüz puanlamadığı içerikler tespit edilmiştir
- Benzer kullanıcılar belirlenmiştir
- Benzer kullanıcıların puanları ağırlıklandırılmıştır
- En yüksek skora sahip içerikler öneri olarak sunulmuştur

Öneri skoru hesaplaması:

:contentReference[oaicite:1]{index=1}

Burada:

- **u → Hedef kullanıcı**
- **v → Benzer kullanıcılar**
- **i → İçerik**

---

# 📈 Örnek Çıktı

| Kullanıcı | İçerik | Kategori | Skor |
|-----------|--------|----------|------|
| 1 | The Martian | Bilim Kurgu | 5.00 |
| 1 | Neuromancer | Siberpunk | 4.82 |
| 2 | The Matrix | Bilim Kurgu | 4.75 |

---

# ▶️ Projenin Çalıştırılması

## Gerekli kütüphanelerin kurulumu

```bash
pip install pandas numpy scikit-learn
```

---

## Projenin çalıştırılması

İstenilen bir hedef kullanıcı için: 

```bash
cd src
python main.py
```

---

Tüm Kullanıcılar için: 

```bash
cd src
python main_all.py
```

---

# 📤 Çıktılar

Üretilen öneriler otomatik olarak aşağıdaki dosyaya kaydedilmektedir:

```text
outputs/recommendations.csv
```

---

# 🎯 Projenin Öne Çıkan Özellikleri

✅ Modüler mimari  
✅ Veri doğrulama pipeline yapısı  
✅ Kullanıcı benzerliği analizi  
✅ Toplu öneri üretimi  
✅ CSV export desteği  
✅ Ölçeklenebilir proje yapısı  

---

# 🚀 Gelecekte Yapılabilecek Geliştirmeler

- Item-Based Recommendation System
- Content-Based Filtering
- Hybrid Recommendation System
- Streamlit ile Web Arayüzü
- Gerçek zamanlı kullanıcı girişi
- Model performans metrikleri


