from openai import OpenAI

shapes_client = OpenAI(
    api_key="ZFYWKN6HT862AA2HNGEJQHXLHMWICWSWOWO1XVXSDWE",
    base_url="https://api.shapes.inc/v1/",
)

response = shapes_client.chat.completions.create(
    model="shapesinc/atri-a6pm",
    messages=[
        {"role": "user", "content": "Lagi  ngapain malam ini"}
    ]
)

print(response)