SQL_CATALOG = """
SELECT
    catalog.id,
    catalog.created,
    catalog.title
FROM
    content.catalog catalog
WHERE
    catalog.user_id = %s
ORDER BY
    catalog.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
CATALOG_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.catalog catalog
WHERE
    catalog.user_id = %s
"""

SQL_CATALOG_SORT = """
SELECT
    catalog.id,
    catalog.title
FROM
    content.catalog catalog
WHERE
    catalog.user_id = %s
ORDER BY
    catalog.title
"""
