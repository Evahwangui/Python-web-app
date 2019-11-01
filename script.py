# importing the flask class object from the flask library
from flask import Flask, render_template


# instanciating the flask class. the  __name__ gets the name of the python script. Python assigns 
# the name __main__ to the python script
app = Flask(__name__)

#url to view the website. The slash means the home page
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return "This is the about page!"

# if __name__ == "__.main__":
#     app.run(debug = True)


if __name__ == '__main__':
    app.run(debug=True)