class MongoUrl:
    def __init__(self, url: str):
        if not url.startswith("mongodb://") and not url.startswith("mongodb+srv://"):
            raise ValueError("Invalid MongoDB URL")
        self.url = url

    def __str__(self):
        return self.url