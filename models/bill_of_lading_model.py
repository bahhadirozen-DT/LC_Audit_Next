from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BillOfLadingModel:

    bl_number: Optional[str] = None
    shipper: Optional[str] = None
    consignee: Optional[str] = None
    notify_party: Optional[str] = None

    vessel: Optional[str] = None

    port_of_loading: Optional[str] = None
    port_of_discharge: Optional[str] = None

    goods_description: Optional[str] = None

    packages: Optional[str] = None

    gross_weight: Optional[str] = None

    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_dict(self):
        return self.__dict__
