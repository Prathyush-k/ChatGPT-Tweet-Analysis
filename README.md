# ChatGPT-Tweet-Analysis
#### **Current Status: Project Planning**

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
