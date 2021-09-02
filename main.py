from scripts import sentiment_emotion, json_handler

def main():
    print("\n\n\n-----------------------------------------------")
    print("Due to API limitations anc frequent errors, processing more than 200 elements is not recommended.")
    print("-----------------------------------------------\n\n\n")

    a = int(input("Enter the number of the first element to process... "))
    b = int(input("Enter the number of the last element to process... "))

    # Pass the csv values to a JSON file
    json_handler.data_to_json('data/TrainingDS.csv')
    json_data = json_handler.load_json('data/TrainingDS.json')

    # Batches, because the API has a 1000 request limit per day
    processed_json_data = sentiment_emotion.paralleldots_classification(a-1, b, json_data)
    json_handler.json_out(processed_json_data, 'data/TrainingDS.json')

    # Tried a lot of methods to implement a JSON to CSV method but had datatype
    # issues. Used an online tool instead.
    print("\n\n\n-----------------------------------------------")
    print("To convert the output JSON file, please use https://data.page/json/csv")
    print("-----------------------------------------------\n\n\n")

if __name__ == "__main__":
    main()
