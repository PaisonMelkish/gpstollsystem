from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def reg():
    return render_template("index.html") 

@app.route("/next1", methods=["POST"]) 
def page3():
    return render_template("page3.html") 

@app.route("/next2") 
def page4():
    return render_template("page4.html")

if __name__ == "__main__":
    app.run(debug=True) 
