import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree

# load iris data
iris_data = datasets.load_iris()
x = iris_data.data
y = iris_data.target

# label for iris dataset
labels = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25)
classifier = tree.DecisionTreeClassifier()
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)

# export the model
model_name = 'model.pkl'
print(f"finished training and dump the model as {model_name}")
pickle.dump(classifier, open(model_name, 'wb'))
