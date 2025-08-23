class VideogameDescription:
    def __init__(self, description: str):
        if not isinstance(description, str):
            raise TypeError("The description must be a string")

        normalized = description.strip()

        if not normalized:
            raise ValueError("Description can't be empty")

        if len(normalized) < 3:
            raise ValueError("Description must have at least 3 characters")

        if len(normalized) > 500:
            raise ValueError("Description can't surpass the 500 characters cap.")

        self._description = normalized

    def __eq__(self, other):
        return isinstance(other, VideogameDescription) and self._description == other._description

    def __str__(self):
        return str(self._description)

    def __repr__(self):
        return str(self._description)