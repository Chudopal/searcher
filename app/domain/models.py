from dataclasses import dataclass
from abc import ABC
from typing import Dict


class Model(ABC):
    """Main interface for models."""


@dataclass
class Word(Model):
    label: str
    weight: float

    def __hash__(self) -> int:
        return hash(self.label)

    def __dict__(self) -> Dict:
        return dict(
            label=self.label,
            weight=self.weight
        )

    @classmethod
    def create(cls, label: str, weight: float):
        return cls(label=label, weight=weight)


@dataclass
class Document(Model):
    link: str

    def __hash__(self) -> int:
        return hash(self.link)

    def __dict__(self) -> Dict:
        return dict(
            link=self.link
        )

    @classmethod
    def create(cls, link: str):
        return cls(link=link)

@dataclass
class WordDocumentAssotiation(Model):
    document: Document
    coefficient: float
    word: Word

    @classmethod
    def create(
        cls,
        coefficient,
        label: str,
        weight: float,
        link: str
    ):
        return cls(
            word=Word(label=label, weight=weight),
            document=Document(link=link),
            coefficient=coefficient
        )