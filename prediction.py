import joblib
def predict(data):
    rf = joblib.load('test_rf_model.sav')
    return rf.predict(data)
