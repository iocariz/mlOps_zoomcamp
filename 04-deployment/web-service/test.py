import predict

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

features = predict.prepare_features(ride)
predictions = predict.predict(ride)