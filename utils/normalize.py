import re

# Known tests and reference ranges
REF_RANGES = {
    "Hemoglobin": {"low": 12.0, "high": 16.0, "unit": "g/dL", "flag": "Anemic"},
    "WBC": {"low": 4000, "high": 11000, "unit": "/uL", "flag": "Abnormal WBC"},
    "Platelet Count": {"low": 150000, "high": 450000, "unit": "/uL", "flag": "Low Platelets"},
}

def extract_value(text: str):
    """Extract numeric value (with decimal if present)."""
    match = re.search(r"([\d]+\.?\d*)", text)
    return float(match.group(1)) if match else None

def interpret_result(test: str, value: float):
    """Interpret based on reference range."""
    if test not in REF_RANGES or value is None:
        return "Unknown"

    ref = REF_RANGES[test]
    if value < ref["low"]:
        return f"Low ({ref['flag']})"
    elif value > ref["high"]:
        return "High"
    else:
        return "Normal"
