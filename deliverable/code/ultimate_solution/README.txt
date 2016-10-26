Note: 
1. Download “train.csv” from the link in “data.txt”
1. put the data under data/ directory
2. run all commands under code/ultimate_solution/ directory


step 1: 

preprocess the data, and generate the training/testing input files
run: python preprocess.py, it will run the script and generate a list of files
top0_1.csv (training file, all 39 categories)
top0_2.csv (testing file, all 39 categories)
top3_1.csv (training file, top 3 categories)
top3_2.csv (testing file, top 3 categories)
top5_1.csv (training file, top 5 categories)
top5_2.csv (testing file, top 5 categories)
top10_1.csv (training file, top 10 categories)
top10_2.csv (testing file, top 10 categories)
top20_1.csv (training file, top 20 categories)
top20_2.csv (testing file, top 20 categories)

Note: We run the full dataset and it takes hours in step 2. So to make it faster (for grading purpose), I modified to code to use only 10% of the dataset. 


Step 2: 
machine learning
run: python ml.py, the output is print out on screen

