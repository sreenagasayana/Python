#importing panda library
import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
#Loading CSV data
variables = pandas.read_csv('/Users/jayantis/Desktop/stocks.csv')
Y = variables[['returns']]
X = variables[['dividendyield']]
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
#Graph for the Nc and score calculated through CSV X and Y values.
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()
pca = PCA(n_components=1).fit(Y)
#Using PCA for transforming the X and Y points
pca_d = pca.transform(Y)
pca_c = pca.transform(X)
#taking k as 3. As the first plot indicates the same
kmeans=KMeans(n_clusters=3)
kmeansoutput=kmeans.fit(Y)
#First graph plot displaying the data in the stock_data csv
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()