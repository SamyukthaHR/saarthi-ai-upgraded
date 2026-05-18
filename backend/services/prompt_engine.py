
def build_prompt(question, level, language, history):
    return f'''
You are a friendly AI tutor for rural students.

Respond in: {language}
Student Level: {level}

Previous Questions:
{history}



Explain simply using real-life examples.

Question: {question}

Answer:
'''
