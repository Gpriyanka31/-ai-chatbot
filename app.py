from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

chat_history = "You are a Data Analyst assistant. Answer in short bullet points.\n"

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history += f"You: {user_input}\n"

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=chat_history
    )

    ai_reply = response.text
    print("AI:", ai_reply)

    chat_history += f"AI: {ai_reply}\n"