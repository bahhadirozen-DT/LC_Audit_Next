"""
LC_Audit_Next - Core Architecture
Module: models.mt700_model

This module defines the MT700Model dataclass, representing a strongly typed,
structured representation of an ICC SWIFT MT700 (Issue of a Documentary Credit)
document. It inherits from BaseDocument and enforces type discipline for downstream
validation and audit engines.
"""

from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union
from models.base_document import BaseDocument


@dataclass
class MT700Model(BaseDocument):
    """Strongly typed data model for SWIFT MT700 Documentary Credits.

    Serves as an isolated, validated data container mapping raw fields to their
    normalized domain types (e.g., structured currency dicts, native dates, 
    and document matrices).
    """
    # SWIFT MT700 Raw Fields
    field20: Optional[str] = None
    field23: Optional[str] = None
    field27: Optional[str] = None
    field31C: Optional[Union[date, str]] = None
    field31D: Optional[Union[date, str]] = None
    field32B: Dict[str, Any] = field(default_factory=dict)
    field39A: Optional[Union[float, str]] = None
    field39B: Optional[Union[float, str]] = None
    field40A: Optional[str] = None
    field41A: Optional[str] = None
    field42C: Optional[str] = None
    field43P: Optional[str] = None
    field43T: Optional[str] = None
    field44A: Optional[str] = None
    field44B: Optional[str] = None
    field44C: Optional[Union[date, str]] = None
    field44D: Optional[Union[date, str]] = None
    field45A: Dict[str, Any] = field(default_factory=dict)
    field46A: Dict[str, Any] = field(default_factory=dict)
    field47A: Optional[str] = None
    field48: Optional[Union[int, str]] = None
    field49: Optional[str] = None
    field53A: Optional[str] = None
    field57A: Optional[str] = None
    field71B: List[str] = field(default_factory=list)
    field71D: Optional[str] = None
    field78: Optional[str] = None

    # Normalized Downstream Business Fields
    lc_number: Optional[str] = None
    applicant: Optional[str] = None
    beneficiary: Optional[str] = None
    issuing_bank: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    expiry_date: Optional[date] = None
    latest_shipment_date: Optional[date] = None
    incoterm: Optional[str] = None
    required_documents: List[str] = field(default_factory=list)

    # Parser Diagnostic Fields
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    parsing_confidence: float = 1.0

    def validate(self) -> bool:
        """Validates inheritance specifications and specific MT700 structural rules.

        Returns:
            bool: True if the model matches structural and type requirements.

        Raises:
            TypeError: If fields fail structural type assertions.
            ValueError: If core validation limits are breached.
        """
        # Execute upstream BaseDocument assertions first
        super().validate()

        # Complex dictionary structures verification
        if not isinstance(self.field32B, dict):
            raise TypeError("field32B must be a dictionary.")
        if not isinstance(self.field45A, dict):
            raise TypeError("field45A must be a dictionary.")
        if not isinstance(self.field46A, dict):
            raise TypeError("field46A must be a dictionary.")
        if not isinstance(self.field71B, list):
            raise TypeError("field71B must be a list of strings.")

        # Check numeric conversions within field32B if populated
        if self.field32B and "amount" in self.field32B:
            if not isinstance(self.field32B["amount"], (int, float)):
                raise TypeError("field32B['amount'] must be a numeric value.")

        # Check array types for field46A parsed documents
        if self.field46A and "documents" in self.field46A:
            if not isinstance(self.field46A["documents"], list):
                raise TypeError("field46A['documents'] must be a list.")

        # Business Fields Validation
        if self.lc_number is not None and not isinstance(self.lc_number, str):
            raise TypeError("lc_number must be a string.")
        if self.applicant is not None and not isinstance(self.applicant, str):
            raise TypeError("applicant must be a string.")
        if self.beneficiary is not None and not isinstance(self.beneficiary, str):
            raise TypeError("beneficiary must be a string.")
        if self.issuing_bank is not None and not isinstance(self.issuing_bank, str):
            raise TypeError("issuing_bank must be a string.")
        if self.currency is not None and not isinstance(self.currency, str):
            raise TypeError("currency must be a string.")
        if self.amount is not None and not isinstance(self.amount, (int, float)):
            raise TypeError("amount must be a float or integer.")
        if self.expiry_date is not None and not isinstance(self.expiry_date, date):
            raise TypeError("expiry_date must be a datetime.date object.")
        if self.latest_shipment_date is not None and not isinstance(self.latest_shipment_date, date):
            raise TypeError("latest_shipment_date must be a datetime.date object.")
        if self.incoterm is not None and not isinstance(self.incoterm, str):
            raise TypeError("incoterm must be a string.")
        if not isinstance(self.required_documents, list):
            raise TypeError("required_documents must be a list.")

        # Diagnostics Validation
        if not isinstance(self.warnings, list):
            raise TypeError("warnings must be a list of strings.")
        if not isinstance(self.errors, list):
            raise TypeError("errors must be a list of strings.")
        if not isinstance(self.parsing_confidence, (int, float)):
            raise TypeError("parsing_confidence must be a float or integer.")
        if not (0.0 <= self.parsing_confidence <= 1.0):
            raise ValueError("parsing_confidence score must be between 0.0 and 1.0.")

        return True

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the MT700Model instance into a standard JSON-ready dictionary.

        Handles ISO serialization protocols for dates and timestamps.

        Returns:
            Dict[str, Any]: Native dictionary mapping of the MT700 parameters.
        """
        data = asdict(self)
        
        # Base class serialization mapping override
        data["created_at"] = self.created_at.isoformat()
        
        # Native date type serialization logic for raw SWIFT fields
        date_fields = ["field31C", "field31D", "field44C", "field44D", "expiry_date", "latest_shipment_date"]
        for field_name in date_fields:
            value = getattr(self, field_name)
            if isinstance(value, date):
                data[field_name] = value.isoformat()
                
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MT700Model":
        """Instantiates an MT700Model object from a raw input mapping dictionary.

        Args:
            data: Key-value parameters mapping to MT700 model definitions.

        Returns:
            MT700Model: A strongly typed instance containing parsed components.
        """
        processed_data = data.copy()

        # Timestamp reconstruction
        created_at_val = processed_data.get("created_at")
        if isinstance(created_at_val, str):
            processed_data["created_at"] = datetime.fromisoformat(created_at_val)
        elif created_at_val is None:
            processed_data.pop("created_at", None)

        # Datetime.date reconstruction safely falling back to raw string on error
        date_fields = ["field31C", "field31D", "field44C", "field44D", "expiry_date", "latest_shipment_date"]
        for field_name in date_fields:
            val = processed_data.get(field_name)
            if isinstance(val, str):
                try:
                    processed_data[field_name] = date.fromisoformat(val)
                except ValueError:
                    pass  # Retain raw formatting state

        return cls(**processed_data)