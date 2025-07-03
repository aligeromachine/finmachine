SQL_PRODUCTS = """
SELECT
    prod.id,
    prod.created,
    prod.title,
    cat.title catalog
FROM
    content.products prod
JOIN
    content.catalog cat on cat.id = prod.catalog_id
WHERE
    prod.user_id = %s
ORDER BY
    prod.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
PRODUCTS_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.products prod
WHERE
    prod.user_id = %s
"""

PRODUCTS_ROW = """
SELECT
    prod.id,
    prod.title,
    prod.catalog_id catalog
FROM
    content.products prod
WHERE
    prod.id = %s
"""
