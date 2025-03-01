from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# Sample traffic data storage
traffic_data = {
    "lane1": 30,
    "lane2": 50,
    "lane3": 40
}

@app.route('/', methods=['GET'])
def home():
    return redirect('/get_traffic')

@app.route('/get_traffic', methods=['GET'])
def get_traffic():
    return jsonify(traffic_data)

@app.route('/update_traffic', methods=['POST'])
def update_traffic():
    data = request.get_json()
    if "lane" in data and "vehicle_count" in data:
        traffic_data[data["lane"]] = data["vehicle_count"]
        return jsonify({"message": "Traffic data updated successfully!"}), 200
    return jsonify({"error": "Invalid request data"}), 400

if __name__ == '__main__':
    app.run(debug=True)