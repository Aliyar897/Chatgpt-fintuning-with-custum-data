import os
import sys
import constant
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.chat_models import ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator

os.environ['OPENAI_API_KEY'] = constant.APIKEY

query = sys.argv[1]

print('this is the question i am answering to: ',query)
loader = TextLoader('data.txt')
# loader = DirectoryLoader('text_data')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))