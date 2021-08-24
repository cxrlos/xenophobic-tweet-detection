# Saved API key  to excluded python module so I don't upload it by mistake
import env as env
import time

import paralleldots
paralleldots.set_api_key(env.PARALLELDOTS_APIKEY_3)

# Start and end values included because the API has a 1000 request limit per day
def paralleldots_classification(start, end, json_data):
    for i in range (start, end):

        # Rate limit, prevents documents from becoming unlabeled
        if(i%6==0 and i!=0):
            print("Waiting for rate limit to pass...")
            time.sleep(60)
            print("-----------------------------------------------")

        print("Document ", start + i + 1)
        print(json_data[i]['Text'])

        print("Sentiment analysis... ", end='')
        response = paralleldots.sentiment(json_data[i]['Text'])
        json_data[i].update(response)

        print("OK\nEmotion analysis... ", end='')
        response = paralleldots.emotion(json_data[i]['Text'])
        json_data[i].update(response)

        print("OK\nIntent analysis...", end='')
        response = paralleldots.intent(json_data[i]['Text'])
        json_data[i].update(response)
        print("OK")
        print("-----------------------------------------------")
    return json_data

    # for i in range (0, 750):
    #     print(i)

