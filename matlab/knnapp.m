app;
getTraingingData;
% training the KNN model
knn_model = fitcknn(X,Y,'NumNeighbors',2,'Standardize',1);
% predicting a sample of tests
[knnLabel,score,cost] = predict(knn_model,Xnew);
%creating a confusion matrix
confusionmatKNN=confusionmat(knnLabel,dataLabels(trainingNumberOfRows:length(dataArray),:));
confusionchart(confusionmatKNN);
title("KNN confusion matrix");
%getting the loss rate
KnnlossRate=loss(knn_model,dataArray,dataLabels);
for i =1:size(confusionmatKNN,1)
    recall(i)=confusionmatKNN(i,i)/sum(confusionmatKNN(i,:));
end
Recall=sum(recall)/size(confusionmatKNN,1);

for i =1:size(confusionmatKNN,1)
    precision(i)=confusionmatKNN(i,i)/sum(confusionmatKNN(:,i));
end
Precision=sum(precision)/size(confusionmatKNN,1);
clear precision  recall;