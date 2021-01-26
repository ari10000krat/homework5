from flask import Flask
from faker import Faker
from csv import reader
from tabulate import tabulate
from requests import get
from base58 import b58encode, b58decode

app = Flask(__name__)



@app.route('/generate-users/<int:countOfUsers>/')  # http://127.0.0.1:5000/generate-users/5/ #TODO удалить
def generate_users(countOfUsers):
    userData = []
    userInfo = ['Name', 'E-mail']
    fake = Faker(['ru_RU'])
    for i in range(countOfUsers):
        userData.append([fake.first_name(), fake.email()])
    table = tabulate(userData, userInfo, tablefmt='grid')
    return f'<pre>{table}<pre>'


@app.route('/mean/')  # http://127.0.0.1:5000/mean/ #TODO удалить
def analize_csv():
    SummOfHeights = 0
    SummOfWeights = 0
    count = 0
    with open('static/hw05.csv', encoding='utf-8') as r_file:
        file_reader = reader(r_file, delimiter=',')
        for row in file_reader:
            if count != 0:
                SummOfHeights += float(row[1])
                SummOfWeights += float(row[2])
            count += 1
        return f'Parsed file: {r_file.name}<br>' \
               f'Total values in file (strings of data): {count - 1}<br>' \
               f'Average height: {round(SummOfHeights / (count - 1), 2)} cm<br>' \
               f'Average weight: {round(SummOfWeights / (count - 1), 2)} kg<br>'


@app.route('/space/')  # http://127.0.0.1:5000/space/ #TODO удалить
def output_space_information():
    r = get('http://api.open-notify.org/astros.json')
    return f"Number of astronauts: {r.json()['number']}"


@app.route('/base58encode/<string:s>/')
def encode_base58(s):
    return b58encode(s)


@app.route('/base58decode/<string:s>/')
def decode_base58(s):
    return b58decode(s)


if __name__ == '__main__':
    app.run(debug=True)
