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
