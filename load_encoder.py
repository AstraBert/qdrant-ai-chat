from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer(
    "jinaai/jina-embeddings-v2-base-en", # switch to en/zh for English or Chinese
    trust_remote_code=True
)