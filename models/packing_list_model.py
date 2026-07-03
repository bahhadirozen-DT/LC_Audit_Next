from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PackingListModel:

    packing_list_no: Optional[str] = None

    exporter: Optional[str] = None
    importer: Optional[str] = None

    packages: Optional[str] = None

    gross_weight: Optional[str] = None
    net_weight: Optional[str] = None

    goods_description: Optional[str] = None

    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_dict(self):
        return self.__dict__
