import csv
from app.services.twilio_services import send_custom_message

def send_messages_from_csv(csv_file, message):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            telefono = row['telefono']
            send_custom_message(telefono, message)

if __name__ == "__main__":
    message = "Hola, este es un mensaje de prueba."
    send_messages_from_csv('trucho.csv', message)
