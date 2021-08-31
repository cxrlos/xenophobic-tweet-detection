from scripts import sentiment_emotion, json_handler

def main():
    m_select = 1
    while m_select != 0:
        print("--- MENU ---")
        print("1.- Convert CSV to JS")
        print("2.- Classify the JSON data")
        print("0.- Exit")

        m_select = int(input("Select an option "))
        if m_select == 1:
            # Batches, because the API has a 1000 request limit per day
            # processed_json_data = sentiment_emotion.paralleldots_classification(1356, 1500, json_data)
            # json_handler.json_out(processed_json_data, 'data/TrainingDS.json')
            print("\nDisabled ATM to avoid data loss\n")
        if m_select == 2:
            # Pass the csv values to a JSON file
            # json_handler.data_to_json('data/TrainingDS.csv')
            # json_data = json_handler.load_json('data/TrainingDS.json')
            print("\nDisabled ATM to avoid data loss\n")

if __name__ == "__main__":
    main()
