# pip install evds pandas
from evds import evdsAPI
import pandas as pd
from datetime import date

api = evdsAPI("BURAYA_KENDİ_EVDS_API_ANAHTARINIZI_YAPIŞTIRIN")
df = api.get_data(
    series=["TP.DK.USD.A.YTL"],
    startdate="01-01-2013",
    enddate=date.today().strftime("%d-%m-%Y"),
    # frequency=1,           # gerekirse: 1=Günlük, 5=Aylık
    # aggregation_types="avg",  # toplulaştırma isterseniz
    # formulas=1               # yüzde değişim vb.
)
df["Tarih"] = pd.to_datetime(df["Tarih"], dayfirst=True, errors="coerce")
df = df.sort_values("Tarih")
df.to_csv("TP.DK.USD.A.YTL_2013_today.csv", index=False, encoding="utf-8-sig")



