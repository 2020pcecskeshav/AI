from flask import flask,render_template
app=flask(__name__)
@app.route('/')
def home():
    text="Hi"
    if request.args.get('q')!=None:
        que=request.args.get('q')
        text+=que
    return render_template('chatbot.html',resp=text)
@app.route('/new')
def new():
    return"<html><h1>awesome<h1></html>"
app=run(debug=True)