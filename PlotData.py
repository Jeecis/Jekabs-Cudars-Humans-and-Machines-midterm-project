import pandas as pd
import matplotlib.pyplot as plt
import os

class PlotData:
    def __init__(self, dataGroups):
        url = "titanic/train.csv"
        self.df = pd.read_csv(url)
        self.dataGroups=dataGroups

    def plot(self):

        self.cleanData(self.df)
        for checkCol in  self.dataGroups:
            self.outputFig(checkCol)


    ## takes in data groups and fills empty fields with -1 if int64 or float64 type field and "unknown" if object type field
    def cleanData(self, data):
        self.df = data.copy()

        for group in  self.dataGroups:

            if self.df[group].dtype == "float64":
                self.df.fillna({group: -1}, inplace=True)
                # df[group].method(-1)
            elif self.df[group].dtype == "int64":
                self.df.fillna({group: -1}, inplace=True)
            elif self.df[group].dtype == "object":
                self.df.fillna({group: "unknown"}, inplace=True)



    def plotGrouped(self):
        self.df['Cabin'] = self.df['Cabin'].str[0]

        self.cleanData(self.df)

        max_age = self.df['Age'].max()
        max_fare = self.df['Fare'].max()

        age_bins_count = int(max_age / 20) + 2
        fare_bins_count = int(max_fare / 50) + 2

        age_bins = []
        fare_bins = []

        for i in range(-1, age_bins_count):
            age_bins.append(i * 20)

        for i in range(-1, fare_bins_count):
            fare_bins.append(i * 50)

        age_labels = []
        for i in range(-20, int(max_age) + 1, 20): #  -20 to 0 means unknown or empty field
            age_labels.append(f'{i}-{i + 20}')

        fare_labels = []
        for i in range(-50, int(max_fare) + 1, 50): #  -50 to 0 means unknown or empty field
            fare_labels.append(f'{i}-{i + 50}')

        self.df['Age'] = pd.cut(self.df['Age'], bins=age_bins, right=False, labels=age_labels)
        self.df['Fare'] = pd.cut(self.df['Fare'], bins=fare_bins, right=False, labels=fare_labels)

        for checkCol in  self.dataGroups:
            self.outputFig(checkCol)


    def outputFig(self, checkCol):
        survived_count = self.df.groupby([f'{checkCol}', 'Survived'], observed=True).size().unstack(fill_value=0)

        survived_count['Ratio'] = survived_count[1] / (survived_count[0] + survived_count[1])
        survived_count['Ratio'] = survived_count['Ratio'].round(2) * 100

        totalP = 0
        for num in survived_count[0]:
            totalP += num

        for num in survived_count[1]:
            totalP += num
        print("Total amount " + str(totalP))

        ax = survived_count.plot(kind='bar', y=['Ratio'], color='green', width=0.8)

        for i in ax.patches:
            ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 1, f'{i.get_height():.1f}%', ha='center',
                    va='bottom')

        plt.xlabel(f'{checkCol}')
        plt.ylabel('Count')
        plt.title(f'Survival Count by {checkCol}')
        plt.xticks(rotation=0)
        plt.legend(['Survived'], loc='upper right')
        plt.tight_layout()
        ax.set_ylim(0, 110)

        folder = 'photos'
        if not os.path.exists(folder):
            os.makedirs(folder)

        output_path = os.path.join(folder, f'{checkCol}.png')
        plt.savefig(output_path)
