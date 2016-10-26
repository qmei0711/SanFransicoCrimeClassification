import sys
import csv
import numpy
from collections import defaultdict
from sklearn import cross_validation
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC, SVC, NuSVC
from sklearn.metrics import classification_report, confusion_matrix

labelMap = {}
fieldnames = ['Category','Time','DayOfWeek', 'PdDistrict']
def labelConversion(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        i = 1
        for row in reader:
            if row[0] not in labelMap:
                labelMap[row[0]] = i
                i += 1

def loadFile(file_path):
    labels, features = [], []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            tmp = {}
            labels.append(row['Category'])
            for i in range(1,len(fieldnames)):
                tmp[fieldnames[i]] = row[fieldnames[i]]
            features.append(tmp)
        return (labels, features)

def writeFile(file_path, label1, label2, feature):
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        for i in range(len(label1)):
            writer.writerow([label1[i]]+[label2[i]]+list(feature[i].values()))

def main():
    # labelConversion('refinedTrain.csv')
    # print labelMap
    trainingLabels, trainingData = loadFile('../../data/refinedTrain.csv')
    vectorizer = DictVectorizer()
    trainingFeatures = vectorizer.fit_transform(trainingData)
    trainingLabels = numpy.array(trainingLabels)

    classifier = LinearSVC()
    classifier.fit(trainingFeatures, trainingLabels)
    trainingScore = classifier.score(trainingFeatures, trainingLabels)
    print trainingScore
    cvScore = cross_validation.cross_val_score(classifier, trainingFeatures, trainingLabels, cv=5)
    print cvScore
    predictLabels = classifier.predict(trainingFeatures)
    print classification_report(trainingLabels, predictLabels)
    print confusion_matrix(trainingLabels, predictLabels)


    

if __name__ == '__main__':
    main()