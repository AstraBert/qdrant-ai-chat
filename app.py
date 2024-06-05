import gradio as gr
from gradio_client import Client
from qdrant_client import QdrantClient
from load_encoder import encoder 
from utils import NeuralSearcher
import time
import os
from dotenv import load_dotenv

mytheme = gr.Theme.from_hub("JohnSmith9982/small_and_pretty")

load_dotenv()

collection_name = os.getenv("QDRANT_COLLECTION")
QDRANT_API_KEY = os.getenv("QDRANT_API")
QDRANT_URL = os.getenv("QDRANT_URL")
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)
api_client = Client("eswardivi/Phi-3-mini-128k-instruct")

def reply(message, history):
    global encoder
    global api_client
    global qdrant_client
    txt2txt = NeuralSearcher(collection_name, qdrant_client, encoder)
    context = txt2txt.search(message)
    to_phi = f"Instructions: you are a useful assistant focused on providing valuable content on Climate-related Financial Disclosures; Context: {context}; User prompt: {message}"
    response = api_client.predict(
        to_phi,	# str  in 'Message' Textbox component
        0.2,	# float (numeric value between 0 and 1) in 'Temperature' Slider component
        True,	# bool  in 'Sampling' Checkbox component
        512,	# float (numeric value between 128 and 4096) in 'Max new tokens' Slider component
        api_name="/chat"
    )
    this_hist = ''
    for char in response:
        this_hist += char
        time.sleep(0.0001)
        yield this_hist

demo = gr.ChatInterface(fn=reply, title="Climate-related Financial Disclosures Counselor", theme=mytheme)
demo.launch(server_name="0.0.0.0", share=False)
