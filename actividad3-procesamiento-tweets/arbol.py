from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
# from IPython.display import Image
import pydotplus
from sklearn.tree import export_graphviz
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,cohen_kappa_score


def generarArbol(df):
    tfidfconverter = TfidfVectorizer(min_df=5, max_df=0.5)
    data = tfidfconverter.fit_transform(list(df['tweet'])).toarray()
    feature_names = list(tfidfconverter.get_feature_names())
    X = pd.DataFrame(np.array(data), columns=feature_names)
    print(X)
    y = df['clase']
    print(y)

    # Split dataset into training set and test set
    # random_state generador de numero aleatorios (semilla)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=1)  # 70% training and 30% test
    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(class_weight="balanced")

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    dot_data = export_graphviz(clf, out_file=None, filled=True, feature_names=feature_names, class_names=['Negativo'
        , 'Neutro', 'Positivo'])
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf('tree2.pdf')

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Kappa:", cohen_kappa_score(y_test, y_pred))


# dirname = os.path.dirname(__file__)
# filename2 = os.path.join(
#     dirname, r'resultado.txt')
# numpy.savetxt(filename2, X, fmt='%s', delimiter=",")


generarArbol(pd.read_csv(r"tweets2.csv"))
