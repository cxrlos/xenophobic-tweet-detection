import pandas as pd
from numpy import ravel 
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier

def csvToPandas(path, columns):
    df = pd.read_csv(path, usecols = columns)
    return df

def pandasToKaggle(path, df):
    df.to_csv(path, index=True, index_label=['ID'], header=["Class"])

def main():
    attributes = [
            "sentiment/negative", 
            "sentiment/positive",
            "emotion/Bored",
            "emotion/Angry",
            "emotion/Sad",
            "emotion/Fear",
            "emotion/Excited",
            "emotion/Happy",
            "intent/spam",
            "intent/feedback/tag/complaint",
            "exclamation_counter", 
            "caps_counter"]

    classes = ["Class"]

    # Read data from CSVs into pandas dataframe
    trainingDF = csvToPandas("./data/TrainingDS.csv", attributes)
    trainingClassesDF = ravel(csvToPandas("./data/TrainingDS.csv", classes))
    testingDF = csvToPandas("./data/TestingDS.csv", attributes)
    
    # Ada classifier
    ada = AdaBoostClassifier(n_estimators = 45, learning_rate=1.1)
    ada.fit(trainingDF, trainingClassesDF)
    adaDF = pd.DataFrame(ada.predict(testingDF))
    adaDF.index += 1
    pandasToKaggle("./data/Ada_Kaggle.csv", adaDF)

    # Bagging classifier
    bagging = BaggingClassifier(n_estimators = 10)
    bagging.fit(trainingDF, trainingClassesDF)
    baggingDF = pd.DataFrame(bagging.predict(testingDF))
    baggingDF.index += 1
    pandasToKaggle("./data/Bagging_Kaggle.csv", baggingDF)

if __name__=="__main__":
    main()
