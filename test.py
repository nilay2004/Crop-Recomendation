import pytest
import numpy as np
import pickle
import os

# Load the trained model
model_path = "RF.pkl"
assert os.path.exists(model_path), "Model file not found. Make sure RF.pkl is in the same directory."
model = pickle.load(open(model_path, 'rb'))

# Function to test
def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    return prediction[0]

# Test Cases
def test_valid_input_1():
    result = predict_crop(90, 40, 40, 25, 80, 6.5, 200)
    assert isinstance(result, str)
    assert result != ""

def test_valid_input_2():
    result = predict_crop(10, 30, 20, 18, 60, 6.0, 120)
    assert result in model.classes_

def test_boundary_values():
    result = predict_crop(0, 0, 0, 0, 0, 0, 0)
    assert result in model.classes_

def test_high_values():
    result = predict_crop(140, 145, 205, 50, 100, 14, 500)
    assert result in model.classes_
