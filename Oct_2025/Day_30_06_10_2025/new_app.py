from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model
with open("linear_model_anyname.pkl", "rb") as obj:
    model = pickle.load(obj)

app = Flask(__name__)

@app.route('/')
def landing_page():
    return "Hello, Welcome to Uptor"

@app.route('/login', methods=['GET'])
def login_page():
    return "Welcome to Login Page"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    year = data.get('year')

    if not year:
        return jsonify({"error": "Please provide JSON body with key 'year'"}), 400

    if isinstance(year, (int, float)):
        year = [year]

    x_value = np.array(year).reshape(-1, 1)
    prediction = model.predict(x_value).tolist()

    return jsonify({
        "input": year,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)