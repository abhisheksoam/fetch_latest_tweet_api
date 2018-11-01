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
http://127.0.0.1:5000/api/tweets/{twitter_user_handle}
```

It should return success response


```terminal
{
    "result": [
        {
            "username": "narendramodi", 
            "tweet": "This relationship augurs well for the people of our two countries, and is also an anchor for peace and prosperity i… https://t.co/aQuubq9WMQ", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057876014984921089, 
            "favorite_count": 2261
        }, 
        {
            "username": "narendramodi", 
            "tweet": "I fully agree with PM @AbeShinzo and cherish our close friendship. My visit to Japan saw many new milestones in the… https://t.co/y7WWVlEOA7", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057876013424623616, 
            "favorite_count": 2520
        }, 
        {
            "username": "narendramodi", 
            "tweet": "印日関係は両国の国民に利益をもたらすものであり、インド太平洋の平和と繁栄を繋ぎとめる錨でもあります。これらの目標に深い興味を持ってくださっている安倍首相に感謝します。目標を実現するためこれからも安倍首相とともに仕事をすることを楽しみにしています。", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057876011923075072, 
            "favorite_count": 580
        }, 
        {
            "username": "narendramodi", 
            "tweet": "安倍首相のお言葉に完全に同意します。私は首相との緊密な友情をかけがえのないものと感じます。この度の日本訪問では、印日特別戦略的グローバルパートナーシップにとって節目となる多くの合意がありました。 https://t.co/lXgMS7YW2o", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057876010291552257, 
            "favorite_count": 2706
        }, 
        {
            "username": "narendramodi", 
            "tweet": "भारत की हृदयस्थली यानि मध्य प्रदेश ने हमेशा मातृभूमि के विकास में अग्रणी भूमिका निभाई है। \n\nपिछले 15 वर्षों में रा… https://t.co/NfXcMCxfpl", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057821367192641536, 
            "favorite_count": 14790
        }, 
        {
            "username": "narendramodi", 
            "tweet": "Greetings to my sisters and brothers of Karnataka on the special occasion of Karnataka Rajyotsava. Karnataka is hom… https://t.co/cCgFqag8pa", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057821231234203648, 
            "favorite_count": 5299
        }, 
        {
            "username": "narendramodi", 
            "tweet": "ರಾಜ್ಯೋತ್ಸವದ ವಿಶೇಷ ಸಂದರ್ಭದಲ್ಲಿ ಕರ್ನಾಟಕದ ನನ್ನ ಸಹೋದರ ಸಹೋದರಿಯರಿಗೆ ಶುಭಾಶಯಗಳು. ಕರ್ನಾಟಕ ಶ್ರೀಮಂತ ಇತಿಹಾಸ ಹೊಂದಿದ್ದು, ವಿವಿಧ ಕ್… https://t.co/tC9CpPogqG", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057821226922500097, 
            "favorite_count": 10644
        }, 
        {
            "username": "narendramodi", 
            "tweet": "यह अटल जी की दूरदृष्टि थी कि छत्तीसगढ़ के गठन का सपना साकार हुआ। \n\nसमय के साथ राज्य ने कई क्षेत्रों में विशेषकर कृ… https://t.co/Ymh84a8WLv", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057820698389827585, 
            "favorite_count": 12257
        }, 
        {
            "username": "narendramodi", 
            "tweet": "हरियाणा परिश्रम, पुरुषार्थ, साहस और देश के प्रति समर्पण की भूमि है। \n\nयह हमें अन्न देने वाले किसानों और देश की रक्… https://t.co/5Z8rOArqYH", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057820518609547264, 
            "favorite_count": 7583
        }, 
        {
            "username": "narendramodi", 
            "tweet": "Kerala Piravi greetings! Kerala has a wonderful culture and has always emphasised on human empowerment. It’s people… https://t.co/3QpvuvSToc", 
            "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
            "id": 1057820303613669376, 
            "favorite_count": 2537
        }
    ], 
    "response": {
        "t_respcode": "", 
        "previous": null, 
        "t_msg": "", 
        "next": "http://127.0.0.1:5000/narendramodi/?since_id=1057820303613669377"
    }
}
```



**Step 5: Test API** 



That's it! Done :) 

If you find something wrong, drop a message!

