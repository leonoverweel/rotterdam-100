for i = 1:length(X)
   x(i) = str2num(cell2mat(X(i))); 
   y(i) = str2num(cell2mat(Y(i))); 
end

for i=1:26
    for j=1:26
        if ~isnan(alldata(i,j))
        if alldata(i,j)<=quantile(unique(reshape(alldata,1,[])),0.3);
            scatter(y(j),x(i),'green');
            scatter(y(j),x(i),'*','green');
            hold on
        elseif alldata(i,j)>quantile(unique(reshape(alldata,1,[])),0.3)&alldata(i,j)<=quantile(unique(reshape(alldata,1,[])),0.6)
            scatter(y(j),x(i),'yellow');
            scatter(y(j),x(i),'*','yellow');
            hold on
        else
             scatter(y(j),x(i),'red');
             scatter(y(j),x(i),'*','red');
             hold on
        end
        end
    end
end
hold off