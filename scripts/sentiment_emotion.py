# Saved API key  to excluded python module so I don't upload it by mistake
import env as env

import paralleldots
paralleldots.set_api_key(env.PARALLELDOTS_APIKEY)

def paralleldots_classification(start, end, json_data):
    for i in range (start, end):
        response = paralleldots.sentiment(json_data[i]["Text"])
        print(response)
        json_data[i].update(response)
        response = paralleldots.emotion(json_data[i]["Text"])
        print(response)
        json_data[i].update(response)
        response = paralleldots.intent(json_data[i]["Text"])
        print(response)
        json_data[i].update(response)
    return json_data

    # for i in range (0, 750):
    #     print(i)

