from agno.models.groq import Groq
from agno.models.message import Message

# Setup - Model
from dotenv import load_dotenv

load_dotenv()

model = Groq(id="llama-3.1-8b-instant")

msg = Message(
    role="user",
    content="Hello, how are you doing today?",
)

response = model.invoke([msg])
response.choices[0].message.content
