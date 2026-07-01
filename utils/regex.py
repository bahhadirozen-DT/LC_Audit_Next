"""
LC_Audit_Next - Centralized Regex Library
Module: utils.regex

This module serves as the single source of truth for compiled regular expression
patterns across the entire trade finance document auditing pipeline. It contains
strictly raw regex structures optimized for speed and safety, completely detached
from parser logic, execution lifecycles, or external extraction dependencies.
"""

import re
from typing import Final

# ==============================================================================
# SWIFT MT700 SPECIFIC PATTERNS
# ==============================================================================

SWIFT_TAG_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^:([0-9]{2}[A-Z]?):",
    re.MULTILINE
)
"""Matches the structural start of standard SWIFT block tags (e.g., :40A:, :31D:)."""

SWIFT_AMOUNT_CURRENCY_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^([A-Z]{3})([0-9.,]+)",
    re.MULTILINE
)
"""Captures leading ISO currency strings directly followed by fractional numeric bodies."""

SWIFT_DATE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\b"
)
"""Validates the foundational strict 6-digit YYMMDD raw string formats inside SWIFT blocks."""

PERCENTAGE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"([0-9]+(?:[.,][0-9]+)?)\s*%"
)
"""Identifies trailing fractional percentages across standard variance allowances (e.g., 39A/B)."""

NUMERIC_DAYS_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b([0-9]+)\s*(?:DAYS|DAYS\s+AFTER|DAYS\s+FROM)\b",
    re.IGNORECASE
)
"""Extracts day boundaries from specific credit timelines and presentation parameters (e.g., 48)."""

DOCUMENT_RECOGNITION_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:COMMERCIAL\s+INVOICE|PACKING\s+LIST|BILL\s+OF\s+LADING|CERTIFICATE\s+OF\s+ORIGIN|"
    r"INSURANCE\s+(?:POLICY|CERTIFICATE)|AIR\s+WAYBILL|TRUCK\s+WAYBILL|WEIGHT\s+NOTE)\b",
    re.IGNORECASE
)
"""Identifies standard commercial document instances across cross-document instructions (e.g., 46A)."""

INCOTERM_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(EXW|FCA|CPT|CIP|DAT|DAP|DDP|FAS|FOB|CFR|CIF)\b",
    re.IGNORECASE
)
"""Detects formal structural ICC international commercial terms inside shipment declarations."""

CURRENCY_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(USD|EUR|GBP|JPY|CHF|CNY|CAD|AUD|SGD|HKD|AED|SAR)\b"
)
"""Extracts isolated traditional trade-related ISO currency markers across free-text zones."""


# ==============================================================================
# COMMERCIAL INVOICE PATTERNS
# ==============================================================================

INVOICE_NUMBER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:INVOICE|INV)\s*(?:NO|NUMBER|\.|:)?\s*([A-Z0-9\-/]+)\b",
    re.IGNORECASE
)
"""Locates specific alpha-numeric invoice structural reference strings inside document headers."""

INVOICE_DATE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:INVOICE\s+DATE|DATE\s+OF\s+ISSUE|DATE)\s*(?::)?\s*([0-9A-Z\s,./-]+)\b",
    re.IGNORECASE
)
"""Extracts textual or date instances explicitly bound to commercial document confirmation headers."""

TOTAL_AMOUNT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:TOTAL|TOTAL\s+AMOUNT|NET\s+TOTAL|GRAND\s+TOTAL|INVOICE\s+VALUE)\s*(?::)?\s*(?:[A-Z]{3})?\s*([0-9,.]+)\b",
    re.IGNORECASE
)
"""Extracts global cumulative trade balancing amounts across document matrices."""

UNIT_PRICE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:UNIT\s+PRICE|PRICE/UNIT|RATE|PU)\s*(?::)?\s*(?:[A-Z]{3})?\s*([0-9,.]+)\b",
    re.IGNORECASE
)
"""Isolates internal specific localized atomic values per structured unit item lines."""

QUANTITY_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:QTY|QUANTITY|PCS|PIECES|UNITS|KGS)\s*(?::)?\s*([0-9,.]+)\b",
    re.IGNORECASE
)
"""Extracts continuous structural mathematical values assigned directly to volume declarations."""

WEIGHT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"([0-9,.]+)\s*(?:KG|KGS|KILOGRAM|KILOGRAMS|MT|TON|TONS|LBS)\b",
    re.IGNORECASE
)
"""Captures pure weights paired explicitly with canonical metric/imperial notations."""

GOODS_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:DESCRIPTION\s+OF\s+GOODS|GOODS\s+DESCRIPTION|DESCRIPTION|COMMODITY)\b",
    re.IGNORECASE
)
"""Locates block anchors targeting detailed shipping material configurations and listings."""


# ==============================================================================
# BILL OF LADING PATTERNS
# ==============================================================================

BL_NUMBER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:BILL\s+OF\s+LADING\s*(?:NO)?|B/L\s*(?:NO)?|BL\s*(?:NO)?)\s*(?:NUMBER|\.|:)?\s*([A-Z0-9\-/]+)\b",
    re.IGNORECASE
)
"""Extracts primary maritime transport identifiers inside title tracking margins."""

