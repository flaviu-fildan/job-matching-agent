from flask import Flask
from chatwrap.client import LlmClient

app = Flask(__name__)
LLM_SERVER_URL = 'http://localhost:1234/v1'

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/cv', methods=['POST'])
def upload_cv():
    cv = "Flaviu Fildan, I know Python, Java 5 years+, C++ - personal projects"
    llmClient = LlmClient(LLM_SERVER_URL)

    return cv

@app.route('/candidates/find', methods=['POST'])
def find_candidates():
    
    return 'Find candidates'

if __name__ == '__main__':
    app.run()

