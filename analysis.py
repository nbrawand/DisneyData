from textblob import TextBlob
import re
import json
import numpy

def clean_tweet(line):
        '''
        Utility function to clean tweet text by removing links, special characters.
        '''
        line = removeLink(line)
        line = line.replace('@', '')
        line = line.replace('#', '')
        return line

def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
#    print(analysis.raw)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def removeLink(line):

    pattern = 'https'
    line = line.split(' ')
    tmp = []

    for elm in line:
        if not pattern in elm:
            tmp.append(elm)

    line = ''
    for l in tmp:
        line += l+' '

    if pattern in line:
        removeLink(line)
    else:
        return line

def get_text(line):
    """json loads fails for many tweets this hack is ugly but doesn't loose data"""
    line = line.replace(r'\r','\n')
    try:
        line = json.loads(line) # data loss
        line = line['text']
    except:
        #print(line)
        first = ',"text":'
        #last = ',"source":'
        last = '","'
        line = find_between(line.replace("('negative', '  tweet:'", ''), first, last)

    #line = clean_tweet(line)
    return line


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

fil = open('log', 'r')

print("")
for line in fil.readlines():

    if line == '' or line == ' ':
        continue

    line = get_text(line)
    line = clean_tweet(line)

    if line == '' or line == ' ':
        continue

    #if (not 'pandora' in line )or (not 'Pandora' in line):
    #    continue

    sentiment = get_tweet_sentiment(line)
    print(line,sentiment)

print("")
