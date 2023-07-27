from sys import stderr
import os
import requests
from datetime import datetime
import csv


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)

        url = 'https://jsonplaceholder.typicode.com/todos/'
        response = requests.get(url)

        if response.status_code == 200:
            todos = response.json()
            for todo in todos:
                self.todo_to_csv(todo)
        else:
            print(f"Error fetching data from API: {response.status_code}", file=stderr)


    def todo_to_csv(self, todo):
        todo_id = todo['id']
        filename = f"{datetime.now().strftime('%Y_%m_%d')}_{todo_id}.csv"
        storage_dir = 'storage'

        # create the storage directory if it does not exist
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

        with open(os.path.join(storage_dir, filename), 'w', newline='') as csvfile:
            fieldnames = ['userId', 'id', 'title', 'completed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(todo)