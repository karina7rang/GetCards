
import tweepy 
import wget
import os
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Fill these in
auth.set_access_token(access_token, access_token_secret)  #Fill these in

api = tweepy.API(auth)

#Get 200 of Chris' tweet
tweets = api.user_timeline(screen_name = 'chrisalbon', 
                           count = 100, 
                           include_rts = False, 
                           excludereplies = True)

if 1==1:
    #200 isn't enough.  Keep getting tweets until we can't get anymore
    last_id = tweets[-1].id
    
    while (True):
        more_tweets = api.user_timeline(screen_name='chrisalbon',
                                    count=200,
                                    include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id-1)
                                        
        # There are no more tweets
        if (len(more_tweets) == 0):
              break
        else:
              last_id = more_tweets[-1].id-1
              tweets = tweets + more_tweets

    print(len(tweets))    

if 1==2:        
    #Filter by those containing #machinelearningflashcards 
    card_tweets = [j for j in tweets if 'machinelearningflashcards' in j.text]
elif 1==1:
    x = [i for i in tweets if 'urls' in i.entities.keys()]
    x = [i for i in x if len(i.entities['urls'])>0]
    card_tweets = [i for i in x if 'machinelearningflashcards' in i.entities['urls'][0]['expanded_url']]

if 1==1:
    media_files = set()
    for status in card_tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0 and media[0]['type']=='photo' ): #if tweet has media and media is photo
            media_files.add(media[0]['media_url']) #get me the url

    print(len(media_files))

if 1==2:
    for media_file in media_files:
        wget.download(media_file, out = './output_cards/') #get the photos!