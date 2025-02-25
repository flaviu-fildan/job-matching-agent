CELERY_BROKER_URL = f"sqlalchemy+sqlite:///db.sqlite3"

import os
import time
from celery import Celery
from pdfminer.high_level import extract_text

from utils.db_client import DBClient

pdf_converter = Celery('tasks', broker=CELERY_BROKER_URL)

UPLOAD_FOLDER = 'cvs'

@pdf_converter.task
def convert_pdf(filename):
    ''' Convert PDF to text '''
    # check the file exists
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        raise Exception(f'File {filename} not found')

    document = extract_text(os.path.join(UPLOAD_FOLDER, filename))

    document_id = str(hash(document))

    db_client = DBClient()
    db_client.add(document, document_id, filename)

    print('Document stored in DB')
