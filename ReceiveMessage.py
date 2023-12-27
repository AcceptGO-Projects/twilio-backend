from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def reply_whatsapp():
    incoming_msg = request.form.get('Body')
    from_number = request.form.get('From')
    
    resp = MessagingResponse()
    
    # Aquí puedes agregar la lógica para guardar el número en tu base de datos

    if 'hola' in incoming_msg.lower():
        # Responde automáticamente
        resp.message("Gracias por contactarnos. Te informaremos sobre nuestros próximos webinars.")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
