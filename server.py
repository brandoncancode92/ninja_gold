from flask import Flask, request, render_template, redirect, session
# Import random to add or take gold randomly.
import random

app = Flask(__name__)

# Session secret key.
app.secret_key = "Loki"

# Root route.
@app.route('/')
def index():
    if 'gold' and 'total_moves' and 'gold_won' not in session:
        session['gold'] = 0
        session['total_moves'] = 15
        session['gold_won'] = []
    return render_template("index.html")

# Route for processing gold and number of moves.
@app.route('/process_gold', methods=["POST"])
def process_gold():
    # Adds gold earned to session
    moves = 1
    if request.form['property'] == 'farm':
        winnings = random.randint(10, 20)
        session['gold'] += winnings
        session['gold_won'].append(winnings)
        session['total_moves'] -= moves
        print(session['total_moves'])
        return redirect('/')

    elif request.form['property'] == 'cave':
        winnings = random.randint(5, 10)
        session['gold'] += winnings
        session['gold_won'].append(winnings)
        session['total_moves'] -= moves
        print(session['total_moves'])
        return redirect('/')

    elif request.form['property'] == 'house':
        winnings = random.randint(2, 5)
        session['gold'] += winnings
        session['gold_won'].append(winnings)
        session['total_moves'] -= moves
        print(session['total_moves'])
        return redirect('/')

    # Adds gold earned/lost to session
    elif request.form['property'] == 'casino':
        winnings = random.randint(-50, 50)
        if winnings < 0:
            session['gold'] += winnings
            session['gold_won'].append(winnings)
            session['total_moves'] -= moves
            print(session['total_moves'])
        else:
            session['gold'] += winnings
            session['gold_won'].append(winnings)
            session['total_moves'] -= moves
            print(session['total_moves'])
        return redirect('/')


# Route for reseting session/game.
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)

# Reduce the number of conditional statments in server to less than 4.
# Change the color of the activity log based on positive or negative gold earned.(Done)
# List the activity log in descending order.(Done)
# Limit the number of moves and set the score that has to be reached to win the game.(Done)
# Display the Winner/Loser reset buttons based on winning or losing the game.(Done)
# Make the game look better with bootstrap and css.