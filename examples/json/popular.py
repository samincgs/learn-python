import json


def download_num(package):
    return package['analytics']['365d']

f = open('homebrew_analytics.json', 'r')
data = json.load(fp=f)
f.close()

formatted_data = json.dumps(data, indent=2)

# sort inplace since list
data.sort(key=download_num, reverse=True)

f = open('most_popular_packages.json', 'w')
json.dump(data, fp=f, indent=2)
f.close()

print(data)