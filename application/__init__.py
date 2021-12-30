from flask import Flask

app = Flask(__name__)

# Import routes at the bottom to prevent looping
from application import routes