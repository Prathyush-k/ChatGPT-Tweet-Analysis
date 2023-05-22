# ChatGPT-Tweet-Analysis
#### **Current Status: Working**

## Objective
The objective of this GitHub repository is to explore and analyze the usage of ChatGPT through sentiment analysis, visualization, and topic modeling techniques. The goal is to gain insights into how ChatGPT is being used and what people are saying about it on Twitter. Additionally, we aim to identify which professions are utilizing ChatGPT the most.

## Dataset
We will utilize a combination of existing data from Kaggle and data obtained through the Twitter API. By combining these sources, we aim to create a comprehensive dataset that includes a diverse range of tweets related to our research topic. 

Dataset Source 1: [Kaggle](https://www.kaggle.com/datasets/khalidryder777/500k-chatgpt-tweets-jan-mar-2023)
<!-- [comment]: #  The dataset used in this project will be made publicly available in the data directory of this GitHub repository. -->

Dataset Source 2: [Twitter](https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/blob/main/Scrape_Twitter.py)<br />
This has the code to scrape data from twitter using keywords

## Tools
#### *deciding*

The following tools and libraries will be used in this project:

1) **Python:** A popular programming language for data analysis and machine learning.
2) **Pandas:** A Python library used for data manipulation and analysis.
3) **Matplotlib:** A Python library used for data visualization and plotting.
4) **Tableau:** A data visualization software that can be used to create interactive dashboards and visualizations.

## Pre-Processing
Code: [Cleaning Data](https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/blob/main/Clean%20Data.ipynb)
1) Removed Null, duplicate values.
2) Removed Stopwords, emails, urls.
3) Changed emojis into text to keep the semantic meaning ( 😂: face_with_tears_of_joy).
4) Normalized text (Françoiš': Francois).
5) Removed special characters, extra spaces, usernames, etc.


## Descriptive Analysis
### Word Cloud
The word cloud visualizes the main words/topics used in tweets during the specified time period.

<img src="https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/blob/main/twitter_unigram.png" height="500" /> 

### Latent Dirichlet Allocation (LDA)
We used LDA topic modelling to seperate the data into 10 topics. We also have the top words from each of the topics.

#### Grid Search for selecting the best parameters.<br />
We optimized the Alpha value and the number of topics selected using grid search.
The best topics should have the least similarity among themselves and highest coherence.

Implemented code to select the best parameters for the LDA model which has the least jaccard_similarity and highest u_mass coherence.

**Alpha value:**  0.2 **Number of Topics:**  12

![image](https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/assets/40651916/d83beafc-c6b0-4830-bb72-9370c043cf5b)

### Sentiment Analysis
Hugging Face model is utilized for sentiment analysis of the top 10k tweets. The overall sentiment is mostly neutral and positive, with very few negative sentiments. 

![image](https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/assets/40651916/7421c3ad-fc98-4c79-8c2f-380f6d3e8374)

We also plotted graphs for each of the topics created by the LDA topic modeling.

#### General topics
Selected few related topics and plotted the average sentiment of tweet for these topics.

![image](https://github.com/Prathyush-k/ChatGPT-Tweet-Analysis/assets/40651916/75416030-ea18-46d0-8663-cfb905e298b5)

