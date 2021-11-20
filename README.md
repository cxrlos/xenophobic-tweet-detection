# Xenophobic Tweet Detection
## Carlos Garcia Gonzalez

### Abstract
Since the beginnings of the Internet, we have been able to communicate in a way that we had never seen before. National borders seemed to disappear in this new world and the limits of human interaction have been changed in a radical fashion for the last few years with the introduction of social media.

Although they brought multiple benefits, they also carried along with some issues thanks to the anonymity that the environment can bring. One of the biggest issues is Xenophobia.

*"Xenophobia, that elegant-sounding name for an aversion to persons unfamiliar, ultimately derives from two Greek terms: xenos, which can be translated as either "stranger" or "guest," and phobos, which means either "fear" or "light."* (Websters Dictionary, 2021).

### Introduction
To help detect this type of posting/data, many solutions have been created. The most popular by far are predictive models that are based on Neural Networks or simpler statistical methods. The objective of this project is to develop a predictive model that is able to accurately detect if a "tweet" contains Xenophobic claims.

### Proposal
Using the default nltk bagging method called CountVectorizer and a regression classifier called ExtraTreesRegressor the program, should be able to generate an accurate model to discern between the xenophobic and non-xenophobic tweets.

### Experimental results 
Predicting the classes for the testing data and evaluating the results with an Area Under the Curve calculation I was able to achieve 94.378% accuracy and claiming the third place on a Kaggle competition.
