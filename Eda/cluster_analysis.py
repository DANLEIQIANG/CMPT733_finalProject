import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
import warnings
import glob
import os

def contactCsv(path):
    read_csv = glob.glob(os.path.join(path, '*.csv'))
    df = None
    for file in read_csv:
        temp = pd.read_csv(file)
        if df is None:
            df = temp
        else:
            df = pd.concat([df, temp], ignore_index=True)
    print(df.info())
    return df

def main(dataset):
    warnings.filterwarnings("ignore")
    #load the dataset
    outpath = 'EDA/image_updated/' + dataset.split('/')[-2] + '/'
    print(outpath)
    df = contactCsv(dataset)
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
    plt.bar(metric['cluster'], metric['count'], color ='cornflowerblue')
    plt.xlabel("Cluster Label")
    plt.ylabel("Number of tweets per cluster")
    plt.savefig(outpath+'cluster_distribution.png')

if __name__ == '__main__':

    dataset = sys.argv[1]
    main(dataset)