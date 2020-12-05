import os
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

DATABASE_ENGINE=os.environ.get('DATABASE_ENGINE','SQLITE')

if DATABASE_ENGINE == 'SQLITE':
    dir_path=Path(os.path.dirname(os.path.realpath(__file__)))
    path=dir_path / '..'

    FILE_PATH=f'{path}/db.sqlite3'

    db_config={
        'SQLALCHEMY_DB_URI': 'sqlite+pysqlite:///{file_path}'.format(file_path=FILE_PATH),
        'SQLALCHEMY_TRACK_MODIFICATIONS':False,
    }
else:
    raise Exception('incorrect engine')

db=SQLAlchemy()