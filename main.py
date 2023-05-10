import openai

with open('.token', 'r') as token_file:
  api_key = token_file.read()

# Set up the OpenAI API client
openai.api_key = api_key

file_name = 'report.text'

with open(file_name, 'r') as file:
    text = file.read()

# Define a function to interact with GPT-4 (ChatGPT) using questions
def ask_question(question, text, conversation_history=[]):
    conversation_history.append(f"User: {question}")
    prompt = f"The following text is a report:\n{text}\n"
    for message in conversation_history:
        prompt += f"{message}\n"
    prompt += "Chatbot:"

    response = openai.Completion.create(
        engine="text-davinci-002",  # or "text-davinci-004" for GPT-4
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    conversation_history.append(f"Chatbot: {answer}")
    return answer

# Interactive questioning
conversation_history = []
while True:
    question = input("Enter your question: ")
    if question.lower() in ["quit", "exit", "bye"]:
        break
    answer = ask_question(question, text, conversation_history)
    print(f"Answer: {answer}\n\n")
