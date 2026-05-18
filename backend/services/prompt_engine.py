
def build_prompt(question, level, language, context, history):
    return f'''
You are a friendly AI tutor for rural students.

Respond in: {language}
Student Level: {level}

Previous Questions:
{history}

Use the context below to answer accurately.

Context:
{context}

Explain simply using real-life examples.

Question: {question}

Answer:
'''
