from flask import Flask
from faker import Faker
from tabulate import tabulate


app = Flask(__name__)


@app.route('/generate-users/<int:countOfUsers>/')
def generate_users(countOfUsers):#http://127.0.0.1:5000/generate-users/5/
    userData = []
    fake = Faker(['ru_RU'])
    for i in range(countOfUsers):
        userData.append([fake.first_name(), fake.email()])
    return str(userData)


if __name__ == '__main__':
    app.run(debug=True)
