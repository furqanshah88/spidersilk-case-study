from flask import Flask, request, redirect, url_for, render_template
import csv
import boto3
import os
app = Flask(__name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'my-s3-bucket'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join('/uploads', filename))
        process_csv(os.path.join('/uploads', filename))
        s3.upload_file(os.path.join('/uploads', filename), 
BUCKET_NAME, filename)
        return redirect(url_for('index'))
def process_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)