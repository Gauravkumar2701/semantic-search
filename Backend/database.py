from model import Document
def add_document(document: Document, index):
    index.upsert(
        vectors=[(document.name, document.embedding)],
        namespace="document-index"
    )

def search_documents(query: str, model, index):
    query_embedding = model.encode(query).tolist()

    # Query Pinecone for similar documents
    response = index.query(vector=query_embedding, top_k=5, include_metadata=True, namespace="document-index")

    results = []
    
    for match in response['matches']:
    
        results.append({
            'id': match['id'],
            'score': match['score'],
            'metadata': match.get('metadata', {})
        })

    # Sort the results based on similarity scores
    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return results
