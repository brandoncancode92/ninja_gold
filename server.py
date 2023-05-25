from flask import Flask, request, render_template, redirect, session
# Import random to add or take gold randomly.
import random

app = Flask(__name__)

# Session secret key.
app.secret_key = "Loki"

# Root route.
@app.route('/')
def index():
    if "gold" and 'activity_log' not in session:
        session['gold'] = 0
        session['activity_log'] = []
    return render_template("index.html")

# Route for processing gold.
@app.route('/process_gold', methods=["POST"])
def process_gold():
    if 'farm' == request.form['property']:
        gold = random.randint(10,20)
        session['gold'] += gold
        session['activity_log'].append(f"You earned {gold} gold nuggets!")
        return redirect('/')

    if 'cave' == request.form['property']:
        gold = random.randint(5,10)
        session['gold'] += gold
        session['activity_log'].append(f"You earned {gold} gold nuggets!")
        return redirect('/')

    if 'house' == request.form['property']:
        gold = random.randint(2,5)
        session['gold'] += gold
        session['activity_log'].append(f"You earned {gold} gold nuggets!")
        return redirect('/')

    if 'casino' == request.form['property']:
        gold = random.randint(-50,50)
        if gold < 0:
            session['gold'] -= gold
            session['activity_log'].append(f"You lost {gold} gold nuggets!")
        else:
            session['gold'] += gold
            session['activity_log'].append(f"You earned {gold} gold nuggets!")
        return redirect('/')


# Route for reseting session/game
@app.route('/reset') # may need post method
def reset():
    session.clear()
    return redirect('/')
# Add a button to actually clear in the HTML

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)