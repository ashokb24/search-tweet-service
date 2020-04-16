from searchtweets import gen_rule_payload, collect_results, load_credentials
from twython import Twython
from datetime import datetime, timedelta
import os

import json


def fullarchivetweetsearch(event, context):
    data = json.loads(event['body'])
    screen_name = data['screenname']
    hash_tag = data['hashtag']
    from_past_number_of_days = data['numberofDays']

    """
        Call the method to get the access token
    """
    access_token = app_only_oauth_access_token(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

    from_to_dates = get_tweet_time_window(from_past_number_of_days)
    """
       Generate the rule criteria to filter the tweets
    """
    rule = gen_rule_payload("from:" + screen_name + " lang:en " + hash_tag,
                            from_date=str(from_to_dates['from_date']),
                            to_date=str(from_to_dates['to_date']),
                            results_per_call=100)
    print("rule:", rule)

    search_args = {
        "bearer_token": access_token,
        "endpoint": os.environ['FULLARCHIVE_TWEETSEARCH_ENDPOINT']}

    """
        calling the twitter api
    """
    tweets_list = collect_results(rule,
                                  max_results=100,
                                  result_stream_args=search_args)
    appended_tweets = []
    """
        Iterating the twitter search response
    """
    for tweet in tweets_list:
        appended_tweets.append(str(tweet.created_at_datetime) + " " + tweet.text)

    json_response = {
        "Given Hashtag": hash_tag,
        "Given TwitterAccount": screen_name,
        "Tweet count": str(len(tweets_list)),
        "Tweet Text": appended_tweets
    }
    output = {'statusCode': 200, 'body': json.dumps(json_response)}
    return output


"""
    Given a consumer key and consumer key secret, this method will return Access Token
"""


def app_only_oauth_access_token(consumer_key, consumer_key_secret):
    twitter = Twython(consumer_key, consumer_key_secret, oauth_version=2)
    return twitter.obtain_access_token()


def get_tweet_time_window(from_past_number_of_days):
    current_time = datetime.now() + timedelta(minutes=-1)
    to_date = current_time.strftime("%Y%m%d%H%M")
    print("toDate:", to_date)

    from_time = datetime.now() + timedelta(days=-from_past_number_of_days, hours=-2, minutes=-1)
    from_date = from_time.strftime("%Y%m%d%H%M")
    print("fromDate:", from_date)
    tweet_window = {"to_date": to_date, "from_date": from_date}
    return tweet_window
