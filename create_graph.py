import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv('TP_DK_EUR_A_YTL_2013_today.csv')

# NaN değerleri temizle
df = df.dropna()

# Tarih sütununu index olarak ayarla ve datetime formatına çevir
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True)

# Grafiği oluştur
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['TP_DK_EUR_A_YTL'], linewidth=2)
plt.title('Euro/TL Kur Değişimi (2013-Günümüz)')
plt.xlabel('Tarih')
plt.ylabel('EUR/TL')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Grafiği kaydet
plt.savefig('euro_tl_grafik.png')
plt.close()