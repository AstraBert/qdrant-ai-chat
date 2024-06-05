# Qdrant-AI-Chat

## Your RAG-based assistant, quick and easy

In this repository lies the [code](./app.py) to build a RAG-based assistant, exploiting Qdrant and Hugging Face Spaces API.

<div align="center">
	<a href="https://huggingface.co/spaces/as-cle-bert/tcfd_counselor"><img src="./imgs/consulting_robot.jpg"></a>	
	<p><i>Image by <a href="https://pollinations.ai/">Pollinations AI</a></i></p>
</div>

## 0. Choose your objective

The first thing to start building is to actually _know_ what you are going to build. In this repository, we will be using [climatebert's TCFD recommendations dataset](https://huggingface.co/datasets/climatebert/tcfd_recommendations), in order to create a climate financial disclosure counselor that will be able to guide us in the wonders and dangers of climate investments and safety.

## 1. Find a database

To implement RAG (*Retrieval-Augmented Generation*), we need to first find a database provider that will host our knowledge base.

A possible solution, simple, elegant and fast, which offers up to 1GB of disk space in its free tier, is [Qdrant](https://qdrant.tech).

So you have to:

1. [Register](https://qdrant.tech/pricing/) to Qdrant Cloud services
2. Create your first cluster
3. Retrieve the API key and the URL of the endpoint for your cluster

## 2. Upload your data

There are various ways to upload your data, one can be found in [this Gist I created for the purpose](https://gist.github.com/AstraBert/ff4bff338d4346718ae6c2d77ea2d71f), where I load data from the above mentioned HF dataset and, exploiting [Jina AI's jina-embeddings-v2-base-en encoder](https://huggingface.co/jinaai/jina-embeddings-v2-base-en), I encode them into 768-dimensional vectors, that are sent to my Qdrant cluster along with the actual Natural Language text.

The so-created database is then available for vector search, you just need to have the same encoder [loaded in your script](./load_encoder.py) and to define some searching functions (I created a class, `NeuralSearcher`, in [utils.py](./utils.py)).

## 3. Build the application
Prior to building the application, consider downloading all the needed dependencies with:

```bash
python3 -m pip install requirements.txt
```

We build the application exploiting [Gradio](https://gradio.app), a popular front-end rendering library for python and JS. 

All the code can be found in [app.py](./app.py).

First of all, we save all our crucial but sensitive variables in a `.env` file (an example can be found [here](./.env.example)).

With Gradio, we create a simple ChatBot interface, where the conversation will be displayed. 

Prior to that, we define a `reply` function that, taking the message from the user, feeds it first to our retriever (`NeuralSearcher`, in my case), in order to get out from our knowledge base in Qdrant some valuable contextual information. After that, the retrieved context gets inserted in the prompt that will be submittend to our LLM, alongside with some instructions (optional) and the user's query.

The LLM we are exploiting is Phi-3-mini-128K, queried via HF Spaces API offered by [this Space](https://huggingface.co/spaces/eswardivi/Phi-3-mini-128k-instruct).

Everything is then smoothly rendered with a custom front-end theme, that you can find [here](https://huggingface.co/spaces/JohnSmith9982/small_and_pretty).

## Wanna see a demo?

Chat with my space here:

<div align="center">
	<iframe
		src="https://as-cle-bert-tcfd-counselor.hf.space"
		frameborder="0"
		width="850"
		height="450"
	></iframe>
</div>

## And now it's your turn! Ready to build amazing AI-powered apps?🚀
