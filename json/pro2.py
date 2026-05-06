import requests

# API URL (dummy free API)
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Convert JSON response to Python dictionary
data = response.json()

# Print the dictionary
print(data)

# Access specific values
print("Name:", data["name"])
print("Email:", data["email"])


# https://chatgpt.com/share/69f42973-ee88-83e8-8f6f-8bb3ddd30ec2