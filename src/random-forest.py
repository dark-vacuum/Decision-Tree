import file_manager
import data_cleaner as dc
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score


def random_forest(x_train, y_train):
    # Creacion del Arbol de desicion CART
    dtc = RandomForestClassifier(n_estimators=50)

    # Entrenamiento
    dtc.fit(x_train, y_train)

    return dtc


def prediction(x_test, tree_forest):

    prediction = tree_forest.predict(x_test)

    print("Predicted values:")
    print(prediction, end = "\n"*2)

    return prediction


def cal_accuracy(x_train, y_train, tree_forest):
    # Accuracy
    accuracy = round(tree_forest.score(x_train, y_train) * 100, 2)
    print("Accuracy:", round(accuracy, 2, ), "%", end = "\n"*2)

    # Validacion Cruzada
    cross_predictions = cross_val_predict(tree_forest, x_train, y_train, cv=3)
    print("Confusion Matrix:\n", confusion_matrix(y_train, cross_predictions), end = "\n"*2)

    # Precision and Recall
    print("Precision:", precision_score(y_train, cross_predictions))
    print("Recall:",recall_score(y_train, cross_predictions), end = "\n"*2)


def main():
    dataset_file = "./../data/titanic-dataset.csv"
    file_output = "./../data/random_forest.csv"

    titanic_data = file_manager.readData(dataset_file)
    titanic_data = dc.dataCleaner(titanic_data)
    
    data_test, x_train, x_test, y_train = dc.splitData(titanic_data)

    rfc = random_forest(x_train, y_train)

    rfc_predictions = prediction(x_test, rfc) 
    cal_accuracy(x_train, y_train, rfc) 
    file_manager.writeData(file_output, data_test["PassengerId"], rfc_predictions)


if __name__ == '__main__':
    main()