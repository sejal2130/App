from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    rows = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            # ===== PIPELINE =====
            df = pd.read_csv(path)        # Extract
            df = df.dropna()              # Transform
            output_path = "data/clean.csv"
            df.to_csv(output_path, index=False)  # Load

            rows = len(df)

    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
