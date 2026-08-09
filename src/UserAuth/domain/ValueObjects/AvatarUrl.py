from dataclasses import dataclass

@dataclass(frozen=True)
class AvatarUrl:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("AvatarUrl must be a string.")
            
        clean_value = self.value.strip()

        if not clean_value:
            raise ValueError("AvatarUrl cannot be empty.")
        if len(clean_value) > 2048:
            raise ValueError("AvatarUrl cannot exceed 2048 characters.")
        if not (clean_value.startswith("http://") or clean_value.startswith("https://")):
            raise ValueError("AvatarUrl must start with http:// or https://")

        # 6. Guardamos el valor final limpio
        object.__setattr__(self, 'value', clean_value)