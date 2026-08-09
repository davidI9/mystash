from dataclasses import dataclass

@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("Email must be a string.")
        if not self.value:
            raise ValueError("Email cannot be empty.")

        parts = self.value.split("@")
        
        if len(parts) != 2:
            raise ValueError("Email must contain exactly one '@' symbol.")
            
        local_part = parts[0]
        domain_part = parts[1]
        
        if not local_part:
            raise ValueError("Email local part cannot be empty.")
            
        if "." not in domain_part:
            raise ValueError("Email domain must contain at least one '.' symbol.")