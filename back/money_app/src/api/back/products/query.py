SQL_PRODUCTS = """
SELECT
    products.id,
    products.created,
    products.title,
    catalog.title cats
FROM
    content.products products
JOIN
    content.catalog catalog on catalog.id = products.catalog_id
WHERE
    products.user_id = %s
ORDER BY
    products.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
PRODUCTS_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.products products
WHERE
    products.user_id = %s
"""
