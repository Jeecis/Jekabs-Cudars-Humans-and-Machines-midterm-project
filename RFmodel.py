from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd




class RFmodel:

    def __init__(self):
        url = "titanic/train.csv"
        self.df = pd.read_csv(url)

    def setUp(self, dataGroups):

        self.df['Cabin'] = self.df['Cabin'].str[0]
        if not "Survived" in dataGroups:
            dataGroups.append("Survived")

        cleanData = self.df[dataGroups]



        X = cleanData.drop("Survived", axis=1)
        y = cleanData["Survived"]

        numerised = pd.get_dummies(X)
        X_train, X_test, y_train, y_test = train_test_split(numerised, y, test_size=0.35, random_state=101)

        return X_train, X_test, y_train, y_test

    def accuracy(self, dataGroups):
        X_train, X_test, y_train, y_test = self.setUp(dataGroups)

        rf = RandomForestClassifier(oob_score=True)
        rf.fit(X_train, y_train)
        answers=rf.predict(X_test)
        dataKeys = y_test.keys()
        correct=0
        for i in range(len(answers)):
            if answers[i]==y_test[dataKeys[i]]:
                correct+=1
        res=correct/len(answers)

        print(f' Accuracy 1 - : {res}')
        print(f' Accuracy 2 - : {rf.score(X_test, y_test)}')

    def track(self, dataGroups):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)


        X_train, X_test, y_train, y_test = self.setUp(dataGroups)

        rf = RandomForestClassifier(oob_score=True)
        rf.fit(X_train, y_train)
        predictions=rf.predict(X_test)
        # print(y_test.keys())
        dataKeys=y_test.keys()
        print(dataKeys)
        fpositives=[]
        fnegatives=[]

        tpositives = []
        tnegatives = []


        for i in range(len(predictions)):
            if predictions[i] != y_test[dataKeys[i]] and predictions[i]==1 :
                fpositives.append(dataKeys[i])
            elif predictions[i] != y_test[dataKeys[i]] and predictions[i]==0:
                fnegatives.append(dataKeys[i])
            elif predictions[i]==1:
                tpositives.append(dataKeys[i])
            elif predictions[i]==0:
                tnegatives.append(dataKeys[i])


        print("FALSE POSITIVES:")
        print(self.df.iloc[fpositives])

        print("FALSE NEGATIVES:")
        print(self.df.iloc[fnegatives])

        print("TRUE POSITIVES:")
        print(self.df.iloc[tpositives])

        print("TRUE NEGATIVES:")
        print(self.df.iloc[tnegatives])

    def kaggle(self,dataGroups):
        url = "titanic/test.csv"
        newdf = pd.read_csv(url)
        newdf['Cabin'] = newdf['Cabin'].str[0]

        cleanData = newdf[dataGroups]
        numerised = pd.get_dummies(cleanData)

        X_train, X_test, y_train, y_test = self.setUp(dataGroups)
        X_train = X_train.drop("Cabin_T", axis=1)

        rf = RandomForestClassifier(oob_score=True)
        rf.fit(X_train, y_train)

        prediction= rf.predict(numerised)
        submission = pd.DataFrame({
            "PassengerId": newdf["PassengerId"],
            "Survived": prediction
        })
        submission.to_csv('submission.csv', index=False)

    def humanJudge(self):
        newDf=self.df.loc[(self.df['Sex'] == "female") & ((self.df["Fare"] >= 100))]

        print(newDf)

