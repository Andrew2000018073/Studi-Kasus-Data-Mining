#Sebelumnya data dimasukan kedalam mysql dan data pada waktu_menit kami drop.  
#Sebelumnya data kami terdiri atas 2 file csv, dan kami lakukan proses join dengan menggunakan mysql


#Import Library
import pandas as pd # Library yang sangat dibutuhkan didalam prepocessing. Berguna untuk pembersihan, pengolahan, load data, dan masih banyak lagi
import numpy as np #Mengolah dan memmproses data dengan kolom atau fitur dengan jumlah yang banyak
import seaborn as sns # Visualisasi data
import matplotlib.pyplot as plt #Visualisasi data
%matplotlib inline

#Melakukan load data
df = pd.read_csv(r'tempat_wisata_beserta_rating_wisatawan_untuk_kota_yogyakarta.csv')
# df = df.sort_values(by=['id_tempat'])
df.head() #Menampilkan data teratas

df.columns #Cek nama kolom

df.isnull().sum() #Mengecek banyaknya noise data

data = df[['tarif', 'rating_tempat']] # Menyimpan nilai pada kolom tarif dan rating tempat pada variabel data

# normalisasi min-max kolom tarif, rating_tempat, langitude, dan longitude
from sklearn.preprocessing import MinMaxScaler 
data_skaling = data[['tarif', 'rating_tempat']].copy() #Menyalin data pada kolom tariff dan rating tempat ke data_skaling
scaler = MinMaxScaler()
data_skaling = scaler.fit_transform(data_skaling.to_numpy())
data_training = data.copy()
data_training[['tarif', 'rating_tempat']] = data_skaling
data_training
