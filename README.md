echo "# App" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sejal2130/App.git
git push -u origin main






# Python Data Pipeline (Flask)

A simple ETL pipeline web application built using Python and Flask.

## Features
- Upload CSV file
- Clean data (remove null values)
- Save processed output

## Run
pip install -r requirements.txt  
python app.py
