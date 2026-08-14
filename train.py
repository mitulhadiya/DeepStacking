from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from deepstacking import layer , sequential

data = load_digits()
X = data.data
y = data.target

x_train , x_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

deepstacking = sequential()
l1 = layer([RandomForestClassifier(),RandomForestClassifier(),RandomForestClassifier()])
deepstacking.add(l1) 

l2 = layer([RandomForestClassifier(),RandomForestClassifier()])
deepstacking.add(l2) 

l3 = layer([RandomForestClassifier()])
deepstacking.add(l3) 

deepstacking.fit(x_train,y_train,10)

y_pred = deepstacking.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
print("Deepstacking Accuricy : ",accuracy)