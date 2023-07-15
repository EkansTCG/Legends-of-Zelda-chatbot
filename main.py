import os
import openai


my_secret = os.environ['SECRET']

openai.api_key = str(my_secret)

end_program = False

while not end_program:
  get_input = input("Enter a prompt: ")
  if(get_input == "exit"):
    print("exiting the chat system")
  else:
    system_data = [
      {"role": "system", "content": "you are an asssistant that only answers Legends of Zelda questions."}, 
      {"role": "user", "content": get_input}
    ]
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo", 
      messages = system_data
    )
    assistant_response = response.choices[0].message.content
    system_data.append({"role": "assistant", "content": assistant_response})
    print ("Response: " + assistant_response)