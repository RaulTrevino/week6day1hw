from app import app
from database import Power


@app.get('/power')
def get_post():
    return {'power': Power}
@app.post('/power')
def get_post():
    pass
@app.put('/power')
def get_post():
    pass
@app.delete('/power')
def get_post():
    pass