import requests
#// DOCBEGIN
r1 = requests.get('https://api.github.com/events')#// DOCLINE test
r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
r3 = requests.put('https://httpbin.org/put', data={'key': 'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')
r = [r1, r2, r3, r4, r5, r6]
for i in range(len(r)):
    print(f'r{i+1} status code: {r[i].text}')
#// DOCEND