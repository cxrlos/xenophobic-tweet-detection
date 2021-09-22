# from scripts import sentiment_emotion, json_handler
from scripts import calculated_features

def main():
    # print("\n\n\n-----------------------------------------------")
    # print("Due to API limitations anc frequent errors, processing more than 200 elements is not recommended.")
    # print("-----------------------------------------------\n\n\n")

    # a = int(input("Enter the number of the first element to process... "))
    # b = int(input("Enter the number of the last element to process... "))

    # Pass the csv values to a JSON file
    # json_handler.data_to_json('data/TestingDS.csv', 'data/TestingDS.json')
    # json_data = json_handler.load_json('data/TestingDS.json')

    # Batches, because the API has a 1000 request limit per day
    # processed_json_data = sentiment_emotion.paralleldots_classification(a-1, b, json_data)
    # json_handler.json_out(processed_json_data, 'data/TestingDS.json')

    # Tried a lot of methods to implement a JSON to CSV method but had datatype
    # issues. Used an online tool instead.
    # print("\n\n\n-----------------------------------------------")
    # print("To convert the output JSON file, please use https://data.page/json/csv")
    # print("-----------------------------------------------\n\n\n")
    # mod_train_set = calculated_features.percentageSpecialChars('./data/Processed_Training.csv')
    # mod_test_set = calculated_features.percentageSpecialChars('./data/Processed_Testing.csv')
    # calculated_features.listToCSV(mod_train_set, './data/deliveries/delivery-4/Processed_Training.csv')
    # calculated_features.listToCSV(mod_test_set, './data/deliveries/delivery-4/Processed_Testing.csv')

    mod_train_set= calculated_features.percentageCaps('./data/Processed_Training.csv') 
    mod_test_set = calculated_features.percentageCaps('./data/Processed_Testing.csv') 
    calculated_features.listToCSV(mod_train_set, './data/deliveries/delivery-4/Processed_Training.csv')
    calculated_features.listToCSV(mod_test_set, './data/deliveries/delivery-4/Processed_Testing.csv')



if __name__ == "__main__":
    main()
