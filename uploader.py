# Upload new files with requests.post()
# response.status_code
# >>> 201

with open('newdata.csv') as fp:
    content = fp.read()

response = requests.post(
    '{}/files/newdata.csv'.format(API_URL), headers=headers, data=content
)