import json
import requests
import time

url = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = url.json()

results = []

t1 = time.perf_counter()


for package in packages_json:
    package_name = package['name']
    package_desc = package['desc']
    
    url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    
    r = requests.get(url)
    package_json = r.json()
    
    # installs_30 = package_json['analytics']['install_on_request']["30d"][package_name]
    # installs_90 = package_json['analytics']['install_on_request']["90d"][package_name]
    installs_365 = package_json['analytics']['install_on_request']["365d"][package_name]
    
    # store data into a dictionary
    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '365d': installs_365
        }
    }
    
    # add all results into the list
    results.append(data)
    
    # add a sleep delay so we are not bombarding the websites with requests which is bad practice and unethical
    time.sleep(r.elapsed.total_seconds()) # delay the amount of time we needed to get the response so we give the same amount of time before the next response

    print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds')
    
    # test to see the first package only
    
    # print(package_name, package_desc, installs_30, installs_90, installs_365)
    
    
t2 = time.perf_counter()
print(f'Finished in {t2 - t1} seconds')
# packages_string = json.dumps(packages_json[0], indent=2)

# print(packages_string)

# package_json = r.json() # parses into response into a valid python dictionary

# package_string = json.dumps(package_json, indent=2) # for formatting purposes

# print(package_string)
# installs_30 = package_json['analytics']['install_on_request']["30d"][package_name]
# installs_90 = package_json['analytics']['install_on_request']["90d"][package_name]
# installs_365 = package_json['analytics']['install_on_request']["365d"][package_name]

# print(package_name, package_desc, installs_30, installs_90, installs_365)
# print(len(packages_json))

# put all info into a file
f = open('homebrew_analytics.json', 'w')
json.dump(results, fp=f)
f.close()

print(results)