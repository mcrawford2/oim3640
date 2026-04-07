from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

topic = input("Enter a business question: ")
if not topic:
    topic = "Explain SWOT analysis with a real company example."

system_prompt = (
    "You are a helpful AI tutor for business students. "
    "Teach clearly, use practical business examples, and break down "
    "complex ideas into simple steps. When useful, include frameworks "
    "like SWOT, Porter's Five Forces, the 4 Ps, and basic finance concepts."
)

first_user_message = (
    "Help me with this business question as a tutor. "
    "Explain in plain language and include a short example: "
    f"{topic}"
)

conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": first_user_message},
]

response = client.responses.create(
    model="gpt-5.4",
    input=conversation
)

first_reply = response.output_text.strip()
print(first_reply)
conversation.append({"role": "assistant", "content": first_reply})

while True:
    user_message = input("You: ").strip()
    if user_message.lower() in {"exit", "quit"}:
        print("GBot: Thanks for chatting! Goodbye!")
        break
    if not user_message:
        continue

    conversation.append({"role": "user", "content": user_message})

    response = client.responses.create(
        model="gpt-5.4",
        input=conversation
    )

    bot_message = response.output_text.strip()
    print(f"GBot: {bot_message}")
    conversation.append({"role": "assistant", "content": bot_message})
    



