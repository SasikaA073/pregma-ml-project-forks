# using the pickle file 
import h2o_wave
from h2o_wave import Q, ui
import pandas as pd
import h2o
import pickle

import h2o
ipA = "127.0.0.1"
portN = "5431"
urlS = "http://127.0.0.1:54321"
connect_type=h2o.connect(ip=ipA, port=portN, verbose=True)


# Define pickle file name
pickle_file_name = "pregma_model_1.pkl"

# Connect to H2O cluster
h2o.init()

# Load the pre-trained model from a pickle file
with open(pickle_file_name, 'rb') as f:
    model = pickle.load(f)

# Define a function to generate the UI
def generate_ui():
    # Create a Wave app instance
    app = h2o_wave.init()

    # Define a layout
    view = [
        ui.form_card(
            box='1 1 8 6',
            items=[
                ui.text('Enter the values to make predictions:'),
                ui.textbox(name='val1', label='Value 1', required=True),
                ui.textbox(name='val2', label='Value 2', required=True),
                ui.textbox(name='val3', label='Value 3', required=True),
                ui.textbox(name='val4', label='Value 4', required=True),
                ui.buttons([
                    ui.button(name='predict_button', label='Predict', primary=True),
                    ui.button(name='reset_button', label='Reset'),
                ]),
            ],
        ),
        ui.text_card(
            box='1 7 8 1',
            text='Prediction results:',
        ),
        ui.text_card(
            box='1 8 8 3',
            name='prediction_result',
            text='',
        ),
    ]

    # Register the layout
    app.set_route('/', view)

    # Define a function to handle the button clicks
    async def predict(q: Q):
        if q.args.predict_button:
            # Get the values entered by the user
            val1 = float(q.args.val1)
            val2 = float(q.args.val2)
            val3 = float(q.args.val3)
            val4 = float(q.args.val4)

            # Make a prediction
            data = {'val1': [val1], 'val2': [val2], 'val3': [val3], 'val4': [val4]}
            hf = h2o.H2OFrame(pd.DataFrame(data))
            prediction = model.predict(hf).as_data_frame().iloc[0, 0]

            # Update the UI with the prediction result
            await q.page['prediction_result'].update(text=f'The prediction is {prediction}.')

        elif q.args.reset_button:
            # Reset the form
            await q.page['val1'].set('')
            await q.page['val2'].set('')
            await q.page['val3'].set('')
            await q.page['val4'].set('')
            await q.page['prediction_result'].update(text='')

    # Register the button click handler
    app.on(q=predict)


# Generate the UI
generate_ui()
