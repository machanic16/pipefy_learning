import requests
import json

# Pipefy API key
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

# Replace with your organization_id
organization_id = read_data('./organization_id.txt')

# Prepare the GraphQL query
query = f"""
query {{
  organization(id: {organization_id}) {{
    pipes {{
      id
      name
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
    # Parse the JSON response and print the pipe names and IDs
    data = json.loads(response.text)
    pipes = data["data"]["organization"]["pipes"]
    for pipe in pipes:
        print(f"{pipe['name']} (ID: {pipe['id']})")
else:
    print(f"Error: {response.status_code}")
