# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:08:57 2023

@author: user
"""
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "chatgpt lang:en until:2023-05-01 since:2023-01-01"
tweets = []
limits = 30000

column_names = ['url', 'date', 'content', 'username','displayname',
                'description', 'followersCount', 'friendsCount',
                'likeCount','retweetCount','verified','profileimage','location']


final_tweets = []
total_number = 100000

for index, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):

    user = tweet.user
    #english_text = re.sub(r'[^\x00-\x7F]+', ' ', tweet.content)
    
    tweet_data = [tweet.url, 
                  tweet.date, 
                  tweet.rawContent, 
                  user.username, 
                  user.renderedDescription,
                  user.description, 
                  user.followersCount,
                  user.friendsCount,
                  tweet.likeCount, 
                  tweet.retweetCount,
                  user.verified ,
                  user.profileImageUrl,
                  user.location
                  ]

    final_tweets.append(tweet_data)

    if(index == total_number):
        break
        
    
# Create the dataframe
final_tweets
final_tweets_df = pd.DataFrame(final_tweets, columns = column_names)
final_tweets_df
final_tweets_df.to_csv("../Data/chatgpt.csv")