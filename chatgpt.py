import openai 
openai.api_key = open("key.txt","r").read().strip('\n')
completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Calculate trajectory from earth to mars and implement in python code"}]
)
print(completion) 
print(completion.get("choices")[0].get("message"))
