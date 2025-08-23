class RecordTitle:
    def __init__(self, title: str):
        if not isinstance(title, str):
            raise TypeError("RecordTitle debe ser un string")

        normalized = title.strip()

        if not normalized:
            raise ValueError("RecordTitle can't be empty")

        if len(normalized) < 3:
            raise ValueError("RecordTitle must have at least 3 characters")

        if len(normalized) > 255:
            raise ValueError("RecordTitle can't surpass the 255 characters cap.")

        self._title = normalized

    def __eq__(self, other):
        return isinstance(other, RecordTitle) and self._title == other._title

    def __repr__(self):
        return str(self._title)
    
    def __str__(self):
        return str(self._title)
