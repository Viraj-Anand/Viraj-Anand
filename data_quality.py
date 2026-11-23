def data_quality_report(rows):
    if not hasattr(rows, "__iter__"):
        raise TypeError("rows must be an iterable of dict-like rows")
    rows = list(rows)
    row_count = len(rows)
    columns = []
    for row in rows:
        if not hasattr(row, "keys"):
            raise TypeError("each row must be a mapping with keys")
        for key in row.keys():
            if key not in columns:
                columns.append(key)
    column_count = len(columns)
    missing_counts = {col: 0 for col in columns}
    for row in rows:
        for col in columns:
            if col not in row or row[col] is None:
                missing_counts[col] += 1
    if row_count == 0:
        missing_fraction = {}
    else:
        missing_fraction = {col: missing_counts[col] / row_count for col in columns}
    seen = set()
    duplicate_rows = 0
    for row in rows:
        key = tuple(sorted(row.items()))
        if key in seen:
            duplicate_rows += 1
        else:
            seen.add(key)
    return {
        "row_count": row_count,
        "column_count": column_count,
        "missing_counts": missing_counts,
        "missing_fraction": missing_fraction,
        "duplicate_rows": duplicate_rows,
    }
