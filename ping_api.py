import requests

GRAPHQL_ENDPOINT = "https://upload-simple-backend.onrender.com/query"

def ping_videos():
    query = """
    query {
      videos {
        id
        title
        description
        duration
        thumbnailUrl
        videoUrl
        createdAt
        updatedAt
      }
    }
    """
    response = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
    if response.status_code == 200:
        print("Successfully pinged the GraphQL API")
    else:
        print("Failed to ping the GraphQL API", response.status_code, response.text)

if __name__ == "__main__":
    ping_videos()
