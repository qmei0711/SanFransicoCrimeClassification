from __future__ import division
import sys
import csv
import argparse
from collections import defaultdict
import numpy as np
from scipy import stats

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import cross_validation
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from random import shuffle
from sklearn import preprocessing as pp
from sklearn.multiclass import OneVsRestClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.cluster import KMeans

from sklearn import svm, datasets
from sklearn import cross_validation


def get_vectors(file_path):

	years = set()
	months = set()
	days = set()
	districts = set()
	categories = set()
	with open(file_path) as f: 
		reader = csv.reader(f)
		first_row = True
		for row in reader:
			if first_row:
				first_row = False
				idx_PdDistrict = row.index('PdDistrict')
				idx_Category = row.index('Category')
				idx_Dates = row.index('Dates')
			else:
				district = row[idx_PdDistrict]
				category = row[idx_Category]
				dates = row[idx_Dates]
				year = dates[:4]
				month = dates[5:7]
				districts.add(district)
				categories.add(category)
				years.add(year)
				months.add(month)

	years = sorted(list(years))
	months = sorted(list(months))
	districts = sorted(list(districts))
	categories = sorted(list(categories))



def load_file(file_path):


	features = []
	labels = []


	with open(file_path) as f: 
		reader = csv.reader(f)
		first_row = True

		X = []
		y = []

		for row in reader:
			if first_row:
				first_row = False
			else:
				# 0		1		 2		  3			4		   5		  6		  7 8
				# Dates,Category,Descript,DayOfWeek,PdDistrict,Resolution,Address,X,Y

				x = [row[0]] + row[3:]
				X.append(x)
				y.append(row[1])


		return X, y


def parse_date(date):
	# year month day hour
	return int(date[:4]), int(date[5:7]), int(date[8:10]), int(date[11:13])


def select_features(X):
	new_X = []
	# 0		1		 2		     3		    4       5 6
	# Dates,DayOfWeek,PdDistrict,Resolution,Address,X,Y

	for x in X:
		date = parse_date(x[0])
		year = date[0]
		month = date[1]
		day = date[2]
		hour = date[3]

		# x2 = [year, x[2]]

		x2 = [year, month, day, hour] + x[1:3]
		new_X.append(x2)

	return new_X

def plot_2D(data, target, target_names):
    colors = cycle('rgbcmykw')
    target_ids = range(len(target_names))
    pl.figure(figsize=(9,9))
    for i, c, label in zip(target_ids, colors, target_names):
        pl.plot(data[target == i, 0],
                data[target == i, 1], '.',
                c=c, label=label)
    pl.legend(target_names)
    pl.show()




def main():
	parser = argparse.ArgumentParser()
	num_categories = [0, 20, 10, 5, 3]
	for num_cat in num_categories:
		if num_cat: 
			print '----- top ' + str(num_cat) + ' categories -----'
		else:
			print '----- all categories -----'

		train_path = '../../data/top' + str(num_cat) + '_1.csv'
		test_path = '../../data/top' + str(num_cat) + '_2.csv'


		X_train, y_train = load_file(train_path)
		X_train = select_features(X_train)
		X_train = np.array(X_train)
		y_train = np.array(y_train)

		les = []
		for feat in xrange(len(X_train[0])):
			column = X_train[:,feat]
			le = pp.LabelEncoder()
			les.append(le)
			le.fit(column)
			X_train[:,feat] = le.transform(column)




		le = pp.LabelEncoder()
		le.fit(y_train)
		y_train = le.transform(y_train)



		X_test, y_test = load_file(test_path)
		X_test = select_features(X_test)
		X_test = np.array(X_test)
		y_test = np.array(y_test)

		for feat in xrange(len(X_train[0])):
			column = X_test[:,feat]
			X_test[:,feat] = les[feat].transform(column)
		y_test = le.transform(y_test)



		# enc = pp.OneHotEncoder()
		# enc.fit(X_train)
		# enc.fit(X_train)
		# X_train = enc.transform(X_train).toarray()
		# X_test = enc.transform(X_test).toarray()

		X_train = np.array(X_train, dtype=float)
		y_train = np.array(y_train, dtype=float)
		X_test = np.array(X_test, dtype=float)
		y_test = np.array(y_test, dtype=float)
		print y_train
		print y_test

		# UNCOMMENT THIS TO DO BINARY CLASSIFICATION
		## binary classification
		# y_train = y_train == np.array(le.transform(np.array(['LARCENY/THEFT'] * len(y_train))), dtype=float)
		# y_test = y_test == np.array(le.transform(np.array(['LARCENY/THEFT'] * len(y_test))), dtype=float)

		print y_train
		print y_test
		print 'done reading files'

		print '##### bagging #####'


		bags = [LinearSVC(random_state=0), LogisticRegression(), BernoulliNB()]
		y_predicts = []
		for bag in bags:
			# NOTE: 3 classifiers: Linear SVM classifier, Logistic Regression, Naive Bayes
			print bag
			ovr = OneVsRestClassifier(bag)
			ovr.fit(X_train, y_train)

			ovr_train_score = ovr.score(X_train, y_train)
			# ovr_cross_score = cross_validation.cross_val_score(ovr, X_train, y_train, cv=10, scoring="accuracy")
			ovr_test_score = ovr.score(X_test, y_test)
			ovr_y_predict = ovr.predict(X_test)
			y_predicts.append(ovr_y_predict)
			# print 'confusion'
			# print confusion_matrix(y_test, ovr_y_predict)

			print 'ovr train score %f and test score: %f' % (ovr_train_score, ovr_test_score)
			print 'weight vector (coef) is ',
			print ovr.coef_

		
		y_predicts = np.array(y_predicts)
		y_voted = stats.mode(y_predicts)[0]
		y_test = np.array(y_test)
		bagging_accuracy = np.sum(y_voted == y_test) / float(len(y_test))
		print 'bagging accuracy: %f' % bagging_accuracy
		# print 'confusion'
		# print confusion_matrix(y_test, y_voted)


		print '##### AdaBoost #####'
		ab = AdaBoostClassifier(n_estimators=5)
		print ab
		ab = ab.fit(X_train, y_train)
		ab_train_score = ab.score(X_train, y_train)
		ab_test_score = ab.score(X_test, y_test)
		print 'AdaBoost train score: %f and test score: %f' % (ab_train_score, ab_test_score)
		# print 'confusion'
		# print confusion_matrix(y_test, y_predicts)
			
		print '##### Random Forest #####'
		rf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
		print rf
		rf = rf.fit(X_train, y_train)
		rf_train_score = rf.score(X_train, y_train)
		rf_test_score = rf.score(X_test, y_test)
		print 'random forest train score: %f and test score: %f' % (rf_train_score, rf_test_score)
		# print 'confusion'
		# print confusion_matrix(y_test, y_predicts)


	
		print '##### gradient boosting trees #####'
		gb = GradientBoostingClassifier(n_estimators=25, learning_rate=0.3, max_depth=3, random_state=0).fit(X_train, y_train)
		print gb
		gb_train_score = gb.score(X_train, y_train)
		gb_test_score = gb.score(X_test, y_test)
		print 'Gradient boosting trees train score: %f and test score: %f' % (gb_train_score, gb_test_score)
		# print 'confusion'
		# print confusion_matrix(y_test, y_predicts)




if __name__ == '__main__':
	main()
