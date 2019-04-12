% fitctree
app;
getTraingingData;
% training the tree model
tree_model = fitctree(X,Y);
% predicting a sample of tests
[treeLabel,score,cost] = predict(tree_model,Xnew);
%creating a confusion matrix
confusionmatTREE=confusionmat(treeLabel,dataLabels(trainingNumberOfRows:length(dataArray),:));
confusionchart(confusionmatTREE);
title("Tree confusion matrix");

%getting the loss rate
TreelossRate=loss(tree_model,dataArray,dataLabels);
%viewing the tree model graph
view(tree_model,'mode','graph')
for i =1:size(confusionmatTREE,1)
    recall(i)=confusionmatTREE(i,i)/sum(confusionmatTREE(i,:));
end
Recall=sum(recall)/size(confusionmatTREE,1);

for i =1:size(confusionmatTREE,1)
    precision(i)=confusionmatTREE(i,i)/sum(confusionmatTREE(:,i));
end
Precision=sum(precision)/size(confusionmatTREE,1);
clear precision  recall;