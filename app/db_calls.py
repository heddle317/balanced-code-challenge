import os
import sqlite3

from app import app

from flask import g

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(os.path.join(app.root_path, '..', 'schema.sql'), mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    '''
        Checks to see if the database url is in memory. If the db is in memory then it
        has to be initialized each time a connection is made.
    '''
    if app.config['DATABASE'] == ':memory:':
        return get_db_memory()
    return get_db_persisted()


def get_db_memory():
    """Opens a new database connection if there is none yet for the
    current application context.
    It also initializes the database whenever it opens a connection because
    the db schema has to be uploaded for every new connection.
    This is used for the testing module.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        with app.open_resource(os.path.join(app.root_path, '..', 'schema.sql'), mode='r') as f:
            g.sqlite_db.cursor().executescript(f.read())
            g.sqlite_db.commit()
    return g.sqlite_db


def get_db_persisted():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
