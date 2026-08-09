import re
from dataclasses import dataclass

@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("UserName must be a string.")
            
        clean_value = self.value.strip()

        if len(clean_value) < 3:
            raise ValueError("UserName must be at least 3 characters long.")
        if len(clean_value) > 30:
            raise ValueError("UserName cannot be longer than 30 characters.")
        if not re.match(r"^[a-zA-Z0-9_]+$", clean_value):
            raise ValueError("UserName can only contain letters, numbers, and underscores.")

        object.__setattr__(self, 'value', clean_value.lower())