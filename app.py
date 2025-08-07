from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Sample data
chocolates = [
    {
        "name": "Dark Chocolate",
        "image": "https://m.media-amazon.com/images/I/81EAqP0D0+L.jpg",
        "price": 6.55
    },
    {
        "name": "Milk Chocolate",
        "image": "https://m.media-amazon.com/images/I/81Rz8SxtiJL.jpg",
        "price": 4.99
    },
    {
        "name": "White Chocolate",
        "image": "https://m.media-amazon.com/images/I/61-pg5u+9pL.jpg",
        "price": 6.49
    },
    {
        "name": "Aged Chocolate",
        "image": "https://m.media-amazon.com/images/I/61-pg5u+9pL.jpg",
        "price": 12226.49
    }
]

@app.route('/chocolates', methods=['GET'])
def get_chocolates():
    return jsonify(chocolates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)