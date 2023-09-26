from flask import Flask, request

app= Flask(__name__)


from resorces.mutant.routes import routes
from resorces.power.routes import routes