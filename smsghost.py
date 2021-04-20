import requests
Country_code = input("Enter the code without + ------>") #Enter the code only. For example 91 or 92. Do not add '+'
Mobile_Number = input("Enter the phone number ---------->")
Receiver = "+" + Country_code + Mobile_Number
Message = input("Enter message to be sent")

resp = requests.post('https://textbelt.com/text', {
  'phone': Receiver,
  'message': Message,
  'key': 'textbelt',
})
print(resp.json())
