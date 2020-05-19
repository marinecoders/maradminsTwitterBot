from lib.maradminsparser import parseIt
import logging
import time

logger = logging.getLogger()


def postTweets():
    tweetData, api = parseIt()
    for entry in tweetData:
        newTweet = "A new MARADMIN has been posted.\n\n" + entry.title + \
                   "\n\n" + entry.url
        print(newTweet)
        # api.update_status(newTweet)
        # api.send_direct_message(user_id="MarcSlaughter", text=newTweet)
        time.sleep(2)


if __name__ == "__main__":
    postTweets()
