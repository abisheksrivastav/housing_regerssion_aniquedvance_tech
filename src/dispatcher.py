from sklearn import ensemble
from xgboost import XGBRegressor

0.75091
MODELS = {
    "xgb": XGBRegressor(colsample_bytree=0.4603, gamma=0.0468, 
                             learning_rate=0.05, max_depth=3, 
                             min_child_weight=1.7817, n_estimators=2200,
                             reg_alpha=0.4640, reg_lambda=0.8571,
                             subsample=0.5213, silent=1,
                             random_state =7, nthread = -1),
    "extratrees": ensemble.ExtraTreesClassifier(n_estimators=200, n_jobs=-1, verbose=2),
}