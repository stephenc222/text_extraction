# Text Extraction with OpenAI

## Installation

Need to install `openai`, `pytesseract` (and the tesseract binary) and `PIL`

## Setup

Need to load your openai api key as `OPENAI_API_KEY` into the environment from which you run the `text_extraction.py` Python script

## How to run

Once packages are installed and the environment set with your openai api key, just run the script like follow:

`python text_extraction.py example_bill.webp`.

Assuming everything works as expected, you should see a fully valid JSON object printed to the terminal, something like this (from `example_bill.webp`):

```json
{
  "accountNumber": "1234567890-1",
  "statementDate": "09/07/2019",
  "serviceAddress": "12345 ENERGY CT",
  "amountDue": "$88.14",
  "dueDate": "09/28/2019",
  "electricDeliveryCharges": "$55.66",
  "electricGenerationCharges": "$32.48"
}
```
