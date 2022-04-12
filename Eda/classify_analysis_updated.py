import pandas as pd
import matplotlib.pyplot as plt
import sys
import plotly.express as px
import geopandas as gpd
import numpy as np
import glob

import os

def helper(x):
    states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    names = {
    'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado',
'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}
    names = {v.upper(): k for k, v in names.items()}
    for i in states:
        if i in x.upper():
            return i
    for i in names.keys():
        if i in x.upper():
            return names[i]
    else:
        return ''

def helperr(x):
    if x==2:
        return 1
    elif x==1:
        return 2
    else:
        return x

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
    outpath = 'EDA/image_updated/' + dataset.split('/')[-2] + '/'
    #load the dataset
    print(outpath)
    df = contactCsv(dataset)
    df['classification_labels'] = df['classification_labels'].apply(helperr)
    if len(np.unique(df['geo_country_code'])) <2:
        print('Only one country originality was detected.')
        df['state'] = df['user_location'].apply(helper)
        temp = df[df['state']!=''].groupby('state').mean()[['classification_labels']]
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='classification_labels',
                    color_continuous_scale="Viridis_r",
                    )
        fig.write_image(outpath + 'mean_label_score_usa.png')

        temp = df[(df['state']!='')&(df['classification_labels']==2)].groupby('state').count()[['sentiment_cluster']]
        temp['all'] = df[(df['state']!='')].groupby('state').count()['sentiment_cluster']
        temp['positive_percent'] = temp['sentiment_cluster']/temp['all']*100
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='positive_percent',
                    color_continuous_scale="Viridis_r",
                    )
        fig.write_image(outpath + 'positive_percent_usa.png')

        temp = df[(df['state']!='')&(df['classification_labels']==0)].groupby('state').count()[['sentiment_cluster']]
        temp['all'] = df[(df['state']!='')].groupby('state').count()['sentiment_cluster']
        temp['negative_percent'] = temp['sentiment_cluster']/temp['all']*100
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='negative_percent',
                    color_continuous_scale="Viridis_r",
                    range_color=(10, 30),
                    )
        fig.write_image(outpath + 'negative_percent_usa.png')

    else:
        temp = df[df.geo_country_code.isin(['NZ','AU','CA','GB','US'])].groupby('geo_country_code').mean()[['classification_labels']]
        temp['country_code'] = temp.index
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        world['country_code'] = world['iso_a3'].apply(lambda x:x[:-1])
        temp = world.merge(temp,on='country_code')
        tempp = temp[(temp['iso_a3']!='CAF')&(temp['iso_a3']!='AUT')]
        tempp.plot(figsize=(15, 10),column='classification_labels',legend=True,legend_kwds={'label': "mean_label_score",
                        'orientation': "horizontal"})
        plt.savefig(outpath + 'mean_label_score_world.jpg')

        temp = df[(df.geo_country_code.isin(['NZ','AU','CA','GB','US']))&(df['classification_labels']==0)].groupby('geo_country_code').count()[['classification_labels']]
        temp['all'] = df[df.geo_country_code.isin(['NZ','AU','CA','GB','US'])].groupby('geo_country_code').count()['classification_labels']
        temp['negative_percent'] = temp['classification_labels']/temp['all']*100
        temp['country_code'] = temp.index
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        world['country_code'] = world['iso_a3'].apply(lambda x:x[:-1])
        temp = world.merge(temp,on='country_code')
        tempp = temp[(temp['iso_a3']!='CAF')&(temp['iso_a3']!='AUT')]
        tempp.plot(figsize=(15, 10),column='negative_percent',legend=True,legend_kwds={'label': "negative_percent",
                        'orientation': "horizontal"}, vmin=17, vmax=22, cmap='YlGnBu', edgecolor='white')
        plt.savefig(outpath + 'negative_percent_world.jpg')

        temp = df[(df.geo_country_code.isin(['NZ','AU','CA','GB','US']))&(df['classification_labels']==2)].groupby('geo_country_code').count()[['classification_labels']]
        temp['all'] = df[df.geo_country_code.isin(['NZ','AU','CA','GB','US'])].groupby('geo_country_code').count()['classification_labels']
        temp['positive_percent'] = temp['classification_labels']/temp['all']*100
        temp['country_code'] = temp.index
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        world['country_code'] = world['iso_a3'].apply(lambda x:x[:-1])
        temp = world.merge(temp,on='country_code')
        tempp = temp[(temp['iso_a3']!='CAF')&(temp['iso_a3']!='AUT')]
        tempp.plot(figsize=(15, 10),column='positive_percent',legend=True,legend_kwds={'label': "positive_percent",
                        'orientation': "horizontal"})
        plt.savefig(outpath + 'positive_percent_world.jpg')


        df=df[df['geo_country_code']=='US']
        df['state'] = df['user_location'].apply(helper)
        temp = df[df['state']!=''].groupby('state').mean()[['classification_labels']]
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='classification_labels',
                    color_continuous_scale="Viridis_r",
                    )
        fig.write_image(outpath + 'mean_label_score_usa.png')

        temp = df[(df['state']!='')&(df['classification_labels']==2)].groupby('state').count()[['cluster_labels']]
        temp['all'] = df[(df['state']!='')].groupby('state').count()['cluster_labels']
        temp['positive_percent'] = temp['cluster_labels']/temp['all']*100
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='positive_percent',
                    color_continuous_scale="Viridis_r",
                    )
        fig.write_image(outpath + 'positive_percent_usa.png')

        temp = df[(df['state']!='')&(df['classification_labels']==0)].groupby('state').count()[['cluster_labels']]
        temp['all'] = df[(df['state']!='')].groupby('state').count()['cluster_labels']
        temp['negative_percent'] = temp['cluster_labels']/temp['all']*100
        temp['state'] = temp.index
        fig = px.choropleth(temp,
                    locations='state', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='negative_percent',
                    color_continuous_scale="YlGnBu",
                    range_color=(10, 40),
                    )
        fig.write_image(outpath + 'negative_percent_usa.png')
        

if __name__ == '__main__':

    dataset = sys.argv[1]
    main(dataset)