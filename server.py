from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo"
@app.route('/michael')
def dojo():
    return "Hi Michael"
@app.route('/flask')
def dojo():
    return "Hi Flask"
@app.route('/john')
def dojo():
    return "Hello John"
@app.route('/hello/<string:hello>/<int:num>')
def hello(hello,num):
    return f"Hello {hello * num}"
if __name__=="__main__":
    app.run(debug=True)
def hello(hello,num):
    return f"Hello {hello * num}"
@app.route('/hello/<string:hello>/<int:num>')
def bye(bye,num):
    return f"bye {bye * num}"
if __name__=="__main__":
    app.run(debug=True)
@app.route('/dogs>/<int:num>')
def hello(dogs,num):
    return f"dogs {dogs * num}"
if __name__=="__main__":
    app.run(debug=True)


