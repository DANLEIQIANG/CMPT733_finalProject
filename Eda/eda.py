import pandas as pd
from nltk.corpus import stopwords
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import nltk
import re
from nltk.tokenize import word_tokenize

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
    df['geo_country_code'].value_counts().plot(kind="barh")
    plt.title('Country Distribution of Tweets')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.gca().invert_yaxis()
    plt.savefig(outpath + 'country_distribution.png')
    plt.close()

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
    plt.figure()
    plt.scatter(x = list(token[:20]['count']),
                            y =list(token[:20]['term']),
                            linewidths = 2,
                            edgecolor='b',
                            alpha = 0.5)
    plt.title('Tokenization Top20 Words Frequency')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.gca().invert_yaxis()
    plt.savefig(outpath + 'token_distribution.png')
    plt.close()

    #word count
    df['text_length'] = df['text'].apply(lambda x:len(x))
    plt.figure()
    sns.boxplot(x=df['text_length']).set_title('Word count in Each Tweet')
    plt.title('Word count in Each Tweet')
    plt.xlabel('Length')
    plt.savefig(outpath + 'box_plot_tweet_length.png')
    plt.close()

    #user_created_time
    df['user_created_time'] = df['user_created_time'].apply(lambda x:datetime.strptime(x[:10], '%Y-%m-%d'))
    plt.figure()
    plt.hist(x=df['user_created_time'])
    plt.title('user_created_time')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.savefig(outpath + 'user_created.png')
    plt.close()

    #account history by country
    df['account_history'] = df['user_created_time'].apply(lambda x:(datetime.now()-x).days/365)
    aggd = df.groupby('geo_country_code').mean()
    plt.figure()
    plt.bar(aggd.index.tolist(),aggd['account_history'])
    plt.title('average account history by country')
    plt.xlabel('Country')
    plt.ylabel('Years')
    plt.savefig(outpath + 'history_by_country.png')
    plt.close()


if __name__ == '__main__':

    dataset = sys.argv[1]
    main(dataset)