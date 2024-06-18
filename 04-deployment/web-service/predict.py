import pickle

with open('model.bin', 'rb' ) as f_in:
    (dv.model) = pickle.load(f_in)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    X = dv.transfrom(features)
    preds = model.predict(X)
    return preds[0]


