from flask import Blueprint, render_template

# Create the index blueprint
blueprint = Blueprint('index', __name__)


# Define the route for the index page
@blueprint.route('/')
def index():
    return render_template('index.html')
