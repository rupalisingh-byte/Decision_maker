from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)
# Use a secure secret key (important for production, but simple for learning)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-secret-key-change-me')

# Global state to store the choices (in a real app, this would be a database)
CHOICES = []
LAST_DECISION = None

@app.route('/', methods=['GET'])
def index():
    """Renders the main page, showing current choices and the last decision."""
    # The global variables CHOICES and LAST_DECISION are passed to the template.
    return render_template('form.html', choices=CHOICES, last_decision=LAST_DECISION)

@app.route('/add_choice', methods=['POST'])
def add_choice():
    """Handles adding a new choice to the global list."""
    new_choice = request.form.get('choice')
    if new_choice:
        # Prevent duplicate entries and empty strings
        choice_clean = new_choice.strip()
        if choice_clean and choice_clean not in CHOICES:
            CHOICES.append(choice_clean)
            global LAST_DECISION
            # Reset the last decision when new options are added
            LAST_DECISION = None 
    
    # Redirect back to the home page (Good practice after a POST request)
    return redirect(url_for('index'))

@app.route('/decide', methods=['POST'])
def decide():
    """Picks a random choice from the list."""
    global LAST_DECISION
    if CHOICES:
        # Use random.choice to select a random item
        LAST_DECISION = random.choice(CHOICES)
    else:
        LAST_DECISION = "Please add some choices first!"

    # Redirect back to the home page to display the result
    return redirect(url_for('index'))

@app.route('/clear', methods=['GET'])
def clear_choices():
    """Clears all choices and the last decision."""
    global CHOICES
    global LAST_DECISION
    CHOICES = []
    LAST_DECISION = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Running the app in debug mode helps you see errors easily
    print("Flask app running on http://127.0.0.1:5000/")
    app.run(debug=True)


