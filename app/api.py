import os
from flask import Flask, jsonify, request, Response
from pdfminer.high_level import extract_text

from utils.db_client import DBClient
from workers.pdf_converter import convert_pdf
# from chatwrap.client import LlmClient

app = Flask(__name__)
LLM_SERVER_URL = 'http://localhost:1234/v1'
UPLOAD_FOLDER = 'cvs'

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/skills', methods=['POST'])
def extract_skills():
    # cv = "Flaviu Fildan, I know Python, Java 5 years+, C++ - personal projects"
    body = request.get_json()

    # llmClient = LlmClient(LLM_SERVER_URL)

    return cv

@app.route('/candidates/find', methods=['POST'])
def find_candidates():
    
    return 'Find candidates'

@app.route('/cvs/upload', methods=['POST'])
def upload_cv():
    ''' Upload file and extract skills '''
    file = request.files['file']

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    convert_pdf.delay(file.filename)
    
    return 'File successfully uploaded'

@app.route('/cvs/extract-info', methods=['POST'])
def extract_info():
    ''' Extract info from CV '''
    file_name = request.get_json()['filename']

    print(f'Extracting info from {file_name}')

    # check the file exists
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, file_name)):
        return Response('File not found', status=404)

    text = extract_text(os.path.join(UPLOAD_FOLDER, file_name))

    data = {
        'text': text
    }

    return jsonify(data)

@app.route('/cvs/store', methods=['POST'])
def store_cv():
    ''' Store CV text in DB '''
    document = request.get_json()['document']

    print(f'Storing document in DB')

    document_id = str(hash(document))

    db_client = DBClient()
    db_client.add(document, document_id)
    
    return Response(status=204)

if __name__ == '__main__':
    app.run(debug=True)
