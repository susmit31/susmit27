from flask import Flask
from flask import request
from flask_cors import CORS
from PIL import Image
import pytesseract as pt

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'helloworld'

ALLOWED_EXTENSIONS = ['jpg', 'png']

@app.route('/hi-<name>')
def print_name(name):
    return {
        "name": f"{name}",
        "message":"hi"
    }

def allowed_file(filename):
    ext = filename.rsplit('.',maxsplit=1)[1].lower()
    return (ext in ALLOWED_EXTENSIONS)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if request.method=='POST':
        file = request.files['uploaded-image']
        if file and allowed_file(file.filename):
            img = Image.open(file)
            text = pt.image_to_string(img)
            return {
                'text': text
            }
    

app.run(debug=True)