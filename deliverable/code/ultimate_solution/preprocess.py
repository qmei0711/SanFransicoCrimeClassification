import csv
import json
import random
from collections import defaultdict

def get_top_categories(file_path, top):

	with open(file_path) as f:
		counts = defaultdict(int)

		reader = csv.reader(f)
		first_row = True
		
		for row in reader:
			if first_row:
				first_row = False
				idx_Category = row.index('Category')
			else:
				category = row[idx_Category]
				counts[category] += 1
		pairs = [(key, counts[key]) for key in counts]
		pairs = sorted(pairs, key=lambda x: -x[1])

		total_count = sum(list(zip(*pairs)[1]))
		if top:
			pairs = pairs[:top]
		print pairs
		top_count = sum(list(zip(*pairs)[1]))
		print 'top %d categores count: %d, all categories count: %d, rate: %f' % (top, top_count, total_count, float(top_count) / total_count)

		top_categories = list(zip(*pairs)[0])
		return top_categories


def split_training_data(file_path, out1, out2, top, threadshold):
	top_categories = get_top_categories(file_path, top)

	with open(file_path) as f, open(out1, 'wb') as o1, open(out2, 'wb') as o2:
		reader = csv.reader(f)
		writer1 = csv.writer(o1)
		writer2 = csv.writer(o2)
		first_row = True
		i = 0
		for row in reader:
			i += 1
			if first_row:
				first_row = False
				writer1.writerow(row)
				writer2.writerow(row)
				idx_Category = row.index('Category')
			else:
				if random.random() > threadshold:
					continue

				category = row[idx_Category]
				if category not in top_categories:
					continue
				if i % 2 == 0:
					writer1.writerow(row)
				else:
					writer2.writerow(row)

def export_count_info(file_path, export_file):


	top5 = get_top_categories(file_path, 5)
	top10 = get_top_categories(file_path, 10)

	years = set()
	months = set()
	districts = set()
	categories = set()
	dows = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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


	# required_cats = ['LARCENY/THEFT', 'ASSAULT', 'DRUG/NARCOTIC', 'BURGLARY', 'ROBBERY']
	required_cats = ['BURGLARY', 'ROBBERY']
	all_data = {}
	category_district_count = {}
	district_year_category_count = {}
	year_category_count = {}
	category_dow_count = {}


	for category in categories:
		category_dow_count[category] = defaultdict(int)
		category_district_count[category] = defaultdict(int)
		all_data[category] = {}
		for year in years:
			all_data[category][year] = {}
			for month in months:
				all_data[category][year][month] = {}
				for district in districts:
					all_data[category][year][month][district] = 0

	for district in districts:
		district_year_category_count[district] = {}
		for year in years:
			district_year_category_count[district][year] = defaultdict(int)

	for year in years:
		year_category_count[year] = defaultdict(int)


	district_count = defaultdict(int)

	with open(file_path) as f: 
		reader = csv.reader(f)
		first_row = True
		for row in reader:
			if first_row:
				first_row = False
				idx_PdDistrict = row.index('PdDistrict')
				idx_Category = row.index('Category')
				# 2015-05-10 23:59:00
				idx_Dates = row.index('Dates')
				idx_Dow = row.index('DayOfWeek')

			else:
				district = row[idx_PdDistrict]
				category = row[idx_Category]
				dates = row[idx_Dates]
				year = dates[:4]
				month = dates[5:7]
				dow = row[idx_Dow]

				all_data[category][year][month][district] += 1
				district_count[district] += 1
				category_district_count[category][district] += 1


				if category in required_cats:
					district_year_category_count[district][year][category] += 1
				# if category in required_cats:
				# 	year_category_count[year][category] += 1
				# if category in top10:
				# 	category_dow_count[category][dow] += 1

		maxes = {}
		mins = {}
		maxes_year = {}
		mins_year = {}
		for district in districts:
			maxes[district] = defaultdict(int)
			mins[district] = defaultdict(int)
			maxes_year[district] = defaultdict(int)
			mins_year[district] = defaultdict(int)

			for category in required_cats:
				maxes[district][category] = 0
				mins[district][category] = 999999999
				
				for year in years:
					count = district_year_category_count[district][year][category]
					if count > maxes[district][category]:
						maxes[district][category] = count
						maxes_year[district][category] = year
					if count < mins[district][category]:
						mins[district][category] = count
						mins_year[district][category] = year


		with open(export_file, 'w') as outfile:
			json.dump(district_year_category_count, outfile)


		for year in years:
			print year
			print top10
			for category in top10:
				print year_category_count[year][category],
				print ',',
			print '\n'


		for category in top10:
			print category
			for dow in dows:
				print dow,
			print '\n'
			for dow in dows:
				print category_dow_count[category][dow],
			print '\n'




def main():


	input_file = '../../data/train.csv'


	export_file = '../../data/output.json'
	export_count_info(input_file, export_file)
	# return

	num_categories = [0, 20, 10, 5, 3]
	for num_cat in num_categories:
		print num_cat
		train_file = '../../data/top' + str(num_cat) + '_1.csv'
		test_file = '../../data/top' + str(num_cat) + '_2.csv'
	
		split_training_data(input_file, train_file, test_file, num_cat, 0.1)	



main()