# HTTP for Humans
# get information from websites, post information, download images, redirects etc.
import requests

github_url = 'https://github.com/samincgs'
image_url = "https://avatars.githubusercontent.com/u/129024887?v=4"
httpbin_get = 'https://httpbin.org/get'
httpbin_post = 'https://httpbin.org/post'
httpbin_put = 'https://httpbin.org/basic-auth/sam/testing'


payload = {'page': 2, 'count': 25} # get request
payload = {'username': 'sam', 'password': 'testing'} # post request
r = requests.get(httpbin_post, params=payload) # get request where payload contains dictionaries of queries ?page=2&count=25
r = requests.post(httpbin_post, data=payload)

print(r.text) # returns the response object

print(r.content) # returns the response body in bytes

# get the contents methods/functions that the resposne object has
print(dir(r))

image_file = open('github_img.png', 'wb') # write byte mode
image_file.write(r.content) # turned bytes into an image
image_file.close()

# check the status code of the response
# 200s -> Success
# 300s -> Redirect
# 400s -> Client Errors (Unauthorization)
# 500s -> Server Errors (Site crashed)
print(r.status_code)

# to check if the request was successful or not (True or false)
print(r.ok)
print(r.url)
# print(r.text)
r_dict = r.json() # capture json dictionary in python dictionary
print(r_dict['form'])
# gives header information ex. server, content-type
# print(r.headers)

r = requests.get(httpbin_put, auth=('sam', 'testing'))
r = requests.get(httpbin_put, timeout=3)

print(r.text)