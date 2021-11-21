from dataclasses import dataclass
from abc import ABC
from typing import Dict


class Model(ABC):
    """Main interface for models."""


@dataclass
class Word(Model):
    id: int
    label: str
    weight: float

    def __hash__(self) -> int:
        return hash(self.label)

    def __dict__(self) -> Dict:
        return dict(
            label=self.label,
            weight=self.weight
        )


@dataclass
class Document(Model):
    id: int
    link: str

    def __hash__(self) -> int:
        return hash(self.link)

    def __dict__(self) -> Dict:
        return dict(
            link=self.link
        )

@dataclass
class WordDocumentAssotiation(Model):
    word_id: int
    document_id: int
    coefficient: float