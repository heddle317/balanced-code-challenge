from app.db_calls import get_db


def get_all_images():
    db = get_db()
    cur = db.execute('select image from images')
    images = cur.fetchall()
    return [image[0] for image in images]
 

def add_image(name, image):
    if not image:
        return
    db = get_db()
    db.execute('insert into images (name, image) values (?, ?)',
                     [name, image])
    db.commit()
