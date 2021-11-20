import pandas as pd
from numpy import ravel

# Libraries used to clean tweets, saw an example for this on the following link:
# https://stackoverflow.com/questions/64719706/cleaning-twitter-data-pandas-python
import re, emoji

from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import ExtraTreesRegressor

trainingDF = pd.read_csv('./data/TrainingDS.csv')
testingDF = pd.read_csv('./data/TestingDS.csv')

vectorizer = CountVectorizer()
transformer = TfidfTransformer(use_idf=False)
classifier = ExtraTreesRegressor(n_estimators=265)

def pandasToKaggle(path, df):
    df.to_csv(path, index=True, index_label=['ID'], header=["Class"])

def cleaner(df):
    arr = []
    for instance in df["Text"]:
        instance = " ".join(instance.split())

        # Deletes emojis, links and continuity expressions (e.g. '(1/3)')
        instance = re.sub(r"\([0-9]+/[0-9]+\)", "", instance)
        instance = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", instance)
        instance = ''.join(c for c in instance if c not in emoji.EMOJI_UNICODE_ENGLISH)

        # Deletes numbers
        instance = re.sub(r"[0-9]", "", instance)

        # Deletes different signs or punctiuations and keeps the text
        instance = instance.replace("#", "").replace("_", " ")
        instance = instance.replace("@", "").replace("_", " ")
        arr.append(instance)
    return pd.DataFrame(arr)

def main():
    trainingClean = cleaner(trainingDF)
    trainingDF["Text"] = trainingClean
    trainingText = trainingDF["Text"].tolist()
    trainingClasses = ravel(trainingDF["Class"].to_numpy())

    testingClean = cleaner(testingDF)
    testingDF["Text"] = testingClean
    testingText = testingDF["Text"].tolist()
    
    trainingBoW = vectorizer.fit_transform(trainingText)
    trainingTf = transformer.fit_transform(trainingBoW)

    testingBoW = vectorizer.transform(testingText)
    testingTf = transformer.transform(testingBoW)

    modeling = classifier.fit(trainingTf, trainingClasses)
    testingClasses = pd.DataFrame(modeling.predict(testingTf))
    testingClasses.index += 1
    pandasToKaggle("./data/final-submission.csv", testingClasses)

    

if __name__=="__main__":
    main()

