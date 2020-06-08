def getLatestTweet(api):

    tweet = api.user_timeline(count=1)
    tweetText = tweet[0].text

    return tweetText
