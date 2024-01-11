#!/usr/bin/env python
# coding: utf-8

from wrappers import *

from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import Ridge
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

from xgboost import XGBClassifier

methods_dict = {
    "ridge": Ridge,
    "pf": PolynomialFeatures,
    "scaler": StandardScaler,
    "PLS": PLSRegressionWrapper,
    "MLPClass": MLPClass,
    "GNB": GaussianNB,
    "SVC": SVC,
    "PCA": PCA,
    "MLP": MLPClassifier,
    "XGB": XGBClassifier,
}
