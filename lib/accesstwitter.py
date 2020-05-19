import tweepy
import logging
import os
import sys

logger = logging.getLogger()


def accessTwitter():
    consumerKey = os.getenv("CONSUMER_KEY")
    consumerSecret = os.getenv("CONSUMER_SECRET")
    accessToken = os.getenv("ACCESS_TOKEN")
    accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

    # Authehnticate to twitter and create API object
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # Verify creds
    try:
        api.verify_credentials()
    except Exception:
        logger.error("Error creating API", exc_info=True)
        sys.exit(1)
    logger.info("API created")
    return api
