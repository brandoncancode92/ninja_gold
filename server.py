from flask import Flask, request, render_template, redirect, session
# Import random to add or take gold randomly.
import random

app = Flask(__name__)

# Session secret key.
app.secret_key = "Loki"

# Root route.
@app.route('/')
def index():
    if 'gold' and 'activity_log' and 'total_moves' and 'gold_won' not in session:
        session['gold'] = 0
        session['activity_log'] = []
        session['total_moves'] = 0
        session['gold_won'] = 0
    return render_template("index.html")

# Route for processing gold and number of moves.
@app.route('/process_gold', methods=["POST"])
def process_gold():

    # Adds gold earned and number of moves to session
    if 'farm' == request.form['property'] or 'cave' == request.form['property'] or 'house' == request.form['property']:
        session['gold_won'] = random.randint(10,20)
        session['gold'] += session['gold_won']
        session['activity_log'].append(f"You earned {session['gold_won']} gold nuggets!")
        return redirect('/')

    # Adds gold earned/lost and number of moves to session
    if 'casino' == request.form['property']:
        session['gold_won'] = random.randint(-50,50)
        if session['gold_won'] < 0:
            session['gold'] += session['gold_won']
            session['activity_log'].append(f"You lost {session['gold_won']} gold nuggets!")
        else:
            session['gold'] += session['gold_won']
            session['activity_log'].append(f"You earned {session['gold_won']} gold nuggets!")
        return redirect('/')

# Route for keeping track of the moves and winning the game
@app.route('/win_game', methods=["POST"])
def win_game():
    moves = 0
    if 'farm' == request.form['property'] or 'cave' == request.form['property'] or 'house' == request.form['property'] or 'casino' == request.form['property']:
        moves += 1
        session['total_moves'] += moves

    if session['gold'] < 200 and session['total_moves'] <=15:
        pass

    elif session['gold'] > 200 and session['total_moves'] <=15:
        session['activity_log'].append("Congratulations, you've won!")

    elif session['gold'] > 200 and session['total_moves'] > 15:
        session['actiivity_log'].append("Game Over")

    else:
        session['gold'] < 200 and session['total_moves'] >=16
        session['activity_log'].append("Game Over")
    return redirect('/')

# Route for reseting session/game
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)

# change the color of the activity log based on positive or negative gold earned(Done)
# list the activity log in descending order(Done)
# limit the number of moves and set the score that has to be reached to win the game