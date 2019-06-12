# A program expanding on hacker_news.py to visualize the information obtained in this exercise

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

# Store the response from the initial API call
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Processing information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Creating a separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
print(submission_dicts)

# THis block only necessary if you want to ensure that the data is reading out properly
# for submission_dict in submission_dicts:
#    print("\nTitle:", submission_dict['title'])
#    print("Discussion link:", submission_dict['link'])
#    print("Comments:", submission_dict['comments'])

names, plot_dicts = [], []
for repo_dict in submission_dicts:
    names.append(repo_dict['title'])

    # Creating a customized tooltip for each project using comments and titles
    plot_dict = {
        'value': repo_dict['comments'],
        'label': repo_dict['title'],
        'x_link': {'href': repo_dict['link']}
    }
    plot_dicts.append(plot_dict)

# Defining the style parameters for the graph
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
chart.force_uri_protocol = 'http'
chart.title = "Most Popular Articles on Hacker-News"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('hacker_news.svg')
