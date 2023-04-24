class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_document(cls, doc):
        return cls(doc['_id'], doc['name'], doc['status'])