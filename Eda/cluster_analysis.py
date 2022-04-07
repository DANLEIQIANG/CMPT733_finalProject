import pandas as pd
from nltk.corpus import stopwords
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import nltk
import re
from nltk.tokenize import word_tokenize
import plotly.express as px
import geopandas as gpd
import numpy as np
import warnings

def main(dataset):
    warnings.filterwarnings("ignore")
    df = pd.read_csv(dataset)
    outpath = 'EDA/image/'
    metric = pd.DataFrame()
    count = []
    cluster = []
    terms = []
    for i in pd.unique(df['cluster_labels']):
        temp = df[df['cluster_labels']==i]
        temp['text_clean'] = temp['text_clean'].apply(lambda x:str(x))
        all_text = np.sum(temp['text_clean'])
        count.append(len(temp))
        cluster.append(i)
        terms.append(pd.Series(all_text.split(' ')).value_counts().index[:20])
    metric['count'] = count
    metric['cluster'] = cluster
    metric['terms'] = terms
    output = metric.sort_values('count',ascending=False)
    output.to_csv(outpath +'clusters.csv')
    plt.bar(metric['cluster'], metric['count'], color ='maroon')
    plt.xlabel("Cluster Label")
    plt.ylabel("Number of tweets per cluster")
    plt.savefig(outpath+'cluster_distribution.png')

if __name__ == '__main__':

    dataset = sys.argv[1]
    main(dataset)