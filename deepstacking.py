import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
from sklearn.base import clone

class layer:
    def __init__(self,models):
        self.models = models
        
    def tmodel(self):
        return len(self.models)

    def get_prediction(self,model,X):
        if hasattr(model,"predict_proba"):
            try:
                return model.predict_proba(X)
            except(AttributeError,NotImplementedError):
                pass
        pred = model.predict(X)
        return pred.reshape(-1,1)
    
    def generate_oof(self,X,y,fold):
        res = []
        kf = StratifiedKFold(n_splits=fold,shuffle=True,random_state=42) 
        for model in self.models:
            pred = None
            for train_idx , test_idx in kf.split(X,y):
                temp = clone(model)
                temp.fit(X[train_idx],y[train_idx])
                pred1 = self.get_prediction(temp,X[test_idx])
                if pred is None:
                    pred = np.zeros((len(X),pred1.shape[1]))
                pred[test_idx] = pred1
            res.append(pred)
        return np.hstack(res)
                            
    def fit(self,X,y):
        for model in self.models:
            model.fit(X,y)

    def predict_proba(self,X):
        res = []
        for model in self.models:
            pred = self.get_prediction(model,X)
            res.append(pred)
        return np.hstack(res)
    
    def predict(self,X):
        res = []
        for model in self.models:
            res.append(model.predict(X)) 
        return np.array(res).T

class sequential :
    def __init__(self):
        self.tlayer = 0 
        self.layers = []
        
    def add(self,layer):
        self.layers.append(layer)
        self.tlayer += 1
        
    def fit(self,X,y,fold = 5):
        res = X
        res2 = []
        for layer in self.layers:
            res2 = layer.generate_oof(res,y,fold)
            layer.fit(res,y)
            res = np.hstack((X,res2))
    
    def predict(self,X):
        res = X
        for layer in self.layers[:-1]:
            res = layer.predict_proba(res)
            res = np.hstack((X,res))
        res = self.layers[-1].predict(res)
        return res