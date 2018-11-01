__author__ = 'abhishek'

import os
import sys
import tweepy

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from config import consumer_key, consumer_secret, access_token, access_token_secret

app = FlaskAPI(__name__)


# Sample Response of our API
def default_response():
    return {
        'result': [],
        'response': {
            'next': None,  # Next 10 elements if it has next tweets
            'previous': None,  # Previous 10 element
            't_msg': '',  # Twitter Msg
            't_respcode': ''  # Twitter Response Code
        }
    }


class Tweet:
    _total_count = 10  # Total Tweet Count

    def __init__(self, username, since_id, max):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.twitter_api = tweepy.API(auth)
        self.user_name = username
        self.since_id = since_id
        self.max = max

    def __repr__(self):
        return "%s, %s, %s" % (self.user_name, self.since_id, self.max)

    def get_user_tweets(self):
        try:
            response = default_response()
            tweet_list = []
            next, prev = None, None

            tweets = []
            try:
                if self.since_id is not None and self.max is None:
                    tweets = self.twitter_api.user_timeline(screen_name=self.user_name,
                                                            count=self._total_count,
                                                            max_id=int(self.since_id) + 1)

                elif self.since_id is None and self.max is not None:
                    tweets = self.twitter_api.user_timeline(screen_name=self.user_name,
                                                            since_id=int(self.max),
                                                            count=self._total_count)
                else:
                    tweets = self.twitter_api.user_timeline(screen_name=self.user_name,
                                                            count=self._total_count)

            except Exception as e:
                response['response']['t_msg'] = "{twitter_reason}".format(twitter_reason=e.message[0]['message'])
                response['response']['t_respcode'] = e.api_code

            # If there are tweets present of a user, Set Pagination for next and prev element
            if len(tweets) != 0:

                # If number of tweets are equal to the total count, then send an next element
                if len(tweets) == self._total_count:
                    next = request.host_url.rstrip('/') + url_for('user_tweets',
                                                                  user_handle=self.user_name,
                                                                  since_id=long(
                                                                      tweets[len(tweets) - 1]._json['id']) + 1)

                if self.since_id is not None and self.max is None:
                    prev = request.host_url.rstrip('/') + url_for('user_tweets',
                                                                  user_handle=self.user_name,
                                                                  max_id=int(tweets[0]._json['id'])
                                                                  )

                # Enumerating over list and appending the tweets data into the tweet_list
                for index, tweet in enumerate(tweets):
                    tweet_list.append({
                        'tweet': tweet._json['text'],
                        'id': tweet._json['id'],
                        'username': self.user_name,
                        'profile_background_image_url_https': tweet._json['user']['profile_background_image_url_https'],
                        'favorite_count': tweet._json['favorite_count']
                    })

            response['result'] = tweet_list
            response['response']['next'] = next
            response['response']['previous'] = prev

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, e)

        finally:
            return response


@app.route("/api/tweets/<string:user_handle>/", methods=['GET'])
def user_tweets(user_handle):
    if request.method == 'GET':
        since_id = request.args.get('since_id')
        end_id = request.args.get('max')
        tweets = Tweet(user_handle, since_id, end_id)
        return tweets.get_user_tweets(), status.HTTP_200_OK
    else:
        return '', status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    app.run(debug=True)
