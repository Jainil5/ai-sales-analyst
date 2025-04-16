from flask import Flask, jsonify, request
from flask_cors import CORS
from chatbot import generate_reponse
from sales_analysis import metrics_data

app = Flask(__name__)
CORS(app)

@app.route('/api/sales-data', methods=['GET'])
def get_sales_data():
    # You can print or log the sales_data for debugging
    app.logger.info("Sales data requested.")
    return jsonify(metrics_data)

@app.route('/api/chatbot', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        print(data)
        question = data["message"]
        print(question)
        if question:
            # Placeholder response (can be replaced with a chatbot logic)
            answer = generate_reponse(question)
            return f"{answer.upper()}"
        else:
            return jsonify({"error": "No question provided"}), 400  # Return 400 for bad request
    except Exception as e:
        app.logger.error(f"Error processing chat request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500  # Return 500 for server errors

if __name__ == '__main__':
    app.run(debug=True)
