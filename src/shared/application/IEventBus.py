# src/shared/application/ports/IEventBus.py
from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.DomainEvent import DomainEvent

class IEventBus(ABC):
    @abstractmethod
    def publish(self, events: List[DomainEvent]) -> None:
        pass