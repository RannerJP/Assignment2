#-------------------------------------------------------------------------
# AUTHOR: Jose Pavon
# FILENAME: decision_tree_2.py
# SPECIFICATION: This program trains on 3 different training sets and outputs the accuracy
# FOR: CS 4210- Assignment #2
# TIME SPENT: about an hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
import random
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for header,row in enumerate(dbTraining):
        placeholder = []
        for count,item in enumerate(row):
            if count<4:
                if item == "Young" or item == "Myope" or item == "No" or item == "Reduced":
                    placeholder.append(1)
                elif item == "Presbyopic" or item == "Hypermetrope" or item == "Yes" or item == "Normal":
                    placeholder.append(2)
                elif item == "Prepresbyopic":
                    placeholder.append(3)
        X.append(placeholder)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for row in dbTraining:
        if row[4] == "Yes":
            Y.append(1)
        else:
            Y.append(2)

    #loop your training and test tasks 10 times here
    averageAll = []
    for i in range (10):
        sum = 0
        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3, random_state=random.randint(1,1000))
        clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for i, row in enumerate(reader):
                    if i > 0: #skipping the header
                        dbTest.append (row)

        testClass =[]
        for row in dbTest:
            if row[4] == "Yes":
                testClass.append(1)
            else:
                testClass.append(2)
        #transform the features of the test instances to numbers following the same strategy done during training,
        #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label

        #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        for sample,data in enumerate(dbTest):
            placeholder = []
            for count,item in enumerate(data):
                if count<4:
                    if item == "Young" or item == "Myope" or item == "No" or item == "Reduced":
                        placeholder.append(1)
                    elif item == "Presbyopic" or item == "Hypermetrope" or item == "Yes" or item == "Normal":
                        placeholder.append(2)
                    elif item == "Prepresbyopic":
                        placeholder.append(3)
            class_predicted = clf.predict([placeholder])[0]
            if class_predicted == testClass[sample]:
                sum += 1
        averageAll.append(sum/len(dbTest))
    
    finalAverage =0 
    for value in averageAll:
        finalAverage += value
    finalAverage = finalAverage/10
    print(f"Final Accuracy when traing on {ds}: {finalAverage}")
        #print the average accuracy of this model during the 10 runs (training and test set).
        #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
        #--> add your Python code here
