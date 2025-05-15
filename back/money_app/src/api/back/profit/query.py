SQL_PROFIT = """
SELECT
    prof.id,
    prof.created,
    prof.title,
    prof.amount,
    src.title src
FROM
    content.profit prof
JOIN
    content.source src on src.id = prof.source_id
WHERE
    prof.user_id = %s
ORDER BY
    prof.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
PROFIT_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.profit prof
WHERE
    prof.user_id = %s
"""
