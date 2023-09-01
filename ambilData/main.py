# import datetime module
import datetime, requests, re, pandas as pd

# consider the start date as 2021-february 1 st
start_date = datetime.date(2022, 3, 1)

# consider the end date as 2021-march 1 st
end_date = datetime.date(2022, 12, 31)

# delta time
delta = datetime.timedelta(days=1)

# iterate over range of dates
list_bulan = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
]

list_hargaIDR = []
list_waktu = []
banyakData = 0

for tahun in range(2014, 2023):
    print(tahun)
    for bulanidx in range(12):
        bulan = list_bulan[bulanidx]
        r = requests.get(f"https://harga-emas.org/history-harga/{tahun}/{bulan}/15")
        dapet = re.findall('<td>([0-9.]+)</td>', r.text)
        r.close()
        hargaIDR = int(dapet[4].replace(".",""))
        list_hargaIDR.append(hargaIDR)
        list_waktu.append(f"{tahun}-{str(bulanidx).zfill(2)}-15")
        start_date += delta


df = pd.DataFrame({
    "Waktu" : list_waktu,
    "Harga" : list_hargaIDR
})

df.to_csv("hasilScrap.csv")
print(df.shape)