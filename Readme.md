## Project Specifications 

Built using Flask API (1.0) and Python

## Get it running

**Step 1:**

Clone this repository:
```terminal
https://github.com/abhisheksoam/fetch_latest_tweet_api.git
```

**Step 2:**

> Make virtualenv and install dependendices using 
 

```terminal
virtualenv env
source env/bin/activate
pip install -r req.txt
```

**Step 3:**

Final Step
```terminal
Set up twitter credential
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

Run 
python api_tweet.py 
```


**Step 4:**

Check everything is working as expected

Head to browser for accesing API
```terminal
http://127.0.0.1:5000/{twitter_user_handle}
```

It should return success response


```terminal
{
    "result": [
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@radhika_apte  Will Ghoul respond to a non Muslim ?", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 1045547625351507969, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 1171857924, 
                        "indices": [
                            0, 
                            13
                        ], 
                        "id_str": "1171857924", 
                        "screen_name": "radhika_apte", 
                        "name": "Radhika Apte"
                    }
                ], 
                "hashtags": [], 
                "urls": []
            }, 
            "in_reply_to_screen_name": "radhika_apte", 
            "in_reply_to_user_id": 1171857924, 
            "retweet_count": 0, 
            "id_str": "1045547625351507969", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "1171857924", 
            "lang": "en", 
            "created_at": "Fri Sep 28 05:35:53 +0000 2018", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@PaytmMall Are you still accepting the donation ???", 
            "is_quote_status": false, 
            "in_reply_to_status_id": 861892454982746112, 
            "id": 998423314698653696, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 834968066819678208, 
                        "indices": [
                            0, 
                            10
                        ], 
                        "id_str": "834968066819678208", 
                        "screen_name": "PaytmMall", 
                        "name": "Paytm Mall"
                    }
                ], 
                "hashtags": [], 
                "urls": []
            }, 
            "in_reply_to_screen_name": "PaytmMall", 
            "in_reply_to_user_id": 834968066819678208, 
            "retweet_count": 0, 
            "id_str": "998423314698653696", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "834968066819678208", 
            "lang": "en", 
            "created_at": "Mon May 21 04:40:42 +0000 2018", 
            "in_reply_to_status_id_str": "861892454982746112", 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@cinnamonsandhu Hey, Your voice is really beautiful. Can you please sing this one... Ik Mera Dil, Ik mere Nain 😁😬           #fan request", 
            "is_quote_status": false, 
            "in_reply_to_status_id": 967170887911751685, 
            "id": 977867258642026496, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 2724855406, 
                        "indices": [
                            0, 
                            15
                        ], 
                        "id_str": "2724855406", 
                        "screen_name": "cinnamonsandhu", 
                        "name": "Cinnamon Sandhu"
                    }
                ], 
                "hashtags": [
                    {
                        "indices": [
                            124, 
                            128
                        ], 
                        "text": "fan"
                    }
                ], 
                "urls": []
            }, 
            "in_reply_to_screen_name": "cinnamonsandhu", 
            "in_reply_to_user_id": 2724855406, 
            "retweet_count": 0, 
            "id_str": "977867258642026496", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "2724855406", 
            "lang": "en", 
            "created_at": "Sun Mar 25 11:18:17 +0000 2018", 
            "in_reply_to_status_id_str": "967170887911751685", 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": true, 
            "text": "@TikonaTIL From the past 4-5 days .. I haven’t seen a connectivity. Really troubled by poor experience of Tikona En… https://t.co/8vGk49CTqx", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 946661098538680320, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 370038433, 
                        "indices": [
                            0, 
                            10
                        ], 
                        "id_str": "370038433", 
                        "screen_name": "TikonaTIL", 
                        "name": "Tikona"
                    }
                ], 
                "hashtags": [], 
                "urls": [
                    {
                        "url": "https://t.co/8vGk49CTqx", 
                        "indices": [
                            117, 
                            140
                        ], 
                        "expanded_url": "https://twitter.com/i/web/status/946661098538680320", 
                        "display_url": "twitter.com/i/web/status/9…"
                    }
                ]
            }, 
            "in_reply_to_screen_name": "TikonaTIL", 
            "in_reply_to_user_id": 370038433, 
            "retweet_count": 0, 
            "id_str": "946661098538680320", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "370038433", 
            "lang": "en", 
            "created_at": "Fri Dec 29 08:36:08 +0000 2017", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@sudhirchaudhary Hello sir,Need your help on this matter. Student raised there voice against corruption\nMore detail:\nhttps://t.co/oO2PFdJTB2", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 852965678697021444, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 75246346, 
                        "indices": [
                            0, 
                            16
                        ], 
                        "id_str": "75246346", 
                        "screen_name": "sudhirchaudhary", 
                        "name": "Sudhir Chaudhary"
                    }
                ], 
                "hashtags": [], 
                "urls": [
                    {
                        "url": "https://t.co/oO2PFdJTB2", 
                        "indices": [
                            117, 
                            140
                        ], 
                        "expanded_url": "https://www.facebook.com/campusforgbpec/", 
                        "display_url": "facebook.com/campusforgbpec/"
                    }
                ]
            }, 
            "in_reply_to_screen_name": "sudhirchaudhary", 
            "in_reply_to_user_id": 75246346, 
            "retweet_count": 2, 
            "id_str": "852965678697021444", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "75246346", 
            "possibly_sensitive": false, 
            "lang": "en", 
            "created_at": "Fri Apr 14 19:23:59 +0000 2017", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@irrfank Sir, I like the story of namesake very much but I am not able to find that movie anywhere. Where do I get it? 😅🤔", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 847393992354390017, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 490442018, 
                        "indices": [
                            0, 
                            8
                        ], 
                        "id_str": "490442018", 
                        "screen_name": "irrfank", 
                        "name": "Irrfan"
                    }
                ], 
                "hashtags": [], 
                "urls": []
            }, 
            "in_reply_to_screen_name": "irrfank", 
            "in_reply_to_user_id": 490442018, 
            "retweet_count": 0, 
            "id_str": "847393992354390017", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "490442018", 
            "lang": "en", 
            "created_at": "Thu Mar 30 10:24:06 +0000 2017", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "#findNamesakeMovie I really want to watch this movie, Pls if anyone knows the link, anything. Just drop a message.", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 847349743495766017, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [], 
                "hashtags": [
                    {
                        "indices": [
                            0, 
                            18
                        ], 
                        "text": "findNamesakeMovie"
                    }
                ], 
                "urls": []
            }, 
            "in_reply_to_screen_name": null, 
            "in_reply_to_user_id": null, 
            "retweet_count": 0, 
            "id_str": "847349743495766017", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": null, 
            "lang": "en", 
            "created_at": "Thu Mar 30 07:28:16 +0000 2017", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "@Flipkart I don't understand. How can you guys initiate payment and debit the money without my knowledge. Shitty platform.Very disappointing", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 843076296188084229, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 57947109, 
                        "indices": [
                            0, 
                            9
                        ], 
                        "id_str": "57947109", 
                        "screen_name": "Flipkart", 
                        "name": "Flipkart"
                    }
                ], 
                "hashtags": [], 
                "urls": []
            }, 
            "in_reply_to_screen_name": "Flipkart", 
            "in_reply_to_user_id": 57947109, 
            "retweet_count": 0, 
            "id_str": "843076296188084229", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": "57947109", 
            "lang": "en", 
            "created_at": "Sat Mar 18 12:27:07 +0000 2017", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }, 
        {
            "contributors": null, 
            "truncated": false, 
            "text": "Who won the hackathon ? Does anyone know about it? #buildforindia", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 782804674814423041, 
            "favorite_count": 0, 
            "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [], 
                "hashtags": [
                    {
                        "indices": [
                            51, 
                            65
                        ], 
                        "text": "buildforindia"
                    }
                ], 
                "urls": []
            }, 
            "in_reply_to_screen_name": null, 
            "in_reply_to_user_id": null, 
            "retweet_count": 0, 
            "id_str": "782804674814423041", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": true, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 2460953959, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "translator_type": "none", 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 5, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "2460953959", 
                "profile_background_color": "C0DEED", 
                "listed_count": 0, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 9, 
                "description": "Trying to be a nice human being :)", 
                "friends_count": 19, 
                "location": "", 
                "profile_link_color": "1DA1F2", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/782805605207506944/xE51OKjQ_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2460953959/1475470372", 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "abhisheksoamraj", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 1, 
                "name": "abhishek soam", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Apr 24 07:34:30 +0000 2014", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": null, 
            "lang": "en", 
            "created_at": "Mon Oct 03 04:49:12 +0000 2016", 
            "in_reply_to_status_id_str": null, 
            "place": null
        }
    ], 
    "response": {
        "t_respcode": "", 
        "previous": null, 
        "t_msg": "", 
        "next": null
    }
}
```



**Step 5: Test API** 


You can definitely create your own tests for testing purpose.

That's it! Done :) 

If you find something wrong, drop a message!

