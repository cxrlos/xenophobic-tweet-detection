import pandas as pd

# Libraries used to clean tweets, saw an example for this on the following link:
# https://stackoverflow.com/questions/64719706/cleaning-twitter-data-pandas-python
import re, emoji

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

trainingDS = pd.read_csv('./data/TrainingDS.csv')
testingDS = pd.read_csv('./data/TestingDS.csv')

# Copied from the previous delivery
def pandasToKaggle(path, df):
    df.to_csv(path, index=True, index_label=['ID'], header=["Class"])

# Deleted some data that might generate noise in the classification and bagging
# process
def cleaner(df):
    arr = []
    for instance in df["Text"]:
        instance = " ".join(instance.split())

        # Deletes emojis, links and continuity expressions (e.g. '(1/3)')
        instance = re.sub(r"\([0-9]+/[0-9]+\)", "", instance)
        instance = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", instance)
        instance = ''.join(c for c in instance if c not in emoji.EMOJI_UNICODE_ENGLISH)

        # Deletes # and @ signs but keeps the text
        instance = instance.replace("#", "").replace("_", " ")
        instance = instance.replace("@", "").replace("_", " ")

        arr.append(instance)
    return pd.DataFrame(arr)

def main():
    traindf = cleaner(trainingDS)
    trainingDS["Text"] = traindf

    testdf = cleaner(testingDS)
    testingDS["Text"] = testdf 
    
    # BoW
    vectorizer = CountVectorizer()
    vectorizer.fit(trainingDS["Text"])
    training_bow_array = vectorizer.transform(trainingDS["Text"]).toarray()
    testing_bow_array = vectorizer.transform(testingDS["Text"]).toarray()

    # SVM that was suggested today in class
    svmClassifier = SVC(decision_function_shape='ovo')
    svmClassifier.fit(training_bow_array, trainingDS['Class'])
    svmDF = pd.DataFrame(svmClassifier.predict(testing_bow_array))
    svmDF.index += 1
    pandasToKaggle("./data/svm-submission.csv", svmDF)

    # Random forest that was my best classifier in Weka
    randomforestClassifier = RandomForestClassifier(n_estimators=100)
    randomforestClassifier.fit(training_bow_array, trainingDS['Class'])
    randomforestDF = pd.DataFrame(randomforestClassifier.predict(testing_bow_array))
    randomforestDF.index += 1
    pandasToKaggle("./data/randomforest-submission.csv", randomforestDF)

    # I wanted to try a recommended classifier called SGD
    sgdClassifier = SGDClassifier()
    sgdClassifier.fit(training_bow_array, trainingDS['Class'])
    sgdDF = pd.DataFrame(sgdClassifier.predict(testing_bow_array))
    sgdDF.index += 1
    pandasToKaggle("./data/sgd-submission.csv", sgdDF)

if __name__ == "__main__":
    main()
