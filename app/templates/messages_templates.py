def get_welcome_message(name:str, date:str, hour:str):
    return f"""Hola {name}, 
¡Gracias por registrarte en acceptgo.co!

*AcceptGO* es todo lo que necesitas para dar el siguiente paso.... *mejores trabajos, becas y conexiones* 🌎.

Logramos lo que muchos creían imposible. Ayudamos a latinos a competir y obtener *oportunidades globales*...

👨‍💼 Mauricio - *CEO* de BNB Corp. en Paraguay 🇵🇾
👩‍💼 Valeria - Aceptada en pre-grado en *Stanford* 🇺🇸
👨‍💼 Mijail - Data Center Engineering Intern en *Amazon* Irlanda 🇮🇪
Conoce más casos en: https://bit.ly/470s7F1

Te invitamos a nuestro siguiente evento *100% gratuito*:
*Cómo ganar una beca completa en Europa?* 🤩 - Entrevista exclusiva a Valeria Calani

🗓 *{date}* a las {hour}

👉 Recibirás el enlace de *Zoom* horas antes del evento

Saludos,
_El Equipo de AcceptGO_
______________________
🛑 No respondas
Esta es una confirmación de registro

Si deseas participar en otros eventos *comunícate con AcceptGO al +59169959308*"""

def get_24_hour_reminder(event_time:str, zoom_url:str):
    return f"""*¡Mañana es el día!* 🥳
*¿Cómo ganar una beca completa en Europa 🌍?* - Entrevista exclusiva a Valeria Calani 😃

🗓️ Te esperamos *mañana* a las {event_time}.

🔗 Zoom: {zoom_url}

*Descubrirás:* 
✅ Cómo ingresó a una *Maestría en Reino Unido* 🇬🇧
✅ Cómo obtuvo una *beca completa* 💯 
✅ Consejos para *destacar internacionalmente*

Te esperamos con tu café online ☕ y tus mejores preguntas 😉.
______________________
🛑 No respondas este recordatorio

Si deseas *comunicarte con AcceptGO, escríbenos al +59169959308*"""

def get_beginning_reminder(zoom_url:str):
    return f"""🚨 *Ya empezamos* 🚨

🔗 *Zoom:* {zoom_url}
______________________
🛑 No respondas este recordatorio

*Comunícate con AcceptGO al +59169959308*"""



def get_12_hour_reminder(zoom_url:str):
    return f"""🚨 *Comenzamos a las 17:00 hrs* 🚨

🔗 *Zoom:* {zoom_url}

*Interacción en Vivo* 
¡Aprovecha para hablar directamente con Valeria, *ganadora de una beca completa para estudiar su maestría en* 🇬🇧!

👉 Ingresa con tu *cámara encendida y tu nombre*
______________________
🛑 No respondas este recordatorio

*Comunícate con AcceptGO al +59169959308*"""
