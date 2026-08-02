class FindPercent:

    def percentage():
        lstPercentage = [98,87,95,95,93];
        i=0;
        total=0;
        for percent in lstPercentage:
            i+=1;
            print("Subject",i,"=",percent);
            total+=percent;
        print("Total:",total);
        print("Percentage: ",total/len(lstPercentage));