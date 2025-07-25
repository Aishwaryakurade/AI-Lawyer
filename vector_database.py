from langchain_community.document_loaders import PDFPlumberLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


#step 1 :upload and load raw pdfs

pdfs_directory='pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:   #"Upload the PDF file received from the frontend to the 'pdfs' directory."
        f.write(file.getbuffer())


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)   #extract text from pdf and return it in a document object 1 page=1 document(object)
    documents = loader.load()                
    return documents
    
  

file_path = 'universal_declaration_of_human_rights.pdf'
documents = load_pdf(file_path)
# print("PDF pages: ",len(documents))


#step 2 :create chunks

def create_chunks(documents): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chunks(documents)
# print("Chunks count: ", len(text_chunks))

#step 3: setup embedding model(using deepseek R1 with ollama)

ollama_model_name="deepseek-r1:1.5b"
def get_embedding_model(ollama_model_name):
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings


#Step 4: Index Documents ,Store embeddings in FAISS (vector store)

FAISS_DB_PATH="vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks, get_embedding_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)
















