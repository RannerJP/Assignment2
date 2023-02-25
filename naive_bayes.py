#-------------------------------------------------------------------------
# AUTHOR: Jose Pavon
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 Hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
db = []
X = []
Y = []
#reading the training data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
for row in db:
  placeholder = []
  for count,item in enumerate(row):
      if 0<count<5:
        if item == "Sunny" or item == "Hot" or item == "Normal" or item == "Strong":
          placeholder.append(1)
        elif item == "Overcast" or item == "Cold" or item == "High" or item == "Weak":
          placeholder.append(2)
        else:
          placeholder.append(3)
  X.append(placeholder)


#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
for row in db:
        if row[5] == "Yes":
            Y.append(1)
        else:
            Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

test = []
#reading the test data in a csv file
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
      if i > 0: #skipping the header
         test.append(row)
print(f"{test[0][0]}   {test[0][1]}   {test[0][2]}   {test[0][3]}   {test[0][4]}   PlayTennis   Confidence")
for count, row in enumerate(test):
    placeholder = []
    testVals = []
    for index,item in enumerate(row):
      if 0<index<5:
        if item == "Sunny" or item == "Hot" or item == "Normal" or item == "Strong":
          placeholder.append(1)
        elif item == "Overcast" or item == "Cold" or item == "High" or item == "Weak":
          placeholder.append(2)
        else:
          placeholder.append(3)
    testVals.append(placeholder)
  
    score = clf.predict_proba(testVals)[0]
    if max(score) > .75:
        class_predicted = clf.predict(testVals)[0]
        if class_predicted == 1:
            class_predicted = "Yes"
        else:
            class_predicted = "No"
        print(f"{test[count][1]}   {test[count][2]}   {test[count][3]}   {test[count][4]}   {class_predicted}   {max(score)}")
    

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here


