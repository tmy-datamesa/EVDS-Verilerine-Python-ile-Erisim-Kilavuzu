# 📊 EVDS Verilerine Python ile Erişim Kılavuzu (Tutorial)

Merhaba! Bu repo, **Türkiye Cumhuriyet Merkez Bankası’nın Elektronik Veri Dağıtım Sistemi (EVDS)** üzerinden Python ile ekonomik veri çekmeyi öğrenmek isteyenler için hazırlanmıştır.  
Adım adım anlatımı YouTube’da izleyebilirsin 👇  
🎥 [EVDS Verilerine Python ile Erişim (Data Masası)](https://youtu.be/BG51rSq9TUE)

---

## 🎯 Bu Kılavuzda Ne Öğreneceksin?

1. EVDS API anahtarını nasıl alacağını,  
2. Python ile EVDS’ye nasıl bağlanacağını,  
3. İstediğin serileri (örneğin döviz kuru) nasıl çekeceğini,  
4. Veriyi nasıl düzenleyip CSV’ye kaydedeceğini,  
5. Sonuçları nasıl grafikleştireceğini öğreneceksin.  

---

## 🧩 1️⃣ API Anahtarı Almak

1. [EVDS Resmî Sitesine Git →](https://evds2.tcmb.gov.tr/)
2. Üye ol veya hesabınla giriş yap.
3. Profil sayfandan bir **API Anahtarı (API Key)** oluştur.
4. Bu anahtarı kodda kullanacağız.  

> 🔒 **Uyarı:** Anahtarını kimseyle paylaşma. Kodu paylaşırken `YOUR_API_KEY` şeklinde bırakabilirsin.

---

## 💻 2️⃣ Gerekli Kütüphaneleri Kur

Aşağıdaki komutu terminal veya VS Code/Colab hücresine yaz:

```bash
pip install evds pandas matplotlib

---

##🐍 4️⃣ Python Betiğini Yaz

evds_kur_ornek.py dosyasına şu kodu yapıştır:

python
Kodu kopyala
from evds import evdsAPI
import pandas as pd
from datetime import date

# 1️⃣ TCMB EVDS API bağlantısı
api = evdsAPI("YOUR_API_KEY")

# 2️⃣ Veri serisini tanımla (örnek: EUR/TL kuru)
df = api.get_data(
    series=["TP.DK.EUR.A.YTL"],
    startdate="01-01-2013",
    enddate=date.today().strftime("%d-%m-%Y"),
)

# 3️⃣ Tarih sütununu düzenle
df["Tarih"] = pd.to_datetime(df["Tarih"], dayfirst=True, errors="coerce")
df = df.sort_values("Tarih")

# 4️⃣ CSV olarak kaydet
df.to_csv("TP_DK_EUR_A_YTL_2013_today.csv", index=False, encoding="utf-8-sig")


📈 5️⃣ Grafiği Oluştur
Veriyi görselleştirmek için:

python
Kodu kopyala
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df["Tarih"], df["TP.DK.EUR.A.YTL"])
plt.title("EUR / TL Döviz Kuru (2013–Günümüz)")
plt.xlabel("Tarih")
plt.ylabel("Kur")
plt.grid(True)
plt.show()

---

##📚 8️⃣ Kaynaklar

📘 TCMB EVDS Resmî Sitesi
📦 evds Python Paketi (PyPI)
🎥 Data Masası YouTube Kanalı
