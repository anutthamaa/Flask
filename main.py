'''
jinja 2 template engine

{%....%} -> conditions, for loops
{{ }} -> to get the parameter
{#....#} -> for comments
'''


from flask import Flask, redirect, url_for, render_template, request

'''WSGI application is created for communication between web applocation and web server'''
app = Flask(__name__)


@app.route('/') ##Decorator to define the urls
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res='Pass'
    else:
        res='Fail'
        
    res_dict = {"Score":score, "Result":res}
    return render_template ('result.html',result=res_dict)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        social = float(request.form['social'])
        total = (science+maths+english+social)/4
    return redirect(url_for('success',score=total))


if(__name__ == '__main__'):
    app.run(debug=True)