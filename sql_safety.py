import re


BLOCKED_WORDS = [
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "replace",
    "grant",
    "revoke",
]


def validate_sql(sql: str) -> str:
    """
    Allow only a single read-only SELECT statement.
    """

    if not sql or not sql.strip():
        raise ValueError("SQL query is empty.")

    cleaned = sql.strip()

    # Remove optional markdown code fences
    cleaned = re.sub(r"^```sql\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^```\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)

    cleaned = cleaned.strip()

    lower = cleaned.lower()

    # Must start with SELECT
    if not lower.startswith("select"):
        raise ValueError(
            "Unsafe SQL blocked: only SELECT queries are allowed."
        )

    # Prevent multiple SQL statements
    if ";" in cleaned.rstrip(";"):
        raise ValueError(
            "Unsafe SQL blocked: multiple SQL statements are not allowed."
        )

    # Block dangerous SQL keywords
    for word in BLOCKED_WORDS:
        if re.search(rf"\b{word}\b", lower):
            raise ValueError(
                f"Unsafe SQL blocked: keyword '{word}' is not allowed."
            )

    # Remove one optional trailing semicolon
    cleaned = cleaned.rstrip(";").strip()

    return cleaned