from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score

"""
Script to create precision and recall

- Modify 'threshold' value
"""

def analyzePRLanguage(analyzedLanguage, listOfContents):
    fn=0
    tp=0
    fp=0
    tn=0
    #added threshold value
    threshold = 0.90
    print("Threshold: %f" % (threshold))
    for content in listOfContents:
        #es. italian yes or no = ground truth
        if (content.language==analyzedLanguage):
            #see if recognized italian
            if ((content.recognized_language==analyzedLanguage) and (content.language_probability >= threshold)):
                #italian and considered italian
                tp=tp+1
            else:
                #italian and but no considered italian
                fn=fn+1
                #print("MISTAKE! Incorrect content_id: %d and text %s" % (content.content_id, (content.title+" "+content.text)))
        else:
            #if not, see if recognized italian
            if ((content.recognized_language==analyzedLanguage) and (content.language_probability >= threshold)):
                #not italian but considered italian
                fp=fp+1
                #print("MISTAKE! Incorrect content_id: %d and text %s" % (content.content_id, (content.title+" "+content.text)))
            else:
                #not italian and not considered italian
                tn=tn+1
    return [fn, tp, fp, tn]


def getPrecisionAndRecall(analyzedLanguage, listOfContents):
    print("--- Precision and recall calculation ---")
    print("--- Analysis for language %s ---" % (analyzedLanguage))
    #es. analyzedLanguage is italian
    [fn, tp, fp, tn] = analyzePRLanguage(analyzedLanguage, listOfContents)

    print("------------------------------------------------")
    print("FN: %d" % (fn)) #not considered italian but they are italian --> mistake of the system
    print("TP: %d" % (tp)) #correct
    print("FP: %d" % (fp)) #considered italian but they are foreign --> mistake of the system
    print("TN: %d" % (tn)) #correct

    print("------------------------------------------------")
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    print("Precision: {0:.2%}".format(precision))
    print("Recall: {0:.2%}".format(recall))
    print("------------------------------------------------")


"""
#define a function that accepts the data from the language tool
def drawGraph():
    #this is an example
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Add noisy features
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

    # Limit to the two first classes, and split into training and test
    X_train, X_test, y_train, y_test = train_test_split(X[y < 2], y[y < 2],
                                                        test_size=.5,
                                                        random_state=random_state)


    average_precision = average_precision_score(y_test, y_test)

    print('Average precision-recall score: {0:0.2f}'.format(
          average_precision))

    # Create a simple classifier
    classifier = svm.LinearSVC(random_state=random_state)
    classifier.fit(X_train, y_train)
    y_score = classifier.decision_function(X_test)

    disp = plot_precision_recall_curve(classifier, X_test, y_test)
    disp.ax_.set_title('2-class Precision-Recall curve: '
                       'AP={0:0.2f}'.format(average_precision))

    plt.show()
"""
