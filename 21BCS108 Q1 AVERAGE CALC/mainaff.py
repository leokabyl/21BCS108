from flask import Flask, jsonify, request
import requests
from collections import deque

app = Flask(__name__)

WINDOW_SIZE = 10
numbers_queue = deque(maxlen=WINDOW_SIZE)
prev_numbers = []

THIRD_PARTY_SERVER_URL = 'http://127.0.0.1:9877/numbers'  # Local third-party server URL

def get_number_from_third_party(number_id):
    url = f"{THIRD_PARTY_SERVER_URL}/{number_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('numbers', [])
    else:
        return []

def calculate_average(queue):
    if not queue:
        return 0
    return sum(queue) / len(queue)

@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_average(number_id):
    try:
        numbers = get_number_from_third_party(number_id)

        for number in numbers:
            if number not in numbers_queue:
                numbers_queue.append(number)
                prev_numbers.clear()
                prev_numbers.extend(numbers_queue)

        average = calculate_average(numbers_queue)

        response = {
            'windowPrevState': list(prev_numbers),
            'windowCurrState': list(numbers_queue),
            'numbers': list(numbers),
            'avg': average
        }

        return jsonify(response)
    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=9876)
