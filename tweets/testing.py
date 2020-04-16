from searchtweets import gen_rule_payload, collect_results, load_credentials
import json
from datetime import datetime, timedelta

from twython import Twython

print("hi ashok")
# appended_tweets = []
# screen_name = "ABhadrappa"
# hash_tag = "#terracegardening"
#
# twitter = Twython("6BclGDOiM9wq2tSZccn75KKkL", "O7OQSgu596QOHiKrr6u2ZlAQwWm4952QF3A1rG678EmPUX4CWN", oauth_version=2)
# access_token = twitter.obtain_access_token()
# current_time = datetime.now() + timedelta(minutes=-1)
# to_date = current_time.strftime("%Y%m%d%H%M")
# print("toDate:", to_date)
#
# from_time = datetime.now() + timedelta(days=-90, hours=-2, minutes=-1)
# from_date = from_time.strftime("%Y%m%d%H%M")
# print("fromDate:", from_date)
# tweet_window = {"to_date": to_date, "from_date": from_date}
#
# rule = gen_rule_payload("from:" + screen_name + " lang:en " + hash_tag,
#                             from_date=str(tweet_window['from_date']),
#                             to_date=str(tweet_window['to_date']),
#                             results_per_call=100)
# print("rule:", rule)
# end_point = "https://api.twitter.com/1.1/tweets/search/fullarchive/AshokTwitterFullArchive.json"
# search_args = {
#         "bearer_token": access_token,
#         "endpoint": end_point}
# tweets_list = collect_results(rule,
#                              max_results=100,
#                              result_stream_args=search_args)
# appended_tweets = []
# for tweet in tweets_list:
#     appended_tweets.append(str(tweet.created_at_datetime)+" "+tweet.text)
#     appended_tweets.append("\n\n")
#
# tweets_count = len(tweets_list)
# print("tweet count " +str(tweets_count))
#
# response = "Number of tweets for a given hashtag "+hash_tag + "\n" \
#                 "by a given twitter account " + screen_name + "\n"

userlist = {
    {
        "users": [
                {
                    "name": "Bhabani Shankar",
                    "screen_name": "itzbsp",
                },
                {
                    "name": "qweqweqweqweqw",
                    "screen_name": "asdasdasd",
                }
            ],
            "next_cursor": 0
    }
}
follower_list = []
next_cursor = -1
while next_cursor:
    for follower_name in userlist["users"]:
        follower_list.append(follower_name["screen_name"].encode("UTF-8"))
    next_cursor = follower_name["users"]["next_cursor"]
