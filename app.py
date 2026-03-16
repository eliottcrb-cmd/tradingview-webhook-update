from flask import Flask, request, jsonify
import os
import hmac
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook server is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json

        # Debug print to verify incoming payload
        print("Received webhook:", data)

        # Example: read environment variables
        api_key = os.getenv("COINBASE_API_KEY")
        api_secret = os.getenv("COINBASE_API_SECRET")

        if not api_key or not api_secret:
            return jsonify({"error": "Missing API credentials"}), 500

        # TODO: Add your Coinbase trading logic here

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000)