ONBOARD_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:SHIPPED\s+ON\s+BOARD|LADEN\s+ON\s+BOARD|ON\s+BOARD\s+DATE|CLEAN\s+ON\s+BOARD)\b",
    re.IGNORECASE
)
"""Triggers strict validation indicators required to prove structural ICC shipment execution."""

VESSEL_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:VESSEL|OCEAN\s+VESSEL|VESSEL\s+NAME|FEEDER)\s*(?:NAME|\.|:)?\s*([A-Z0-9\s.]+)(?:\s+VOY|\b)",
    re.IGNORECASE
)
"""Extracts standard maritime vessel designations while excluding structural voyage designations."""

PORT_LOADING_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:PORT\s+OF\s+LOADING|POL|PORT\s+OF\s+LOAD)\s*(?::)?\s*([A-Z0-9\s,.-]+?)(?=\s*(?:PORT|VIA|\n|\t))",
    re.IGNORECASE
)
"""Triggers identification blocks tracking spatial points of transport initialization."""

PORT_DISCHARGE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:PORT\s+OF\s+DISCHARGE|POD)\s*(?::)?\s*([A-Z0-9\s,.-]+?)(?=\s*(?:PORT|VIA|\n|\t))",
    re.IGNORECASE
)
"""Triggers identification blocks tracking target geographical points of delivery execution."""

CONTAINER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b([A-Z]{4}[0-9]{7})\b"
)
"""Enforces strict ISO 6346 identification structural layouts for primary shipping equipment."""

SEAL_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:SEAL|SEAL\s*(?:NO|NUMBER)?)\s*(?::)?\s*([A-Z0-9\-]+)\b",
    re.IGNORECASE
)
"""Extracts security lock indicators tied structurally to maritime shipping equipment identifiers."""


# ==============================================================================
# PACKING LIST PATTERNS
# ==============================================================================

PACKAGE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"([0-9,.]+)\s*(?:PKGS|PACKAGES|CTNS|CARTONS|BOXES|CRATES|BAGS|DRUMS)\b",
    re.IGNORECASE
)
"""Captures pure quantitative values bound specifically to standardized external containers."""

GROSS_WEIGHT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:GROSS\s+WEIGHT|G\.W\.|GW)\s*(?::)?\s*([0-9,.]+)\s*(?:KG|KGS|MTS|TONS|LBS)?\b",
    re.IGNORECASE
)
"""Extracts overall package mass markers from logistics sheets."""

NET_WEIGHT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:NET\s+WEIGHT|N\.W\.|NW)\s*(?::)?\s*([0-9,.]+)\s*(?:KG|KGS|MTS|TONS|LBS)?\b",
    re.IGNORECASE
)
"""Extracts isolated merchandise weight bounds excluding container packaging elements."""

CBM_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"([0-9,.]+)\s*(?:CBM|M3|CUBIC\s+METER|CUBIC\s+METERS)\b",
    re.IGNORECASE
)
"""Extracts absolute volume parameters from physical shipping matrices."""

PALLET_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"([0-9,.]+)\s*(?:PLTS|PALLETS|PALLET|SKIDS)\b",
    re.IGNORECASE
)
"""Isolates spatial configuration indicators used in internal structural warehouse profiles."""


# ==============================================================================
# INSURANCE PATTERNS
# ==============================================================================

POLICY_NUMBER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:POLICY|CERTIFICATE|INSURANCE\s+NO|POLICY\s+NO)\s*(?:NUMBER|NUMBER\s+NO|\.|:)?\s*([A-Z0-9\-/]+)\b",
    re.IGNORECASE
)
"""Extracts legal registration and policy identification IDs from marine security wrappers."""

INSURANCE_AMOUNT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:AMOUNT\s+INSURED|INSURED\s+AMOUNT|SUM\s+INSURED)\s*(?::)?\s*(?:[A-Z]{3})?\s*([0-9,.]+)\b",
    re.IGNORECASE
)
"""Extracts explicit liability capitalization covers assigned within risk documents."""

INSURANCE_PERCENT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:INSURED\s+FOR|COVERAGE\s+PERCENT|FOR)\s*([0-9]+(?:[.,][0-9]+)?)\s*%",
    re.IGNORECASE
)
"""Matches target structural value percentages (e.g., 110% CIF requirements under UCP 600)."""

RISKS_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:INSTITUTE\s+CARGO\s+CLAUSES\s*\(?[A-C]\)?|WAR\s+RISKS|STRIKES\s+RISKS|ALL\s+RISKS)\b",
    re.IGNORECASE
)
"""Identifies specific reference bindings classifying global trade protection conditions."""


# ==============================================================================
# CERTIFICATE OF ORIGIN PATTERNS
# ==============================================================================

COUNTRY_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:COUNTRY\s+OF\s+ORIGIN|ORIGINATING\s+IN|MANUFACTURED\s+IN)\s*(?::)?\s*([A-Z\s]{2,})\b",
    re.IGNORECASE
)
"""Extracts geographic tracking targets connected with state declarations."""

ORIGIN_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"\b(?:PREFERENTIAL\s+ORIGIN|CERTIFICATE\s+OF\s+ORIGIN|ORIGIN\s+CRITERION)\b",
    re.IGNORECASE
)
"""Locates specific regulatory headings within cross-border shipping documents."""