
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
import xgboost as xgb
import operator

from sklearn.metrics import mean_squared_error
from math import sqrt


# In[3]:

def rmse(y, yhat):
    return np.sqrt(np.mean((yhat-y)**2))

def train_xgboost(train_valid, features, num_boost_round=500, test_size=0.20, 
                  eta=0.13, max_depth=10):
    params = {"objective": "reg:linear",
              "booster" : "gbtree",
              "eta": eta,
              "max_depth": max_depth,
              "subsample": 0.9,
              "colsample_bytree": 0.6,
              "silent": 1,
              "seed": 0,
              'eval_metric': 'rmse'
              }

    X_train, X_valid = train_test_split(train_valid, test_size=test_size, random_state=10)
    y_train = np.log1p(X_train.Score)
    y_valid = np.log1p(X_valid.Score)
    dtrain = xgb.DMatrix(X_train[features], y_train)
    dvalid = xgb.DMatrix(X_valid[features], y_valid)

    watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
    gbm = xgb.train(params, dtrain, num_boost_round, evals=watchlist, 
                    early_stopping_rounds=100, verbose_eval=True)

    print("Validating")
    yhat = gbm.predict(xgb.DMatrix(X_valid[features]))
    error = rmse(X_valid.Score.values, np.expm1(yhat))
    print('RMSE: {:.6f}'.format(error))
    return gbm

def xgboost_predict(model, test, features, nafill=0.0):
    _test = test.fillna(nafill)
    dtest = xgb.DMatrix(_test[features])
    predictions = model.predict(dtest)
    return np.expm1(predictions)


# In[ ]:



