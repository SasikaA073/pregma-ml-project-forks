import pickle, os
from flask import Flask, render_template, request

# Define the models you are using
model_name = 'predictor.pkl'

# Construct the path to the pickle file 
model_path = os.path.join(os.path.dirname(__file__), 'models', model_name)

# Load the saved model
with open(model_path, 'rb') as f:
    predictor = pickle.load(f)

# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    """Values that I have to get from the form are:

    'clump_thickness',
    'uniformity_of_cell_size',
    'uniformity_of_cell_shape',
    'marginal_adhesion',
    'single_epithelial_cell_size',
    'bare_nuclei',
    'bland_chromatin',
    'normal_nucleoli',
    'mitoses'
    
    """
    # Convert the values to integers (correct data type)
    clump_thickness = int(request.form['form1-input_clump_thickness'])
    uniformity_of_cell_size = int(request.form['form1-input_uniformity_of_cell_size'])
    uniformity_of_cell_shape = int(request.form['form1-input_uniformity_of_cell_shape'])
    marginal_adhesion = int(request.form['form1-input_marginal_adhesion'])
    single_epithelial_cell_size = int(request.form['form1-input_single_epithelial_cell_size'])
    bare_nuclei = int(request.form['form1-input_bare_nuclei'])
    bland_chromatin = int(request.form['form1-input_bland_chromatin'])
    normal_nucleoli = int(request.form['form1-input_normal_nucleoli'])
    mitoses = int(request.form['form1-input_mitoses'])
       
    # Make a prediction using the loaded model
    prediction = predictor.predict([[
        clump_thickness, uniformity_of_cell_size, uniformity_of_cell_shape, marginal_adhesion, single_epithelial_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitoses
        ]])[0]
    
    

    # Convert the prediction to a string
    if prediction == 0:
        result = 'Benign'
    else:
        result = 'Malignant'

    # Render the prediction results page
    return render_template('result.html', result=result)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
