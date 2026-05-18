
def load_document():
    try:
        with open("data/science.txt", "r") as f:
            return f.read()
    except:
        return ""

def retrieve_context(question):
    doc = load_document()
    return doc[:1000]
