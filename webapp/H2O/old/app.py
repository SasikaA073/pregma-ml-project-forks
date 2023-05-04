import pickle
import h2o
from h2o_wave import Q, app, ui

# Load the pickle file and create a prediction function
with open('pregma_model_1.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(inputs):
    # Create a H2O frame from the input data
    input_frame = h2o.H2OFrame(inputs)

    # Make a prediction using the loaded model
    prediction = model.predict(input_frame).as_data_frame().iloc[0, 0]

    # Return the prediction as a string
    return str(prediction)

# Set up the Wave server
app = app()

# Define the layout of the dashboard
page = app.page('pregnancy')
page.add('header', ui.header('Healthy Pregnancy Predictor'))
page.add('input', ui.form([
    ui.textbox(name='age', label='Age'),
    ui.dropdown(name='ethnicity', label='Ethnicity', choices=[
        ui.choice(name='african_american', label='African American'),
        ui.choice(name='asian', label='Asian'),
        ui.choice(name='caucasian', label='Caucasian'),
        ui.choice(name='hispanic', label='Hispanic'),
        ui.choice(name='other', label='Other')
    ]),
    ui.textbox(name='bmi', label='BMI'),
    ui.textbox(name='glucose', label='Glucose'),
    ui.textbox(name='blood_pressure', label='Blood Pressure'),
    ui.textbox(name='insulin', label='Insulin'),
    ui.textbox(name='pregnancies', label='Number of Pregnancies'),
]))
page.add('output', ui.text(''))

# Create a function to handle requests from the dashboard
async def predict_healthy_pregnancy(q: Q):
    # Get the user input from the form
    inputs = {
        'Age': q.args.age,
        'Ethnicity': q.args.ethnicity,
        'BMI': q.args.bmi,
        'Glucose': q.args.glucose,
        'BloodPressure': q.args.blood_pressure,
        'Insulin': q.args.insulin,
        'Pregnancies': q.args.pregnancies,
    }

    # Use the prediction function to generate a prediction
    prediction = predict(inputs)

    # Update the output display with the prediction
    q.page['output'].text = f'The model predicts that the pregnancy is {"healthy" if prediction == 0 else "unhealthy"}'

# Run the Wave server
if __name__ == '__main__':
    app.run()
