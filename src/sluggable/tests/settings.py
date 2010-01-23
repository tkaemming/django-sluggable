import os

DIRNAME = os.path.dirname(os.path.abspath(__file__))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'test.db')

INSTALLED_APPS = (
    'sluggable',
    'sluggable.tests',
)