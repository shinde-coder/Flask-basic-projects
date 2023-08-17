import os
from flask import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:/Flask/flask/testing1/files_uploading/static'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'pdf', 'mp3', 'jpeg', 'gif', 'txt'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/media/upload', methods=['POST'])
def upload_media():
    if 'file' not in request.files:
        return jsonify({"error": 'media not provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'no file selected'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"msg": "Media added successfully"})
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
