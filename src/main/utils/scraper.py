from langchain_community.document_loaders import WebBaseLoader

url = "https://www.veritas.edu.ng/"
loader = WebBaseLoader(url)

data = loader.load()

print(data)