from h2o_wave import main, app, Q, ui


@app('/pregma')
async def serve(q: Q):
    q.page['card1'] = ui.form_card(box='1 1 2 2', items=[
        ui.text(content='Pregma'),
        ui.button(name='button1', label='Button 1', primary=True),
    ])

    # if q.args
    await q.page.save()
