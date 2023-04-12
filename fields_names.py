import requests
import json

# Replace with your Pipefy API key
def read_data(file_path):
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

API_KEY =  read_data('./pipefy_api_key.txt')

# Set up the headers for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

# Replace with your pipe_id
pipe_id = "303157524"

# Prepare the GraphQL query
query = f"""
query {{
  pipe(id: {pipe_id}) {{
    fields {{
      id
      name
      internal_id
    }}
  }}
}}
"""

# Send the request to the Pipefy API
response = requests.post(
    "https://api.pipefy.com/graphql",
    json={"query": query},
    headers=headers,
)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and print the field names
    data = json.loads(response.text)
    print(data)
    # fields = data["data"]["pipe"]["fields"]
    # for field in fields:
    #     print(f"Field Name: {field['name']}, Field ID: {field['id']}, Internal ID: {field['internal_id']}")
else:
    print(f"Error: {response.status_code}")
