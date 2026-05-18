
user_memory = {}

def store_interaction(user_id, question):
    if user_id not in user_memory:
        user_memory[user_id] = []
    user_memory[user_id].append(question)

def get_history(user_id):
    return user_memory.get(user_id, [])
