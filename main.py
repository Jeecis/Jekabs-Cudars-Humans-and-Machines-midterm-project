from PlotData import PlotData
from RFmodel import RFmodel

dataGrouped=["Embarked",'Cabin',"Fare","Age","Sex","Pclass","SibSp", "Parch"]

dg0=["Embarked",'Cabin',"Fare","Age","Sex","Pclass","SibSp", "Parch", "Ticket", "Name"]
dg1=["Embarked"]
dg2=["Cabin"]
dg3=["Fare"]
dg4=["Age"]
dg5=["Sex"]
dg6=["Pclass"]
dg7=["SibSp"]
dg8=["Parch"]
dg25=["Ticket"]
dg26=["Name"]

dg9=["Sex", "Fare","Pclass"]
dg10=["SibSp", "Parch","Cabin"]
dg11=["Embarked", "Age","Parch"]
dg12=["Sex", "Fare","SibSp"]
dg13=["Pclass", "SibSp","Cabin"]

dg14=["Sex", "Fare","Pclass", "SibSp"]
dg15=["SibSp", "Parch","Cabin", "Fare"]
dg16=["Embarked", "Age","Parch","Cabin"]
dg17=["Sex", "Fare","SibSp","Cabin"]
dg18=["Pclass", "SibSp","Cabin","Sex"]

dg19=["Sex", "Fare","Pclass", "SibSp", "Cabin"]
dg20=["SibSp", "Parch","Cabin", "Fare","Sex"]
dg21=["Embarked", "Age","Ticket","Cabin", "Sex"]

dg22=["Sex", "Fare","Pclass", "SibSp", "Cabin", "Embarked"]
dg23=["Sex", "Fare","Pclass", "SibSp", "Cabin", "Parch"]

dg24=["Sex", "Fare","Pclass", "SibSp", "Cabin", "Embarked", "Parch"]

dg27=["Sex", "Fare","Pclass", "SibSp", "Cabin", "Ticket"]

dg28=["Ticket", "Pclass", "Sex", "Cabin", "Parch", "SibSp", "Fare"]



dgs=[dg0,dg1,dg2,dg3,dg4,dg5,dg6,dg7,dg8,dg9,dg10,dg11,dg12,dg13,
     dg14,dg15,dg16,dg17,dg18, dg19, dg20, dg21, dg22, dg23, dg24,
     dg25, dg26,dg27,dg28]
testarr=["ugaBuga"]



def main(name):
    plot=PlotData(dataGrouped)
    plot.plotGrouped()


    rf=RFmodel()
    rf.humanJudge()
    rf.kaggle(dg19)
    rf.accuracy(dg0)
    rf.track(dg0)

    i=0
    for array in dgs:
        print(f"{i}. {array}  ", end="")
        rf.accuracy(array)
        print("============================")
        i+=1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
