from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from io import BytesIO
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware
from model import Document
from utils import clean_text, extract_text_from_pdf
from database import add_document, search_documents

from dotenv import load_dotenv

load_dotenv()


    
# Initialize FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load sentence transformer model for embeddings
model = SentenceTransformer("all-mpnet-base-v2")

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(os.getenv("PINECONE_API"))

# Define the index name
index_name = 'quickstart'

# Check if the index already exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=model.get_sentence_embedding_dimension(),
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        ) 
    ) 

app.state.index = pc.Index(index_name)


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    try:
        
        file_content = await file.read()
        pdf_file = BytesIO(file_content)
        
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_file)

        # Clean and preprocess text
        cleaned_text = clean_text(text)

        # Create embedding and move to CPU
        embedding = model.encode(cleaned_text).tolist()

        document = Document(
            name=file.filename, 
            text=text, 
            embedding=embedding,
        )
        add_document(document, app.state.index)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/search")
async def search_docs(q: str):
    try:
        results = search_documents(q, model, app.state.index)
        return JSONResponse(content=results)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
