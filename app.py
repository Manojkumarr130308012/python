import os
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io


# inputPath = easygui.fileopenbox(title='Select image file')
# outputPath = easygui.filesavebox(title='Save file to...')

# input = Image.open(inputPath)
# output = remove(input)
# output.save(outputPath)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/remove-background', methods=['POST'])
def remove_background():
    # Check if an image was uploaded
    if 'image' not in request.files:
        return 'No image file provided', 400

    # Read the uploaded image file
    file = request.files['image']
    input_data = file.read()

    # Process the image to remove the background
    output_data = remove(input_data)
    output_io = io.BytesIO(output_data)

    # Return the processed image
    return send_file(output_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


