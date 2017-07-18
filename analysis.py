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


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

fil = open('log', 'r') # read raw tweet data from log
outfil = open('tweetdata','w') # dump clean data to tweetdata for analysis
outfil.write('date~,~tweet~,~sentiment\n')
for line in fil.readlines():

    # skip if line is empty
    if line == '' or line == ' ':
        continue

    line = line.replace(r'\r','\n')

    # try to load data as a dict
    try:
        line = json.loads(line)
    except:
        continue

    # keep timestamp
    time = line['created_at']

    # get clean tweet
    text = clean_tweet(line['text'])

    if text == '' or text == ' ':
        continue

    #if (not 'pandora' in line )or (not 'Pandora' in line):
    #    continue

    sentiment = get_tweet_sentiment(text)

    # write to file
    outfil.write("{}~,~{}~,~{}\n".format(time, text, sentiment))

outfil.close()
fil.close()
