SQL_BUY = """
SELECT
    buy.id,
    buy.created,
    buy.title,
    buy.amount,
    shop.title shop,
    cat.title cat,
    prod.title prod
FROM
    content.buy buy
JOIN
    content.shop shop on buy.shop_id = shop.id
JOIN
    content.products prod on buy.products_id = prod.id
JOIN
    content.catalog cat on prod.catalog_id = cat.id
WHERE
    buy.user_id = %s
ORDER BY
    buy.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
BUY_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.buy buy
JOIN
    content.shop shop on buy.shop_id = shop.id
JOIN
    content.products prod on buy.products_id = prod.id
WHERE
    buy.user_id = %s
"""
BUY_ROW = """
SELECT
    buy.id,
    buy.created,
    buy.title,
    buy.amount,
    shop.id shop,
    cat.id cat,
    prod.id prod
FROM
    content.buy buy
JOIN
    content.shop shop on buy.shop_id = shop.id
JOIN
    content.products prod on buy.products_id = prod.id
JOIN
    content.catalog cat on prod.catalog_id = cat.id
WHERE
    buy.id = %s
"""