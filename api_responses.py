# A simple exercise to process an API response

import requests

# Storing a response from an API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Storing the API response in a variable
response_dict = r.json()
print("Total respositories:", response_dict['total_count'])

# Processing results
print(response_dict.keys())

# Exploring information about the repositories
repo_dicts = response_dict['items']
print("Respositories returned:", len(repo_dicts))

# Exploring the first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Printing specific information from the first repository
print("\nSelected information about the first repository:")
print("Name:", repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("Repository:", repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print("Updated:", repo_dict['updated_at'])
print("Description:", repo_dict['description'])
