# Project: PDF-based Conversational Assistant

This project creates a conversational assistant which is able to answer queries based on the content of a PDF file. The project uses OpenAI GPT-4 embeddings for representation, FAISS for storing and retrieving these representations, and Flask for handling web requests. As a new student exploring this field, I learned to leverage techniques like document loading, natural language processing embeddings, vector storage, and web development with Flask.

## Requirements

1. Python 3.6 or above
2. Flask
3. PyPDF2
4. requests
5. FAISS
6. OpenAI API (Python Client)

## Setup

1. Clone the repository.

2. Install the required packages using pip:

    ```
    pip install flask PyPDF2 requests faiss-cpu openai
    ```

3. Set the OpenAI API key in your environment. This is used for OpenAI's embeddings:

    ```
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

1. Run the Flask app:

    ```
    python app.py
    ```

2. Open your browser and visit `localhost:5000`.

3. You can upload a PDF file which the bot will read and use to answer queries.

4. After uploading, you will be taken to the chat interface. Type your question and the bot will attempt to answer based on the PDF's content.

## API Endpoints

- GET `/`: The index page with the file upload form.

- POST `/upload`: Upload a PDF file for the bot to process. Returns a chat page for interacting with the bot.

- POST `/chat`: Send a message to the bot and get a response.

## Known Limitations

1. The bot is as accurate as the GPT-4 model, so it might not always give accurate or expected responses.

2. The bot can only understand English text from the PDFs. Non-English or encoded PDFs might cause errors or inaccurate responses.

3. Processing and storing the PDF's contents into embeddings might take some time for large files.

## Future Work

1. Improve the bot's accuracy and performance.

2. Support more file formats and languages.

3. Implement a more interactive and user-friendly chat interface.
