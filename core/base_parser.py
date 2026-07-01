"""
LC_Audit_Next - Core Architecture
Module: core.base_parser

This module defines the BaseParser abstract class, which serves as the foundational
interface and utility layer for all document-specific parsers in the system.
"""

from abc import ABC, abstractmethod
import os
from pathlib import Path
from typing import Set, Union


class BaseParser(ABC):
    """Abstract Base Class for all document parsers.

    Provides common text preprocessing, sanitization, and validation utilities
    that every specialized parser requires. It enforces a strict interface
    without implementing specific business, OCR, or regex parsing logic.

    Attributes:
        parser_name (str): The unique identifier for the specific parser.
        supported_extensions (Set[str]): Lowercase file extensions (e.g., {'.txt', '.pdf'})
            that the parser is capable of handling.
    """

    def __init__(self, parser_name: str, supported_extensions: Set[str]) -> None:
        """Initializes the BaseParser with core identification parameters.

        Args:
            parser_name: The name/identifier of the parser implementation.
            supported_extensions: A set of file extensions supported by this parser.
        """
        self.parser_name: str = parser_name
        # Normalize extensions to lowercase and ensure they start with a dot
        self.supported_extensions: Set[str] = {
            ext.lower() if ext.startswith(".") else f".{ext.lower()}"
            for ext in supported_extensions
        }

    def validate_input(self, file_path: Union[str, Path]) -> Path:
        """Validates that the input file exists, is a file, and has a supported extension.

        Args:
            file_path: The path to the file to be validated.

        Returns:
            Path: A pathlib.Path object of the validated file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IsADirectoryError: If the path points to a directory.
            ValueError: If the file extension is not supported by the parser.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found at path: {path}")
        if not path.is_file():
            raise IsADirectoryError(f"Path is not a file: {path}")
        if path.suffix.lower() not in self.supported_extensions:
            raise ValueError(
                f"Unsupported file extension '{path.suffix}' for parser '{self.parser_name}'. "
                f"Supported types: {self.supported_extensions}"
            )

        return path

    def load_text(self, file_path: Union[str, Path], encoding: str = "utf-8") -> str:
        """Reads the raw textual content from a validated file.

        Args:
            file_path: The path to the text-based file.
            encoding: Character encoding to use when reading the file. Defaults to "utf-8".

        Returns:
            str: The raw text content of the file.
        """
        validated_path = self.validate_input(file_path)
        with open(validated_path, mode="r", encoding=encoding) as file:
            return file.read()

    def normalize_spaces(self, text: str) -> str:
        """Normalizes whitespace by collapsing multiple spaces and tabs into a single space.

        Trims leading and trailing whitespaces while preserving single newlines
        to maintain structural line breaks where necessary.

        Args:
            text: The target text to normalize.

        Returns:
            str: Normalized text with cleaned whitespace.
        """
        lines = text.splitlines()
        cleaned_lines = [" ".join(line.split()) for line in lines]
        return "\n".join(line for line in cleaned_lines)

    def remove_control_characters(self, text: str) -> str:
        """Removes non-printable ASCII control characters from the text.

        Preserves standard formatting characters like line breaks (LF, CR) and tabs.

        Args:
            text: The target text to sanitize.

        Returns:
            str: Cleaned text free of corruptive control characters.
        """
        return "".join(
            char for char in text 
            if char.isprintable() or char in "\n\r\t"
        )

    def clean_text(self, text: str) -> str:
        """Pipeline method that applies all baseline text-sanitization steps.

        Can be overridden by subclasses if additional or alternative pipeline
        steps (like lowercasing or unicode normalization) are required.

        Args:
            text: Raw input text.

        Returns:
            str: Sanitized and structured text ready for parsing.
        """
        if not text:
            return ""
        
        text = self.remove_control_characters(text)
        text = self.normalize_spaces(text)
        return text.strip()

    @abstractmethod
    def parse(self, raw_text: str) -> Any:
        """Abstract method to extract structured data from the cleaned text.

        Must be implemented by concrete subclasses to target specialized
        document types (e.g., Bill of Lading, Invoice).

        Args:
            raw_text: The source text (preferably sanitized) to parse.

        Returns:
            Any: A structured document model instance (e.g., BaseDocument or subclass).
        """
        pass