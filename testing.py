import requests

#enter anyimage from Testimages
filename = 'Testimages/bitti.jpg'
url = 'http://127.0.0.1:5000/run'

#dictionary with image path
send_files = {'image':filename}

#post request to '/run' in app.py
output = requests.post(url, files=send_files)

#returning output obtained from home() in app.py
print(output.text)
