from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "BG Remover Backend Live!"

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    
    # Open image
    input_img = Image.open(file.stream).convert("RGBA")

    # Remove background
    output_img = remove(input_img)

    # Save in memory (no storage)
    byte_io = io.BytesIO()
    output_img.save(byte_io, format='PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
