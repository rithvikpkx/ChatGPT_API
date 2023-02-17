import openai

key = open("API_Key.txt")
openai.api_key = key.read()

prompt = input("Prompt: ")

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens = 2048)
print(response)
