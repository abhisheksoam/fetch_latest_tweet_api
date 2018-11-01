__author__ = 'abhishek'

import os
import sys

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from config import twitter_api

app = FlaskAPI(__name__)


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


def get_user_tweets(user_name, since_id=None, max=None):
    try:
        response = default_response()

        total_count = 10
        tweet_list = []

        next, prev = None, None
        tweets = []
        try:
            if since_id is not None and max is None:
                tweets = twitter_api.user_timeline(screen_name=user_name, count=total_count, max_id=int(since_id) + 1)
            elif since_id is None and max is not None:
                tweets = twitter_api.user_timeline(screen_name=user_name, count=total_count, since_id=int(max) - 1)
            else:
                tweets = twitter_api.user_timeline(screen_name=user_name, count=total_count)

        except Exception as e:
            response['response']['t_msg'] = "{twitter_reason}".format(twitter_reason=e.message[0]['message'])
            response['response']['t_respcode'] = e.api_code

        # If there are tweets present of a user, Set Pagination for next and prev element

        if len(tweets) != 0:
            if len(tweets) == total_count:
                next = request.host_url.rstrip('/') + url_for('user_tweets',
                                                              user_handle=user_name,
                                                              since_id=tweets[len(tweets) - 1]._json['id']
                                                              )

            if since_id is not None:
                prev = request.host_url.rstrip('/') + url_for('user_tweets',
                                                              user_handle=user_name,
                                                              max=tweets[0]._json['id']
                                                              )

            for index, tweet in enumerate(tweets):
                tweet_list.append(tweet._json)

        response['result'] = tweet_list
        response['response']['next'] = next
        response['response']['previous'] = prev

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    finally:
        return response


@app.route("/<string:user_handle>/", methods=['GET'])
def user_tweets(user_handle):
    if request.method == 'GET':
        since_id = request.args.get('since_id')
        end_id = request.args.get('max')
        return get_user_tweets(user_handle, since_id, end_id), status.HTTP_200_OK
    else:
        return '', status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    app.run(debug=True)
