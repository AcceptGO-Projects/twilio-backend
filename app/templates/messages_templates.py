def get_welcome_message(name:str, date:str, hour:str):
    return f"""Hola {name}, 
¡Gracias por registrarte en acceptgo.co!

*AcceptGO* es todo lo que necesitas para dar el siguiente paso.... *mejores trabajos, becas y conexiones* 🌎.

Logramos lo que muchos creían imposible. Ayudamos a latinos a competir y obtener *oportunidades globales*...

👨‍💼 Mauricio - *CEO* de BNB Corp. en Paraguay 🇵🇾
👩‍💼 Valeria - Aceptada en pre-grado en *Stanford* 🇺🇸
👨‍💼 Mijail - Data Center Engineering Intern en *Amazon* Irlanda 🇮🇪
Conoce más casos en: https://bit.ly/470s7F1

Te invitamos a la entrevista  de Jorge Luis Jaldín 👉 *sin costo*.

🗓️ {date} a las {hour} vía Zoom

Descubrirás: 
✅ Cómo obtuvo una beca en *MIT* de Cadena de Suministros y Logística 💯
✅ Cómo consiguió trabajo en una *multinacional* 💼
✅ Consejos para destacar internacionalmente

👉 Recibirás el enlace de *Zoom* horas antes del evento

Saludos,
_El Equipo de AcceptGO_
______________________
🛑 No respondas esta confirmación de registro

Si deseas *comunicarte con AcceptGO, escríbenos al +59169959308*"""

def get_24_hour_reminder(event_time:str, zoom_url:str):
    return f"""**¡Mañana es el día!** 🥳
**Evaluación de potencial - Webinar AcceptGO** 🚀

¿Quieres conocer cómo **sobresalir profesionalmente**? 😃🙌🏻

🗓 Te esperamos **mañana a las {event_time}**

🔗 Zoom: {zoom_url}

Descubrirás:
✅ ¿Por qué se pierden **becas**?
✅ Cómo mejorar tu **perfil profesional** para acceder a **oportunidades globales** 🌎
✅ Cómo usar **IA** 🤖 para **potenciar tu perfil**

👉 Si deseas una **evaluación personalizada en vivo** para trabajos y becas internacionales 🌎, ten listo tu **Currículum**.

Te esperamos con tu **café online** ☕ y tus mejores preguntas 😉.
______________________
🛑 No respondas este recordatorio

Si deseas **comunicarte con AcceptGO, escríbenos al +59169959308**"""

def get_12_hour_reminder(event_time:str, zoom_url:str):
    return f"""🚨 **Empezamos en una hora** 🚨

🗓 **{event_time}**

🔗 **Zoom**: {zoom_url}

**Interacción en Vivo**
¡Aprovecha para hablar directamente con Jonathan, **ganador de 5 becas, con experiencia laboral en 4 países** 🇺🇸🇵🇾🇲🇽🇧🇴!

👉 Ten tu **Currículum** a mano
👉 Ingresa con tu **cámara encendida y tu nombre**
______________________
🛑 No respondas este recordatorio

Si deseas **comunicarte con AcceptGO, escríbenos al +59169959308**"""

def get_beginning_reminder(zoom_url:str):
    return f"""🚨 **Ya empezamos** 🚨

🔗 **Zoom**: {zoom_url}

👉 Ten tu **Currículum** a mano
👉 Ingresa con tu **cámara encendida y tu nombre**
______________________
🛑 No respondas este recordatorio

Si deseas **comunicarte con AcceptGO, escríbenos al +59169959308**"""

