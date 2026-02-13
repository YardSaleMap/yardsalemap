from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/listings', methods=['GET'])
def get_listings():
    # Code to retrieve listings would go here
    return jsonify({'listings': []})

@app.route('/api/refresh', methods=['POST'])
def refresh_listings():
    # Code to refresh listings would go here
    return jsonify({'message': 'Listings refreshed'}), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)