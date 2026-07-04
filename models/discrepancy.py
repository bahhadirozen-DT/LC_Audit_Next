from dataclasses import dataclass


@dataclass
class Discrepancy:

    document: str

    field: str

    status: str

    severity: str

    rule: str

    description: str

    mt700_value: str | None = None

    document_value: str | None = None

    recommendation: str = ""

    def to_dict(self):

        return self.__dict__
