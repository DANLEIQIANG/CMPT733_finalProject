
  <h1 align="center">Twitter Sentiment Analysis in Significant Event</h1>

  <p align="center">
    Kunkun group
  </p>
</div>







<!-- ABOUT THE PROJECT -->
## About The Project

In today's society, people are accustomed to expressing their various emotions through social media platforms. Sentiment analysis of tweets posted by Twitter users can reveal whether people's perceptions of a product or event are negative, neutral or positive. Sentiment analysis is most commonly used in e-commerce campaigns. By analyzing these massive reviews, sentiment analysis can help businesses convert dissatisfied users into advocates. Sentiment analysis enables businesses to capture consumers’ opinions in real-time. This real-time information helps companies develop new marketing strategies, improve product functionality, and predict the likelihood of product failure. Sentiment analysis is also of great help in managing their brand image. By analyzing public comments, sentiment analysis also can help governments assess their strengths and weaknesses. Taking the comparison of the US Presidential election as an example, Twitter sentiment analysis can conduct public opinion perception, filter out the public's views and tendencies on events, and then make some predictions about the election and formulate public strategies. 
 

Our final data product is a web application with three main functions. We build the back-end of the web application through Flask, save labeled data in MySQL, build the front-end with React, and encapsulate the components in Echarts for generating dynamic graphs by reading data from the database.




### Built With
Main technolohies:

* [Flask](https://nextjs.org/)
* [React.js](https://reactjs.org/)
* [MySql](https://vuejs.org/)
* [Scikit-learn](https://angular.io/)
* [Pandas](https://svelte.dev/)
* [NLTK](https://laravel.com)
* [Plotly](https://getbootstrap.com)
* [matplotlib](https://jquery.com)




<!-- GETTING STARTED -->
## Getting Started

<h3>Front-end:</h3>

### Prerequisites

Download React.js

### Start Commend:

In Frond-end folder:

Start frond-end service in port 3000:
   ```sh
   npm start
   ```
<h3>Back-end:</h3>

### Prerequisites

Download Flask, MySQL
### Start Commend:

In Backer-end folder -> Mock_Server folder -> HelloWorld folder:

Start Back-end service in port 5000:
   ```sh
   python model.py
   ```

### Repo Directory
|Directory  |Description|
|-|-|-|
|Dataprep|Twitter data collection scripts.|
|Dataset|All datasets in project. <br/>Datasets with suffix 'labeled' are datasets labeled by model.|
|Eda|Data cleaning, eda and image generation scripts.|
|Model|Machine learning models.|
|Frontend|Web application frontend.|
|Backend|Web application backend.|

