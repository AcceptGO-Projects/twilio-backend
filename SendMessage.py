from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

numbers  = [
  '+59167016655',
  '+59170308805',
  '+59160508851',
  '+59169834275',
  '+59171576500',
  '+59176796607',
  '+59165608561',
  '+59165160110'
  ]

for number in numbers:
  message = client.messages.create(
    from_='whatsapp:+17542081136',
    body='Atento al webinnar en 5 minutos',
    to=f'whatsapp:{number}'
  )

  print(message.sid)