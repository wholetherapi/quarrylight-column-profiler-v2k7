from collections import Counter


def profile(values: list) -> dict:
    non_null = [v for v in values if v is not None]
    counts = Counter(non_null)
    distinct = len(counts)
    top = counts.most_common(5)
    return {
        "rows": len(values),
        "nulls": len(values) - len(non_null),
        "distinct": distinct,
        "top_values": top,
    }


def null_ratio(values: list) -> float:
    if not values:
        return 0.0
    return sum(1 for v in values if v is None) / len(values)
