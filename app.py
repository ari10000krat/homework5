from flask import Flask
from faker import Faker
from csv import reader
from tabulate import tabulate
from requests import get
from base58 import b58encode, b58decode

app = Flask(__name__)


@app.route('/requirements/')
def output_requirements():
    result = ''
    with open('requirements.txt', encoding='utf-8') as file:
        for line in file:
            result += f'{line}'
    return f'<pre>{result}</pre>'


@app.route('/generate-users/<int:countOfUsers>/')
def generate_users(countOfUsers):
    if countOfUsers == 0:
        return 'Invalid count of users'
    userData = []
    userInfo = ['Name', 'E-mail']
    fake = Faker(['ru_RU'])
    for i in range(countOfUsers):
        userData.append([fake.first_name(), fake.email()])
    table = tabulate(userData, userInfo, tablefmt='grid')
    return f'<pre>{table}</pre>'


@app.route('/mean/')
def analize_csv():
    SummOfHeights = 0
    SummOfWeights = 0
    count = 0
    try:
        with open('static/hw05.csv', encoding='utf-8') as r_file:
            file_reader = reader(r_file, delimiter=',')
            for row in file_reader:
                if count != 0:
                    SummOfHeights += float(row[1])
                    SummOfWeights += float(row[2])
                count += 1
            return f'<pre>Parsed file: {r_file.name}\n' \
                   f'Total values in file (strings of data): {count - 1}\n' \
                   f'Average height: {round(SummOfHeights / (count - 1) * 2.54, 2)} cm\n' \
                   f'Average weight: {round(SummOfWeights / (count - 1) * 2.2, 2)} kg\n</pre>'
    except:
        return 'No such file exists'


@app.route('/space/')
def output_space_information():
    r = get('http://api.open-notify.org/astros.json')
    return f"Number of astronauts: {r.json()['number']}"


@app.route('/base58encode/<string:s>/')
def encode_base58(s):
    if ' ' in s:
        return 'The string cannot contain spaces'
    else:
        return b58encode(s)


@app.route('/base58decode/<string:s>/')
def decode_base58(s):
    if ' ' in s:
        return 'The string cannot contain spaces'
    else:
        return b58decode(s)


if __name__ == '__main__':
    app.run()
