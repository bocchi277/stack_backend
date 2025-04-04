from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load CSV data
df = pd.read_csv("top_10_tags_per_year.csv")
@app.route("/data", methods=["GET"])
def get_data():
    data = df.to_dict(orient="records") 
    return jsonify(data)

if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0", port=5000)
