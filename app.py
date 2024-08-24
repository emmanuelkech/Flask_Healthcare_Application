from flask import Flask, render_template, request
from pymongo import MongoClient

# Initialize a Flask application
app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db'] 
collection = db['user_data'] 

@app.route('/', methods=['GET', 'POST'])
def index():
    # If the form is submitted via POST
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        income = request.form.get('income')
        utilities = request.form.get('utilities', 0)
        entertainment = request.form.get('entertainment', 0)
        school_fees = request.form.get('school_fees', 0)
        shopping = request.form.get('shopping', 0)
        healthcare = request.form.get('healthcare', 0)
        
        # Insert data into MongoDB
        collection.insert_one({
            'name': name,
            'age': age,
            'gender': gender,
            'income': income,
            'utilities': utilities,
            'entertainment': entertainment,
            'school_fees': school_fees,
            'shopping': shopping,
            'healthcare': healthcare
        })
    # Render the HTML form
    return render_template('index.html')

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run()
