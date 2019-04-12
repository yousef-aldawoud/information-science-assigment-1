app;
getTraingingData;
% training the naive bayes model
nb_model = fitcnb(X,Y,'ClassNames',UniqueLabels);
% predicting a sample of tests
[nbLabel,score,cost] = predict(nb_model,Xnew);
%creating a confusion matrix
confusionmatNB=confusionmat(nbLabel,dataLabels(trainingNumberOfRows:length(dataArray),:));
confusionchart(confusionmatNB);
title("Naive bayes confusion matrix");
%getting the loss rate
NBlossRate=loss(nb_model,dataArray,dataLabels);
for i =1:size(confusionmatNB,1)
    recall(i)=confusionmatNB(i,i)/sum(confusionmatNB(i,:));
end
Recall=sum(recall)/size(confusionmatNB,1);

for i =1:size(confusionmatNB,1)
    precision(i)=confusionmatNB(i,i)/sum(confusionmatNB(:,i));
end
Precision=sum(precision)/size(confusionmatNB,1);
clear precision  recall;