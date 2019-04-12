% this script trims the dataset to two parts
% training data set and testing data set

%creates random indexes for the picked data set
randomIndexes=randperm(length(dataLabels));

%picks a percentage of dataset
trainingNumberOfRows = round(0.8*length(dataArray));
dataArray=dataArray(randomIndexes,:);
dataLabels=dataLabels(randomIndexes);

% x is the training parameters
X=dataArray(1:trainingNumberOfRows,:);

% y is the training labels
Y=dataLabels(1:trainingNumberOfRows);

% Xnew is the the parameters for the other percentage of the dataset
Xnew=dataArray(trainingNumberOfRows:length(dataArray),:);