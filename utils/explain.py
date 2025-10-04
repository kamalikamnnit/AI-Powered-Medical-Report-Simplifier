from utils.normalize import REF_RANGES, extract_value, interpret_result

EXPLANATIONS = {
    "Anemic": "Low hemoglobin may relate to anemia.",
    "Abnormal WBC": "High WBC can occur with infections.",
    "Low Platelets": "Low platelet count may increase bleeding risk."
}

def parse_medical_report(text: str):
    import re
    results = {}
    explanations = []
    summary_parts = []

    chunks = re.split(r"[;\n]", text)
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        for test in REF_RANGES:
            if test.lower() in chunk.lower():
                value = extract_value(chunk)
                interpretation = interpret_result(test, value)
                results[test] = {
                    "raw_line": chunk,
                    "value": value,
                    "outcome": interpretation
                }

                if "Low" in interpretation or "High" in interpretation:
                    summary_parts.append(f"{interpretation} {test}")
                    for key, exp in EXPLANATIONS.items():
                        if key in interpretation:
                            explanations.append(exp)

    summary = ", ".join(summary_parts) if summary_parts else "All values within normal range."
    return results, summary, explanations
