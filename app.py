from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "BG Remover Running"

@app.route('/remove', methods=['POST'])
def remove_bg():
    file = request.files['file']
    input_img = Image.open(file.stream).convert("RGBA")
    output_img = remove(input_img)

    byte_io = io.BytesIO()
    output_img.save(byte_io, format='PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
