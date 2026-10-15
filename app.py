from flask import Flask, request, send_file
from ultralytics import YOLO
import os
app = Flask(__name__)
model = YOLO('best.pt')
PAGE = '<h2>Car Damage Detection</h2><form method=post enctype=multipart/form-data><input type=file name=img><button>Check</button></form>'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        request.files['img'].save('in.jpg')
        r = model.predict('in.jpg', conf=0.25)[0]
        r.save('out.jpg')
        return send_file('out.jpg', mimetype='image/jpeg')
    return PAGE

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))