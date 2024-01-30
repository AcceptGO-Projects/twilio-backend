def get_welcome_message(name:str, date:str):
    return f"""Hola {name}, 
¡Gracias por registrarte en acceptgo.co!

AcceptGO es todo lo que necesitas para dar el siguiente paso.... mejores trabajos, becas y conexiones 🌎.

Logramos lo que muchos creían imposible. Ayudamos a latinos a competir y obtener oportunidades globales...

👨‍💼 Mauricio - CEO de BNB Corp. en Paraguay 🇵🇾
👩‍💼 Valeria - Aceptada en pre-grado en Stanford 🇺🇸
👨‍💼 Mijail - Data Center Engineering Intern en Amazon Irlanda 🇮🇪

Conoce más casos en: https://bit.ly/470s7F1

Te registraste al webinar para evaluar tu potencial para becas y trabajos por Zoom 👉 100% gratuito.

🗓 Te esperamos el {date} 20:00 hrs 🇧🇴

👉 Recibirás el enlace de Zoom horas antes del evento

Saludos,
Jonathan Capra, ganador de 5 becas, experiencia en 🇧🇴🇵🇾🇺🇸🇲🇽"""

def get_24_hour_reminder(event_time:str):
    return f"""¡Mañana es el día! 🥳
Evaluación de potencial - Webinar AcceptGO 🚀

¿Estás listo para conocer cómo sobresalir profesionalmente? 😃🙌🏻

🗓 Te esperamos mañana a las {event_time}

🔗 Te enviaremos el enlace de Zoom una hora antes del evento

👉 Si deseas una evaluación personalizada en vivo para trabajos y becas internacionales 🌎, ten lista una oración de tu Currículum de la que te sientas orgulloso.

Te esperamos con tu café online ☕ y tus mejores preguntas 😉.
_____
Ingresa con tu cámara encendida 📸 y tu nombre."""

def get_beginning_reminder(event_time:str, zoom_url:str):
    return f"""⚠ Ya empezamos ⚠
Evaluación de potencial - Webinar AcceptGO 🚀

🕤 {event_time}
🔗Enlace de Zoom: {zoom_url}

❌No debes estudiar ni prepararte para entrar a la sesión 
✔ Entra desde tu computadora para tener una mejor experiencia 

👉 Si deseas una evaluación personalizada en vivo para trabajos y becas internacionales 🌎, ten lista una oración de tu Currículum de la que te sientas orgulloso

________
Ingresa con tu cámara encendida 📸 y tu nombre"""



def get_12_hour_reminder(event_time:str, zoom_url:str):
    return f"""¡Hoy es el día! 🥳
Evaluación de potencial - Webinar AcceptGO 🚀

¿Estás listo para conocer cómo sobresalir profesionalmente? 😃🙌🏻

🗓 Te esperamos hoy a las {event_time}

🔗 Zoom: {zoom_url}

Descubrirás:
✅ ¿Por qué se pierden 225 becas?
✅ Cómo crear un perfil global para ganar becas
✅ Cómo usar IA 🤖 para potenciar tu perfil

🚨 Interacción en Vivo: Responderemos todas tus preguntas.
¡Aprovecha para hablar directamente con Jonathan, ganador de 5 becas, con experiencia laboral en 4 países 🇺🇸🇵🇾🇲🇽🇧🇴!

👉 Para una evaluación personalizada, trae una frase de tu CV que te represente.

______________________
👥 Ven con tu café ☕, energía positiva y cámara encendida 📸. 

¡Nos vemos pronto para transformar tu futuro profesional! 🌟"""
