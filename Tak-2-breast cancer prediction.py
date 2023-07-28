import numpy as np
import pandas as pd
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

"""Data Collection & Processing"""

# loading the data from sklearn
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()

# loading the data to a data frame
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)

# adding the 'target' column to the data frame
data_frame['label'] = breast_cancer_dataset.target

# number of rows and columns in the dataset
data_frame.shape

# getting some information about the data
data_frame.info()

# checking for missing values
data_frame.isnull().sum()

# statistical measures about the data
data_frame.describe()

# checking the distribution of Target Variable
data_frame['label'].value_counts()

"""1 --> Benign
0 --> Malignant
"""

data_frame.groupby('label').mean()

"""Separating the features and target"""

X = data_frame.drop(columns='label', axis=1)
Y = data_frame['label']

"""Splitting the data into training data & Testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

"""Model Training - Logistic Regression"""

# Set solver and max_iter to address the convergence warning
model = LogisticRegression(solver='liblinear', max_iter=1000)

# training the Logistic Regression model using Training data
model.fit(X_train, Y_train)

"""Model Evaluation - Accuracy Score"""

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy on training data = ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy on test data = ', test_data_accuracy)

"""Building a Predictive System"""

# Input data point for prediction
input_data = (13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259)

# Convert the input data to a numpy array and reshape
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Perform feature scaling on the input data
scaler = StandardScaler()
input_data_scaled = scaler.fit_transform(input_data_reshaped)

# Make prediction using the trained model
prediction = model.predict(input_data_scaled)
print(prediction)

if prediction[0] == 0:
    print('The Breast cancer is Malignant')
else:
    print('The Breast Cancer is Benign')
