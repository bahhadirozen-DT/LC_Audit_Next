from dataclasses import dataclass

@dataclass
class ReserveResult:
    passed: bool
    field: str
    message: str
    severity: str = "WARNING"
