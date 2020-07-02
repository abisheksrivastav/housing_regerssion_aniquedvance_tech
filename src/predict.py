import os
import pandas as pd
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics
import joblib
import numpy as np

from . import dispatcher


def predict(test_data_path, model_type, model_path):
    df = pd.read_csv(test_data_path)
    test_idx = df["Id"].values
    predictions = None

    for FOLD in range(5):
        df = pd.read_csv(test_data_path)
        encoders = joblib.load(os.path.join(model_path, f"{model_type}_{FOLD}_label_encoder.pkl"))
        cols = joblib.load(os.path.join(model_path, f"{model_type}_{FOLD}_columns.pkl"))
        for c in encoders:
            lbl = encoders[c]
            df.loc[:, c] = df.loc[:, c].astype(str).fillna("NONE")
            df.loc[:, c] = lbl.transform(df[c].values.tolist())
        
        clf = joblib.load(os.path.join(model_path, f"{model_type}_{FOLD}.pkl"))
        
        df = df[cols]
        preds = clf.predict(df)

        if FOLD == 0:
            predictions = preds
        else:
            predictions += preds

        predictions /= 5    
    
    

    sub = pd.DataFrame(np.column_stack((test_idx, predictions)), columns=["Id", "SalePrice"])
    return sub
    

if __name__ == "__main__":
    submission = predict(test_data_path="input/test.csv", 
                         model_type="xgb", 
                         model_path="models/")
    submission.loc[:, "Id"] = submission.loc[:, "Id"].astype(int)
    submission.to_csv(f"models/rf_submission.csv", index=False)