# model 
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def K_model(df):
    kmeans_model = KMeans(n_clusters=3)
    kmeans_model.fit(df)
    labels = kmeans_model.predict(df)
    d = pd.DataFrame(df)
    d['cluster'] = labels
    values = d.cluster.value_counts()
    values.to_csv('k.txt', sep='\t', index=True)