"""
LC_Audit_Next - Core Architecture
Module: models.base_document

This module defines the BaseDocument dataclass, which serves as the foundational 
data model for all international trade and credit letter (L/C) documents within 
the system (e.g., Bills of Lading, Commercial Invoices, Packing Lists).
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass
class BaseDocument:
    """
    Parent data model representing a standardized trade document.
    
    Acts as a pure data container holding raw extracted content, structural 
    metadata, and ingestion metrics. It contains no processing, OCR, or 
    parsing logic.
    """
    document_type: str
    document_name: str
    source_file: str
    raw_text: str
    language: str = "en"
    confidence: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def validate(self) -> bool:
        """
        Validates the integrity and type correctness of the document fields.

        Returns:
            bool: True if the document instance passes all structural checks.
            
        Raises:
            ValueError: If string fields are empty or confidence is out of bounds.
            TypeError: If fields do not match their expected types.
        """
        # Type validations
        if not isinstance(self.document_type, str):
            raise TypeError("document_type must be a string.")
        if not isinstance(self.document_name, str):
            raise TypeError("document_name must be a string.")
        if not isinstance(self.source_file, str):
            raise TypeError("source_file must be a string.")
        if not isinstance(self.raw_text, str):
            raise TypeError("raw_text must be a string.")
        if not isinstance(self.language, str):
            raise TypeError("language must be a string.")
        if not isinstance(self.confidence, (int, float)):
            raise TypeError("confidence must be a float or integer.")
        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary.")
        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be a datetime object.")

        # Value validations
        if not self.document_type.strip():
            raise ValueError("document_type cannot be empty or whitespace.")
        if not self.document_name.strip():
            raise ValueError("document_name cannot be empty or whitespace.")
        if not self.source_file.strip():
            raise ValueError("source_file cannot be empty or whitespace.")
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError("confidence score must be between 0.0 and 1.0.")

        return True

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the BaseDocument instance into a standard dictionary format.
        Handles ISO format serialization for datetime objects.

        Returns:
            Dict[str, Any]: Dictionary representation of the model.
        """
        data = asdict(self)
        data["created_at"] = self.created_at.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseDocument":
        """
        Instantiates a BaseDocument object from a dictionary.
        Safely parses ISO format datetime strings back to datetime objects.

        Args:
            data (Dict[str, Any]): Dictionary containing document fields.

        Returns:
            BaseDocument: A populated instance of the base document model.
        """
        # Shallow copy to avoid mutating the original input dictionary
        processed_data = data.copy()
        
        created_at_val = processed_data.get("created_at")
        if isinstance(created_at_val, str):
            processed_data["created_at"] = datetime.fromisoformat(created_at_val)
        elif created_at_val is None:
            # Pop it so the dataclass field factory generates the timestamp
            processed_data.pop("created_at", None)

        return cls(**processed_data)