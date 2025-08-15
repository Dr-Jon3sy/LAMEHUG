import os
from openai import OpenAI
from dotenv import load_dotenv

class LameException(Exception):
    pass

def get_commands(key):
    client = OpenAI(api_key=key)
    try:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="you are a windows system administrator",
            temperature=0.1,
            input="""Make a list of commands to create folder C:\lame\info and 
                     to gather computer information, hardware information, 
                     process and services information, networks information, 
                     AD domain information, to execute in one line and add each 
                     result to text file c:\Programdata\lame\info.txt. 
                     Return only commands, without markdown."""
        )
    except Exception as e:
        print(f"error: {e}")
        raise e
    
    if response.error is not None:
        raise LameException(response.error)
    return response.output_text
def main():
    load_dotenv()
    my_api_key = os.getenv('OPEN_API_KEY')
    if my_api_key is None:
        raise LameException("No Key")
    commands = "cmd.exe " + get_commands(my_api_key)
    print(commands)
if __name__ == "__main__":

    main()