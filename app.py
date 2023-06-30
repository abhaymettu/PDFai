import requests
from flask import Flask, render_template, request, jsonify, session
import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI

app = Flask(__name__)
app.secret_key = '1234'  

os.environ["OPENAI_API_KEY"] = "your API key"

loader = None
db = None
qa = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global loader, db, qa
    if 'pdf_file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded'})

    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'})

    file.save('temp.pdf')
    loader = PyPDFLoader("temp.pdf")
    pages = loader.load_and_split()
    chunks = pages

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.1), db.as_retriever())

    os.remove('temp.pdf')
    session['chat_history'] = []
    return render_template('chat.html')


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    if message.lower() == 'exit':
        return jsonify({'response': 'Thank you for using Abhay\'s chatbot!'})

    response = chatbot_response(message)

    chat_history = session.get('chat_history', [])
    chat_history.append({'user': message})
    session['chat_history'] = chat_history

    return jsonify({'response': response})

def chatbot_response(message):
    chat_history = session.get('chat_history', [])
    chat_history.append({'user': message})

    responses = []

    for i, chat in enumerate(chat_history):
        result = qa({"question": chat['user'], "chat_history": [entry['user'] for entry in chat_history[:i]]})
        response = result['answer']
        responses.append(response)
 
    session['chat_history'] = chat_history

    return '\n'.join(responses)





if __name__ == '__main__':
    app.run()
