# RSS Parser reads the MARADMINS page, determines what was last tweeted,
# and then passes dict of more recent tweets back to main.

import feedparser
from pathlib import Path


class aTweet:
    def __init__(self, title, url):
        self.title = title
        self.url = url


def parseIt():
    # TODO: make this generic...
    projectPath = Path('/Users/Marc/Documents/maradminsTwitterBot/lib')

    lastTweetFile = projectPath / "lastTweet.txt"

    lastTweet = open(lastTweetFile, 'r+')
    lines = lastTweet.readlines()

    # Get the RSS page
    maradminPage = feedparser.parse('https://www.marines.mil/DesktopModules'
                                    '/ArticleCS/RSS.ashx?ContentType='
                                    '6&Site=481&max=10&category=14336')

    toReturn = []

    for entry in maradminPage.entries:
        if not (entry.title == lines[0].strip()):
            if (len(entry.title) > 80):
                toReturn.append(aTweet(entry.title[0:75] + "...", entry.link))
            else:
                toReturn.append(aTweet(entry.title, entry.link))
        else:
            break

    lastTweet.seek(0)
    lastTweet.write(maradminPage.entries[0].title)

    return toReturn
