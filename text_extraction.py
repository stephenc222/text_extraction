from PIL import Image
import os
import openai
import sys
import pytesseract


# Set up OpenAI API key and chat log filename
openai.api_key = os.environ["OPENAI_API_KEY"]

MAX_TOKENS = 1500
COMPLETION_TOKENS = 2500
MODEL = "gpt-3.5-turbo"


def get_response(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        max_tokens=COMPLETION_TOKENS,
        n=1,
        stop="\nUser:",
        temperature=0.7,
    )
    return response.choices[0].message


# (pytesseract.image_to_string(Image.open('bill_6.webp')))

def text_extraction(filename: str):
  if not filename:
    print("filename is required")
    sys.exit(1)
  image_text = pytesseract.image_to_string(Image.open(filename))
  messages=[{
    "role": "user",
    "content": f"Please write me a JSON object that contains the relevant information from the following text, and please simplify the key names and reduce the object down to the most critical information:\n{image_text}"
  }]
  response = get_response(messages=messages)
  print(response.content)

if __name__ == "__main__":
    filename=sys.argv[1]
    text_extraction(filename=filename)