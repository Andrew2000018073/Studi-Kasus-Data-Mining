# metode elbow untuk menemukan jumlah cluster yang optimal untuk digunakan 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init='k-means++', random_state=42)
    clustering.fit(data_training)
    wcss.append(clustering.inertia_)

ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sns.lineplot(x = ks, y = wcss);


#Melihat jumlah cluster yang baik dengan menggunakan silhoutte
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

kmeans = KMeans(n_clusters = 6)
kmeans.fit(data_training)
df['kluster'] = kmeans.labels_
print(kmeans.labels_)
print(silhouette_score(data_training, kmeans.labels_))


#Menampilkan clustering dalam model grafik
sns.scatterplot(x="rating_tempat", y="tarif",hue = 'kluster', 
palette=['red','yellow','green','blue','purple', 'orange'], data=df)


#Menginialisasi kembali variabel kluster dengan jenis kluster masing-masing dan sesuai dengan kolom tarif dan ratin tempat kluster
kluster0 = df.loc[(df['kluster'] == 0), ['tarif', 'rating_tempat']]
kluster1 = df.loc[(df['kluster'] == 1), ['tarif', 'rating_tempat']]
kluster2 = df.loc[(df['kluster'] == 2), ['tarif', 'rating_tempat']]
kluster3 = df.loc[(df['kluster'] == 3), ['tarif', 'rating_tempat']]
kluster4 = df.loc[(df['kluster'] == 4), ['tarif', 'rating_tempat']]

#Melihat rata-rata dari rating dan tarif pada setiap cluster. Serta tarif dan rating tempat dengan nilai terkecil dan terbesar pada setiap kelompok cluster
tarif_min = kluster0['tarif'].min()
tarif_max = kluster0['tarif'].max()
rating_min = kluster0['rating_tempat'].min()
rating_max = kluster0['rating_tempat'].max()
print('total kelompok kluster 0 pada dataset : ', len(kluster0))
print('rentang tarif  : ', 'Rp. ', tarif_min, ' - ', 'Rp. ', tarif_max)
print('rentang rating : ', rating_min, ' - ', rating_max)
print('_______________________________________________________________')
print('informasi rata - rata : ')
kluster0.mean()
