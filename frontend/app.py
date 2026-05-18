import streamlit as st
import requests

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Saarthi AI",
    page_icon="🤖",
    layout="wide",
)

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #020617, #0f172a);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid rgba(255,255,255,0.08);
}

.block-container {
    padding-top: 2rem;
}

.big-title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.subtitle {
    color: #94a3b8;
    font-size: 18px;
}

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 20px;
}

.user-bubble {
    background: linear-gradient(135deg,#6366f1,#8b5cf6);
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 16px;
    color: white;
}

.ai-bubble {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 16px;
    color: white;
}

# .subject-card {
#     background: rgba(255,255,255,0.04);
#     border-radius: 24px;
#     padding: 36px 20px;
#     text-align: center;
#     border: 1px solid rgba(255,255,255,0.08);
#     min-height: 180px;

#     display:flex;
#     flex-direction:column;
#     align-items:center;
#     justify-content:center;

#     transition: 0.3s ease;
# }

# .subject-card:hover {
#     transform: translateY(-6px);
#     border: 1px solid rgba(99,102,241,0.5);
#     box-shadow: 0px 0px 30px rgba(99,102,241,0.25);
# }

# .subject-card h3 {
#     color: white;
# }

# .subject-card p {
#     color: #94a3b8;
# }

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🤖 Saarthi AI")
    st.caption("Offline AI Tutor")

    st.button("➕ New Chat")

    st.divider()

    st.markdown("### 📚 Subjects")
    st.markdown("- Science")
    st.markdown("- Math")
    st.markdown("- English")
    st.markdown("- General Knowledge")

    st.divider()

    st.markdown("### 🌐 Language")

    language = st.selectbox(
        "Language",
        ["English", "Hindi", "Kannada"],
        label_visibility="collapsed"
    )

    st.divider()

    st.success("🟢 Offline AI Active")

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class='big-title'>
        Hello, Samyuktha 👋
    </div>

    <div class='subtitle'>
        Your offline AI tutor powered by Gemma.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- SUBJECTS ----------------
# c1, c2, c3, c4 = st.columns(4)

# subjects = [
#     ("🧪", "Science"),
#     ("🧮", "Math"),
#     ("📖", "English"),
#     ("🌍", "GK")
# ]

# cols = [c1, c2, c3, c4]

# for col, subject in zip(cols, subjects):

#     with col:

#         st.markdown(
#             f"""
#             <div class='subject-card'>
#                 <div style='font-size:40px'>
#                     {subject[0]}
#                 </div>

#                 <h3>{subject[1]}</h3>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# ---------------- SUBJECTS ----------------
# c1, c2, c3, c4 = st.columns(4)

# subjects = [
#     ("🧪", "Science"),
#     ("🧮", "Math"),
#     ("📖", "English"),
#     ("🌍", "GK")
# ]

# for col, (icon, title) in zip([c1, c2, c3, c4], subjects):

#     with col:

#         st.markdown(
#             f"""
#             <div style="
#             background: rgba(255,255,255,0.04);
#             border-radius: 24px;
#             padding: 40px 20px;
#             text-align: center;
#             border: 1px solid rgba(255,255,255,0.08);
#             min-height: 180px;
#             ">

#             <div style="
#             font-size:48px;
#             margin-bottom:20px;
#             ">
#             {icon}
#             </div>

#             <div style="
#             font-size:28px;
#             font-weight:700;
#             color:white;
#             ">
#             {title}
#             </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# ---------------- SUBJECTS ----------------

c1, c2, c3, c4 = st.columns(4)

subjects = [
    ("🧪", "Science"),
    ("🧮", "Math"),
    ("📖", "English"),
    ("🌍", "GK")
]

for col, (icon, title) in zip([c1, c2, c3, c4], subjects):

    with col:

        st.markdown(f"""
<div style="
background: rgba(255,255,255,0.04);
border-radius: 24px;
padding: 30px 20px;
text-align: center;
border: 1px solid rgba(255,255,255,0.08);
margin-bottom:10px;
">

<div style="
font-size:48px;
margin-bottom:18px;
">
{icon}
</div>

<div style="
font-size:24px;
font-weight:700;
color:white;
margin-bottom:10px;
">
{title}
</div>

</div>
""", unsafe_allow_html=True)

        if st.button(f"Open {title}", key=title):

            starter_prompts = {
                "Science": "Explain gravity simply",
                "Math": "Teach me fractions",
                "English": "Improve my grammar",
                "GK": "Tell me about India"
            }

            question = starter_prompts[title]

            st.session_state.messages.append({
                "role": "user",
                "content": question
            })

            with st.spinner("Saarthi is thinking..."):

                try:

                    response = requests.post(
                        "http://localhost:8000/chat",
                        json={
                            "user_id": "user",
                            "question": question,
                            "language": language.lower(),
                            "level": "beginner"
                        },
                        timeout=120
                    )

                    answer = response.json()["answer"]

                except:

                    answer = "Backend not connected."

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            st.rerun()

st.write("")
st.write("")

# ---------------- CHAT ----------------
chat_container = st.container()

with chat_container:

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"""
                <div class='user-bubble'>
                    👦 {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class='ai-bubble'>
                    🤖 {msg['content']}
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- INPUT ----------------
question = st.chat_input("Ask Saarthi anything...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.spinner("Saarthi is thinking..."):

        try:
            # question = st.text_input("Ask your question")
            # if st.button("Ask"):
            # response = requests.post(
            #     "http://localhost:8000/chat",
            #     json={
            #         "user_id": "user_id",
            #         "question": question,
            #         "level": level,
            #         "language": language
            #     }
            # )
            # st.write("### Answer")
            # st.write(response.json()["answer"])

            response = requests.post(
                "http://localhost:8000/chat",
                json={
                    "user_id": "user",
                    "question": question,
                    "language": language.lower(),
                    "level": "beginner"
                },
                timeout=120
            )

            answer = response.json()["answer"]

        except:

            answer = """
            I could not connect to the local AI backend.
            Please ensure FastAPI + Ollama are running.
            """

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()