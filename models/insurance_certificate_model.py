from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class InsuranceCertificateModel:

    certificate_number: Optional[str] = None

    insured: Optional[str] = None

    beneficiary: Optional[str] = None

    policy_number: Optional[str] = None

    insurance_company: Optional[str] = None

    insured_amount: Optional[str] = None

    currency: Optional[str] = None

    warnings: List[str] = field(default_factory=list)
    originals: int | None = None
    copies: int | None = None
    errors: List[str] = field(default_factory=list)

    def to_dict(self):
        return self.__dict__