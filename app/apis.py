import json

from app import app

from app.image_models import get_all_images
from app.image_models import add_image

from flask import render_template
from flask import request
from flask import session

IMAGE_LIST = []

@app.route('/images/', methods=['GET', 'POST'])
def process_images():
    if request.method == 'POST':
        data = json.loads(request.data)
        IMAGE_LIST.append(data.get('src'))
        # I should probably clean these input values somehow.
        add_image(data.get('name', ''), data.get('src'))
    images = get_all_images()
    # images = IMAGE_LIST
    return render_template('show_images.html', images=images)
