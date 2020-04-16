from twython import Twython
import os
import json


def followerlistsearch(event, context):

    print(event)
    event_string = json.dumps(event)
    data = json.loads(event_string)
    screen_name = data['queryStringParameters']['screenname']

    access_token = app_only_oauth_access_token(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])

    twitter = Twython(access_token=access_token)

    follower_list = []
    # This is to go through paginated results
    next_cursor = -1

    while next_cursor:
        followers = twitter.get_followers_list(screen_name=screen_name, count=200, cursor=next_cursor)
        for follower_name in followers["users"]:
            follower_list.append("Follower Twitter A/c " + follower_name["screen_name"]+" and its tweet count " + str(follower_name["statuses_count"]))
        next_cursor = followers["next_cursor"]

    json_response = {
        "Given TwitterAccount": screen_name,
        "FollowersList": follower_list
    }

    output = {'statusCode': 200, 'body': json.dumps(json_response)}
    return output


def app_only_oauth_access_token(consumer_key, consumer_key_secret):
    twitter = Twython(consumer_key, consumer_key_secret, oauth_version=2)
    return twitter.obtain_access_token()
