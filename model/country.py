from dataclasses import dataclass

@dataclass
class Country:
    stato: str
    statocod: int


    def __hash__(self):
        return hash(self.stato)

    def __eq__(self, other):
        return self.stato == other.stato

    def __str__(self):
        return f"{self.stato} ({self.statocod})"