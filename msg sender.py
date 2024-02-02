import requests
url="https://textflow-sms-api.p.rapidapi.com/send-sms"

payload={
    "phone_number":"+919653814628",
    "text":"HELLO THIS IS A TEST MESSAGE"
}
headers= {
    'content-type': 'application/json',
    'X-RapidAPI-Key': '611a646ea9msh052affb0d888dd5p173bf2jsnbe9763eb46ac',
    'X-RapidAPI-Host': 'textflow-sms-api.p.rapidapi.com'
  }

response = requests.post(url, json=payload,headers=headers)
print(response.json())