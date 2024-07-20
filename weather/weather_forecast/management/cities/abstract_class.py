from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load_data(self) -> list[dict[str, list[str]]]:
        """Load data from the source."""
        pass
