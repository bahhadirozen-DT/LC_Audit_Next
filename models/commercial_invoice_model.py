from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class CommercialInvoiceModel:

    invoice_number: Optional[str] = None
    invoice_date: Optional[str] = None

    seller: Optional[str] = None
    buyer: Optional[str] = None

    currency: Optional[str] = None
    total_amount: Optional[float] = None

    incoterm: Optional[str] = None

    goods: List[Dict] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)
    originals: int | None = None
    copies: int | None = None
    errors: List[str] = field(default_factory=list)

    def to_dict(self):
        return self.__dict__

    def validate(self):
        return (
            self.invoice_number is not None
            and self.seller is not None
            and self.buyer is not None
        )