from flask import Flask, render_template, request
import pickle

# Load the model (assuming it's in the same directory)
model = pickle.load(open('FLASK Files/ridge_regression.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("base.html")  # Assuming base.html exists

@app.route('/assesment')
def prediction():
    return render_template("index.html")  # Assuming index.html exists

@app.route('/predict', methods=['POST'])
def admin():
    # Get form data
    mfr = request.form["mfr"]
    cereal_type = request.form["type"]
    calories = float(request.form["Calories"])  # Convert to float
    protein = float(request.form["Protien"])  # Convert to float
    fat = float(request.form["Fat"])  # Convert to float
    sodium = int(request.form["Sodium"])  # Convert to int
    fiber = float(request.form["Fiber"])  # Convert to float
    carbo = float(request.form["Carbo"])  # Convert to float
    sugars = int(request.form["Sugars"])  # Convert to int
    potass = int(request.form["Potass"])  # Convert to int
    vitamins = int(request.form["Vitamins"])  # Convert to int
    shelf = float(request.form["Shelf"])  # Convert to float
    weight = float(request.form["Weight"])  # Convert to float
    cups = float(request.form["Cups"])  # Convert to float


    # One-hot encode mfr (assuming 'a' to 'n' represent categories)
    mfr_encoded = [0] * 7  # Initialize empty list for one-hot encoding
    if mfr == 'a':
        mfr_encoded[0] = 1
    elif mfr == 'g':
        mfr_encoded[1] = 1
    elif mfr == 'k':
        mfr_encoded[2] = 1
    elif mfr == 'n':
        mfr_encoded[3] = 1
    elif mfr == 'p':
        mfr_encoded[4] = 1
    elif mfr == 'q':
        mfr_encoded[5] = 1
    elif mfr == 'r':
        mfr_encoded[6] = 1
    else:
        print(f"Warning: Invalid mfr value: {mfr}")  # Handle invalid mfr

    # Encode cereal type (assuming 'c' and 'h' represent categories)
    cereal_type_encoded = 0 if cereal_type == 'c' else 1

    # Prepare data for prediction
    data = [[*mfr_encoded, cereal_type_encoded, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups]]

    # Make prediction
    prediction = model.predict(data)
    if len(prediction.shape) > 1:  # Check if it's a multi-dimensional array
        prediction = prediction[0][0]  # Access first element from first row
    else:
        prediction = prediction[0]  # Access the single value

    return render_template("prediction.html", z=prediction)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to True for development