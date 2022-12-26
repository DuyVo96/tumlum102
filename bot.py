
import tweepy
import pandas as pd

consumer_key = "F7W9hOV2RRVQsKYTni4sECkLK"
consumer_secret = "lArpBzMJXHeamk8ra8imn3uP9hxNjEAwwtWdomHM0CbyEiumAu"
access_token = "465533586-6PtGQ59llkYzubRSuTxr2AZmbz7X1UiHLmWA8iTI"
access_token_secret = "iqw0c2xaE65pq6utQmVhjBIyu6OAfQ5K2S5BEI1nt9mOD"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

followers_scraped = []
followers_list = []


def scrape_user_followers(username):
    for i, _id in enumerate(tweepy.Cursor(api.get_friend_ids,
                                          screen_name=username).items()):
        print(i, _id)
        followers_scraped.append(_id)
    return followers_scraped


friends = scrape_user_followers('ShengMo0x')

for i in range(len(friends)):
    # screen_name = api.get_user(user_id=friends[i]).screen_name
    followers_list.append([i, api.get_user(user_id=friends[i]).screen_name])
    # print(i, screen_name)

df = pd.DataFrame(followers_list, columns=["Id", "Name"
                                           ])
df.to_csv("data.csv", index=False)
