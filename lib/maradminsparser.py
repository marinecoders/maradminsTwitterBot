# RSS Parser reads the MARADMINS page, determines what was last tweeted,
# and then passes dict of more recent tweets back to main.

import feedparser
from lib.getlatesttweet import getLatestTweet
from lib.accesstwitter import accessTwitter


class aTweet:
    def __init__(self, title, url):
        self.title = title
        self.url = url


def parseIt():

    api = accessTwitter()
    tweetText = getLatestTweet(api).splitlines()

    # Get the RSS page
    maradminPage = feedparser.parse('https://www.marines.mil/DesktopModules'
                                    '/ArticleCS/RSS.ashx?ContentType='
                                    '6&Site=481&max=10&category=14336')

    toReturn = []

    for entry in maradminPage.entries:
        if not (entry.title[0:50] == tweetText[2].strip()[0:50]):
            if (len(entry.title) > 80):
                toReturn.append(aTweet(entry.title[0:75] + "...", entry.link))
            else:
                toReturn.append(aTweet(entry.title, entry.link))
        else:
            break

    return toReturn, api
