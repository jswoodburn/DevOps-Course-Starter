class Item:
    def __init__(self, id, name, status, last_edited):
        self.id = id
        self.name = name
        self.status = status
        self.last_edited = last_edited

    @classmethod
    def from_document(cls, doc):
        return cls(doc['_id'], doc['name'], doc['status'], doc['last_edited'])