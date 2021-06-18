from flask_app import app
#  import your controllers 
from flask_app.controllers import dojos

if __name__ == "__main__":
    app.run(debug=True)