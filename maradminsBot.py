from lib.maradminsparser import parseIt
import tweepy
import os
import logging
import sys
import time

logger = logging.getLogger()


# Get twitter access environment variables
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


# TODO require API as argument, once twitter auth is setup
def postTweets():
    tweetData = parseIt()
    for entry in tweetData:
        newTweet = "A new MARADMIN has been posted.\nTitle: " + entry.title + \
                   "\n\n" + entry.url
        print(newTweet)
        # api = accessTwitter()  # Change with TODO
        # api.update_status(newTweet)
        # api.send_direct_message(user_id="MarcSlaughter", text=newTweet)
        time.sleep(2)


if __name__ == "__main__":
    # api = accessTwitter()
    postTweets()
