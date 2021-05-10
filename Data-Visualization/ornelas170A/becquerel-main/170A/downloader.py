# And download them with requests.get()
# response.text
# >>> '1,Joe Bloggs,27\n'

response = requests.get(
    '{}/files/newdata.csv'.format(API_URL), headers=headers
)
