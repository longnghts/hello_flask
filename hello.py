from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    

    # import statements, maybe some other routes
    
    @app.route('/dojo')
    def dojo():
        return "Dojo!"
    
    @app.route('/say/<name>')
    def hello(name):
        print(name)
        return "Hi, " + name + "!"

    @app.route('/repeat/<num>/<name>')
    def counter(num, name):
        print(num)
        print(name)
        return name * int(num)
        


# app.run(debug=True) should be the very last statement! 


app.run(debug=True)    # Run the app in debug mode.
