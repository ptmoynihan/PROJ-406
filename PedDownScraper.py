# %% Import Modules
import snscrape.modules.twitter as sntwitter
import pandas as pd

#%% Welcome
print("Welcome to SNScrape")

tweet_list = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:peddownyyc').get_items()):
    if i > 100:
        break
    tweet_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Create Dataframe
tweets_df = pd.DataFrame(tweet_list, columns = ['Datetime', 'Tweet ID', 'Text', 'Username'])

# %% Save as csv
tweets_df.head
tweets_df.to_csv('peddowntweets.csv')
# %%
