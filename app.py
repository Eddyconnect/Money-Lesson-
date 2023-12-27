from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static')

ROOMS = [{
    'id': 1,
    'group-name': 'ML Community',
    'description': 'General ML Community discussion group.',
    'join-link': 'http://bit.ly/ml_community'
}, {
    'id': 2,
    'group-name': 'ML Book Reading Challenge',
    'description':
    'A sub-group of ML community dedicated to self development book readings.',
    'join-link': 'http://bit.ly/ml_community'
}, {
    'id': 3,
    'group-name': 'ML Stocks',
    'description':
    'A sub-group of ML community dedicated to crypto discussions.',
    'join-link': 'http://bit.ly/ml_community'
}, {
    'id': 4,
    'group-name': 'ML Savings Challenge 2024',
    'description':
    'A sub-group of ML community dedicated to personal savings target.',
    'join-link': 'http://bit.ly/ml_community'
}, {
    'id': 5,
    'group-name': 'ML Crypto',
    'description':
    'A sub-group of ML community dedicated to crypto discussions.',
    'join-link': 'http://bit.ly/ml_community'
}, {
    'id': 6,
    'group-name': 'ML Accountability Group 2024',
    'description':
    'A sub-group of ML community dedicated to individuals ready to go the extra mile to score their 2024 goals.',
    'join-link': 'https://wa.link/y3nrhp'
}]


@app.route('/')
def hello_world():
  return render_template('index.html', rooms=ROOMS)


@app.route('/api/groups')
def groups_list():
  return jsonify(ROOMS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
