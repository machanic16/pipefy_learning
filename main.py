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

# Replace with your pipe_id and fields you want to fetch
pipe_id = "303157524"
# pipe_id = read_data('./organization_id.txt')
fields_to_fetch = ["email"]

# Prepare the GraphQL query
query = '''
query {
  pipe(id: 303157524) {
    id
    uuid
    name
    cards_count
    organization {
      id
    }
    members{
      role_name
      user{
        id
        email
      }
    }
    phases {
      id
      name
    }
    start_form_fields {
      id
      label
    }
    labels{
      id
      name
      color
    }
    webhooks {
      name
      id
    }
  }
}
'''

# See cards ids from pipe
query = ''' {
  pipe(id: 303157524) {
    phases {
      cards{
      edges{
        node{
          id
        }
      }
    }
    }
    }
  }'''

# Query a card
query = '''{
  card(id: 671622402) {
    fields {
      name
      value
      filled_at
    }
  }
}'''

# # See cards ids from pipe
query = ''' {
  pipe(id: 303157524) {
    phases {
      cards{
      edges{
        node{
            id
            fields {
                name
                value
            }
        }
      }
    }
    }
    }
  }'''


# Send the request to the Pipefy API
response = requests.post(
    "https://api.pipefy.com/graphql",
    json={"query": query},
    headers=headers,
)

# Modify pipe
# q_2  = '''mutation {
#   updatePipe(input: {id:303157524 , name: "New pipe name", public: true, anyone_can_create_card: true, color: green}) {
#     pipe {
#       id
#     }
#   }
# }'''

# response = requests.post(
#     "https://api.pipefy.com/graphql",
#     json={"query": q_2},
#     headers=headers,
# )



# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and print the data
    data = json.loads(response.text)

    print(data["data"]["pipe"])
    # phases = data["data"]["pipe"]
    # for card in phases:
    #     print(card)
    #     # print(card["cards"]["edges"])
    #     print()
    #     print()
    #     print('---')
else:
    print(f"Error: {response.status_code}")

