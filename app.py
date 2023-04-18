from flask import Flask, redirect, url_for

'''WSGI application is created for communication between web applocation and web server'''
app = Flask(__name__)


@app.route('/') ##Decorator to define the urls
def welcome():
    return ("Hi! Welcome to Bangalore")

@app.route('/member')
def welcomename():
    return ("Hi Anu! Welcome")

@app.route('/member/<name>')
def welcomedynamicname(name):
    return ("Hi " + name + "! Welcome")

@app.route('/success/<int:score>')
def success(score):
    return ("You have passed and score is "+ str(score))

@app.route('/fail/<int:score>')
def fail(score):
    return ("You have failed and score is "+ str(score))

@app.route('/results/<int:marks>')
def result(marks):
    res = ""
    if marks < 50:
        res = "fail"
    else:
        res = "success"
    return redirect(url_for(res,score=marks))

if(__name__ == '__main__'):
    app.run(debug=True)