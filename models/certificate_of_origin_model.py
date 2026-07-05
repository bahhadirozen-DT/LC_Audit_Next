from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CertificateOfOriginModel:

    certificate_number: Optional[str] = None

    exporter: Optional[str] = None
    consignee: Optional[str] = None

    country_of_origin: Optional[str] = None
    country_of_destination: Optional[str] = None

    goods_description: Optional[str] = None

    warnings: List[str] = field(default_factory=list)
    originals: int | None = None
    copies: int | None = None
    errors: List[str] = field(default_factory=list)

    def to_dict(self):
        return self.__dict__