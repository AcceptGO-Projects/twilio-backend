from app.repositories.message_repository import MessageRepository

class MessageService:
    def __init__(self, message_repo: MessageRepository):
        self.message_repo = message_repo

    def get_all_messages(self):
        return self.message_repo.get_messages()
    
    def get_message_by_id(self, message_id: int):
        return self.message_repo.get_message_by_id(message_id)
