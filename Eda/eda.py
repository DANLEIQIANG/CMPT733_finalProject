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

def main(dataset):
    #setup environment if necessary
    try:
        nltk.download('stopwords')
        nltk.download('punkt')
    except:
        pass
    outpath = 'EDA/image/'
    
    #load the dataset
    df = pd.read_csv(dataset)
    
    #plot countries
    df = df[df.geo_country_code.isin(['NZ','AU','CA','GB','US'])]
    data = pd.DataFrame(df['geo_country_code'].value_counts())
    data['country'] = data.index
    fig = px.bar(data, x='country', y='geo_country_code',
                 title='Country Distribution of Tweets')
    fig.write_image(outpath + 'country_distribution.png')

    #token distribution
    clean = '@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+'
    stop_words = set(stopwords.words('english'))
    def filter_stopwords(text):
        return " ".join([word for word in word_tokenize(text) if word not in stop_words])
    def text_preprocessing(text):
        text = re.sub(clean, ' ', text)
        text = text.lower()
        text = filter_stopwords(text)
        return text
    df['text']=df['text'].apply(text_preprocessing)
    tokens = df['text'].str.split(expand=True).stack().value_counts().to_dict()
    token = pd.DataFrame.from_dict(tokens,orient='index', columns = ['count'])
    token.reset_index(inplace=True)
    token.columns = ['term','count']
    fig = px.scatter(token.head(20), x="count", y="term", title='Tokenization Top20 Words Frequency')
    fig.write_image(outpath + 'token_distribution.png')

    #word count
    df['text_length'] = df['text'].apply(lambda x:len(x))
    fig = px.box(df, y="text_length")
    fig.write_image(outpath + 'box_plot_tweet_length.png.png')

    #user_created_time
    df['user_created_time'] = df['user_created_time'].apply(lambda x:datetime.strptime(x[:10], '%Y-%m-%d'))
    fig = px.histogram(df, x="user_created_time", title='user_created_time')
    fig.write_image(outpath + 'user_created.png')
    

    #account history by country
    df['account_history'] = df['user_created_time'].apply(lambda x:(datetime.now()-x).days/365)
    aggd = df.groupby('geo_country_code').mean()
    aggd['country'] = aggd.index
    fig = px.bar(aggd, x='country', y='account_history',
                 title='Country Distribution of Tweets')
    fig.write_image(outpath + 'history_by_country.png')
    #plt.savefig(outpath + 'history_by_country.png')
    #plt.close()


if __name__ == '__main__':

    dataset = sys.argv[1]
    main(dataset)