# Description: 

import chromadb

DB_NAME = 'cv_collection'

class DBClient:

  chroma_client = chromadb.PersistentClient('./chroma_db')

  def __init__(self, db_name=DB_NAME):
    ''' Initialize the DB client '''
    self.collection = self.chroma_client.get_or_create_collection(name=db_name)


  def add(self, document, document_id, filename):
    ''' Add document to the collection '''
    self.collection.upsert(
      documents=[document], 
      ids=[document_id],
      metadatas=[{'filename': filename}]
      )
    

    
