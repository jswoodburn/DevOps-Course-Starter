class Item:
    def __init__(self, id, name, status, list_id):
        self.id = id
        self.name = name
        self.status = status
        self.list_id = list_id
        
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'], card['idList'])