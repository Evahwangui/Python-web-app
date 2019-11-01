from flask import Flask


app = Flask(__name__)

#url to view the website. The slash means the home page
@app.route('/')
def home():
    return "Web content goes here!"

# if __name__ == "__.main__":
#     app.run(debug = True)

if __name__ == '__main__':
    app.run(debug=True)