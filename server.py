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

    # Get the property name from the request
    property_name = request.form['property']

    # Get the winnings for the property
    winnings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }.get(property_name)

    # Add the winnings to the user's gold
    if winnings is not None:
        session['gold'] += winnings

    # Add the winnings to the user's gold_won list
    session['gold_won'].append(winnings)

    # Subtract one move from the user's total_moves
    session['total_moves'] -= moves

    # Print the user's total_moves
    print(session['total_moves'])

    # Redirect the user to the home page
    return redirect('/')


# Route for reseting session/game.
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)

# TO DO LIST
# Reduce the number of conditional statments in server to less than 4.(Done)
# Change the color of the activity log based on positive or negative gold earned.(Done)
# List the activity log in descending order.(Done)
# Limit the number of moves and set the score that has to be reached to win the game.(Done)
# Display the Winner/Loser reset buttons based on winning or losing the game.(Done)
# Make the game look better with bootstrap and css.(Done)