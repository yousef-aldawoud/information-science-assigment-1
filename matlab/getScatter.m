app;
x=dataArray(:,5);
y=dataArray(:,8);
scatter(x,y);
title("thumb by index");
xlabel('Thumb')
ylabel('ring')



x=dataArray(:,4);
y=dataArray(:,7);
op=scatter(x,y,'b','*');

title("roll by ring");
xlabel('roll')
ylabel('index')


x=dataArray(:,1);
y=dataArray(:,2);
scatter(x,y);
title("X hand location by Y hand location");
xlabel('X hand location')
ylabel('Y hand location')