from h2o_wave import main, app, Q, ui


@app('/pregma')
async def serve(q: Q):

    q.page['card1'] = ui.form_card(box='1 1 2 10', items=[
        ui.text(content="Hello world!"),
    ])

    await q.page.save()

# TODO: create a form to get the input for the email  and password
# TODO: crete a form to get the first month data
# TODO: create a form to get the second month data
# TODO: connect to the database (write the data to the firebase database) - use the firebase admin sdk - leave this for the last
# TODO: connect the pickle files to the form 1 and form 2