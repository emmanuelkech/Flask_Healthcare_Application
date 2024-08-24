# Import necessary modules
from pymongo import MongoClient
import pandas as pd

class User:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def export_to_csv(self, csv_filename):
        # Extract data from MongoDB
        data = list(self.collection.find({}, {'_id': 0, 'name': 1, 'age': 2, 'gender': 3, 'income': 4, 'utilities': 5, 'entertainment': 6, 'school_fees': 7, 'shopping': 8, 'healthcare': 9}))
        
        # Create a DataFrame
        df = pd.DataFrame(data)
        
        # Save to CSV
        df.to_csv(csv_filename, index=False)

        print(f'CSV file "{csv_filename}" created successfully!')

user = User('survey_db', 'user_data') 
user.export_to_csv('user_data.csv')