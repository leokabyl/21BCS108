
import random
from flask import Flask, jsonify

app = Flask(__name__)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
random_numbers = [] #[i for i in range(1, 101)]
for i in range(10):
    random_numbers.append(random.randint(1,9))

@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_numbers(number_id):
    if number_id == 'p':
        return jsonify({'numbers': prime_numbers})
    elif number_id == 'f':
        return jsonify({'numbers': fibonacci_numbers})
    elif number_id == 'e':
        return jsonify({'numbers': even_numbers})
    elif number_id == 'r':
        return jsonify({'numbers': random_numbers})
    else:
        return jsonify({'numbers': []}), 404

if __name__ == '__main__':
    app.run(debug=True, port=9877)
