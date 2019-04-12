% Change the value to choose the feature to represent in the plotbox
% 1-x 2-y 3-z 
% 4-roll 5-thumb 6-bending value    7-fore bending value    8-index bending value   9-ring bending value
app;
arrFeatures =["x" "y" "z" "roll" "thumb bending value" "fore bending value" "index bending value" "ring bending value"];
changingValue = 5;
thumb=boxplot(dataArray(:,changingValue),dataLabels);
title(arrFeatures(changingValue)+ " by sign");
xlabel('Sign language words')
ylabel(arrFeatures(changingValue))
