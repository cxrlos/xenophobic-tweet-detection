from scripts import sentiment_emotion, json_handler

def main():
    # The line below was used to pass the csv values to a JSON file initially, 
    # the reason it's commented is because I only intend to update it in the 
    # following weeks.
    # json_handler.data_to_json('data/TrainingDS.csv')
    json_data = json_handler.load_json('data/TrainingDS.json')

    # Batches, because the API has a 1000 request limit per day
    processed_json_data = sentiment_emotion.paralleldots_classification(200, 210, json_data)
    json_handler.json_out(processed_json_data, 'data/TrainingDS.json')


if __name__ == "__main__":
    main()
