# information-science-assigment-1

[Data link](http://archive.ics.uci.edu/ml/datasets/Australian+Sign+Language+signs)

This project shows a comparision between 3 machine learning models on a picked sample of the data above.
The project is written in Matlab and python.
The python scripts are used to collect the data into one file.

##Cleaning data
To collect the data to xlsx file run this command in the terminal:-

```python3 sign_data_converter.py  [main directory path]  [new xlsx files path]```

To collect the xlsx files to one file run this command :-

```python3 collecter.py  [xlsx files directory path]  [new xlsx file path/name]```

##Matlab scripts

app :- gets the data and modifies it to be processable

knnapp:- trains the KNN model on the dataset and gets the loss rate and the confusion matrix

treeApp:- trains the decision tree model on the dataset and gets the loss rate and the confusion matrix

nbApp:- trains the naive bayes model on the dataset and gets the loss rate and the confusion matrix



