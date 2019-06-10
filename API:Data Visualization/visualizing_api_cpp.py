# A simple exercise to process an API response

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Storing a response from an API call
url = 'https://api.github.com/search/repositories?q=language:cpp&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Storing the API response in a variable
response_dict = r.json()
print("Total respositories:", response_dict['total_count'])
repo_dicts = response_dict['items']

# Filling two arrays with the desired information
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Creating a customized tooltip for each project using stars and descriptions
    description = repo_dict['description']
    if not description:
        description = "No description available."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'x_link': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# Creating a visualization of these arrays
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred C++ Projects on GitHb"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('cpp_repos.svg')
