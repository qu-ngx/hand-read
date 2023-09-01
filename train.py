import pickle
import sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Open saved dataset created from dataset
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Convert data and labels to array
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split the data into test set and train set
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Used an pre-trained ANN called RandomForestClassifier for hyperparameters
model = RandomForestClassifier()

# Fitting the model to reduce loss
model.fit(x_train, y_train)

# Making predicitons based on x_test
y_predict = model.predict(x_test)

# Testing out the accuracy of the model
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

# Store model to the file using dump
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
