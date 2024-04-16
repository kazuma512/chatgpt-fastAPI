# chatgpt-fastAPI

## Introduction
This is a simple API project that calls the ChatGPT API using FastAPI.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
async def ask_gpt(input_text):
    completion = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input_text}])
    return completion.choices[0].message.content
```
