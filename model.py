


import pandas as pd
import numpy as np
import re
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeClassifierCV
from sklearn.ensemble import BaggingClassifier
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import StratifiedKFold 

    
stop_words=stopwords.words('english')
    


lr=BaggingClassifier(base_estimator=LogisticRegression(C=8, class_weight=None,
                                                    dual=False,
                                                    fit_intercept=True,
                                                    intercept_scaling=1,
                                                    l1_ratio=None, max_iter=100,
                                                    multi_class='auto',
                                                    n_jobs=None, penalty='l2',
                                                    random_state=None,
                                                    solver='lbfgs', tol=0.0001,
                                                    verbose=0,
                                                    warm_start=False),
                  bootstrap=True, bootstrap_features=False, max_features=1.0,
                  max_samples=1.0, n_estimators=10, n_jobs=None,
                  oob_score=False, random_state=42, verbose=0,
                  warm_start=False)
rc=BaggingClassifier(base_estimator= RidgeClassifierCV())
def model(test_data,train_data):
   
    train_data['data'] = train_data['data'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
    #train, test = train_test_split(train_data, shuffle = True, stratify = data.label, train_size = 0.99, random_state = 50)
    train = train_data.drop(["label"] , axis=1)
    label_encoder = preprocessing.LabelEncoder()
     
    y_train = train_data.label.values
    
    y_train = label_encoder.fit_transform(y_train) 
    #y_test =  label_encoder.fit_transform(test['label'])
    # 
    tfidf = TfidfVectorizer()
    x_train = tfidf.fit_transform(train.data.values)
    # Create StratifiedKFold object. 
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42) 
    lst_accu_stratified = [] 

    for train_index, test_index in skf.split(x_train, y_train): 
        x_train_fold, x_test_fold = x_train[train_index], x_train[test_index] 
        y_train_fold, y_test_fold = y_train[train_index], y_train[test_index] 
        
        #x_test = tfidf.transform(test.data.values)
        rc.fit(x_train ,y_train )

        x_test = tfidf.transform(test_data.data.values)
        predictions_encoded = rc.predict(x_test)

        predictions = label_encoder.inverse_transform(predictions_encoded)

        final = pd.DataFrame({"Filename" : test_data.Filename.values , "Label" : predictions})
        return final













