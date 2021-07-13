import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pypinyin


def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
        return s


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code: ', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']  # 字典列表
print('Repositories returned:', len(repo_dicts))
names, stars = [], []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'xlink': repo_dict['html_url'],
        #'label': repo_dict['description']
    }
    if repo_dict['description'] == None:
        plot_dict['label'] = 'No description'
    else:
        plot_dict['label'] = repo_dict['description']
    plot_dicts.append(plot_dict)
# 可视化
#print(plot_dicts)
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()  # 创建一个Config类的实例
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 20  # 突出主标签
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)  # 设置样式，不显示图例
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

# chart.add('', stars)
chart.add('', plot_dicts, encodings='utf-8')
chart.render_to_file('python_repos_test.svg')

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 具体信息
# print('\nSelect information about first repository:')
# for repo_dict in repo_dicts:
#     print("Name: ", repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Update:', repo_dict['updated_at'])
#     print("Description:", repo_dict['description'])
