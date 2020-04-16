from twython import Twython
from searchtweets import gen_rule_payload, collect_results, load_credentials
import os

import json


def app_only_oauth_access_token(consumer_key, consumer_key_secret):
    twitter = Twython(consumer_key, consumer_key_secret, oauth_version=2)
    return twitter.obtain_access_token()
