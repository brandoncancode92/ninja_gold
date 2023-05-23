from flask import Flask, request, render_template, redirect, session
# Import random to add or take gold randomly.
import random

app = Flask(__name__)

# Session secret key.
app.secret_key = "Loki"

# Root route.
@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    return render_template("index.html")

# Route for processing gold.
@app.route('/process_gold', methods=["POST"])
def process_gold():
    if 'farm' == request.form['property']:
        gold = random.randint(10,20)
        session['gold'] += gold
        return redirect('/')

    if 'cave' == request.form['property']:
        gold = random.randint(5,10)
        session['gold'] += gold
        return redirect('/')

    if 'house' == request.form['property']:
        gold = random.randint(2,5)
        session['gold'] += gold
        return redirect('/')

    if 'casino' == request.form['property']:
        gold = random.randint(0,50)
        session['gold'] += gold
        return redirect('/')


# Route for reseting session/game
@app.route('/reset') # may need post method
def reset():
    session.clear()
    return redirect('/')
# Add a button to actually clear in the HTML

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)