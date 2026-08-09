from dataclasses import dataclass

@dataclass(frozen=True)
class GoogleId:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("GoogleId must be a string.")
            
        clean_value = self.value.strip()

        if not clean_value:
            raise ValueError("GoogleId cannot be empty.")
        if len(clean_value) > 255:
            raise ValueError("GoogleId cannot exceed 255 characters.")

        object.__setattr__(self, 'value', clean_value)