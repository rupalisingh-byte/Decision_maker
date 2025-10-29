🎲 Instant Decision Maker (Flask Microservice)

This is a simple, beginner-friendly web application built with Flask and Jinja2 that helps users make quick decisions by randomly selecting an option from a list of user-provided choices.

It's an excellent project for anyone learning the fundamentals of the Flask web framework, focusing on form handling, template rendering, and state management.

🌟 Features

Add Choices: Easily submit new options (e.g., "Go to the movies," "Read a book," "Go hiking").

Instant Decision: Click the "Pick One Now!" button to get a random, unbiased result from the current list.

Clear State: Clear all choices to start a new decision list.

Simple State Management: Uses a global Python list to maintain choices across requests (perfect for a small, single-user learning app).

Modern Styling: Utilizes Tailwind CSS (via CDN) for a clean, fully responsive user interface.

🚀 Getting Started

Follow these steps to get the application up and running on your local machine.

Prerequisites

You need Python 3.x and Flask installed.

# Install the Flask framework
pip install Flask


Installation

Clone this repository (or save the form1.py file and the templates/form.html file):

git clone 
cd decision-maker-app


Ensure you have the following file structure:

**decision-maker-app/
├── form1.py  # The Flask application logic
└── templates/
    └── form.html      # The HTML template (Jinja2)**


Running the Application

Execute the Python file from your terminal:

python decision_maker.py


The application will start, and you can access it in your web browser, typically at:

👉 **http://127.0.0.1:5000/**

🔧 Project Structure

**File/Directory

Description

form1.py**

Contains the core Flask application. Defines routes (/, /add_choice, /decide), handles form submissions, and manages the global list of choices (CHOICES).

templates/

The standard directory where Flask looks for HTML templates.

templates/form.html

The main Jinja2 template for the application. It includes the forms for adding choices, displaying the current list, and showing the final decision.

💡 How It Works (Flask Fundamentals)

This project demonstrates these core Flask concepts:

Rendering Templates: The index() function uses render_template('form.html', ...) to send variables (choices and last_decision) from the Python backend to the Jinja2 template.

Handling POST Requests: The add_choice() and decide() functions use the methods=['POST'] attribute to accept data from the HTML forms.

Accessing Form Data: The request.form.get('choice') method safely extracts the data submitted by the user.

The PRG Pattern: After every action (add or decide), the app uses redirect(url_for('index')) to force a page reload, preventing form resubmissions and cleanly updating the display.
