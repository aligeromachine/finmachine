SQL_BUY = """
SELECT
    buy.id,
    buy.created,
    buy.title,
    buy.amount,
    shop.title shop,
    prod.title prod
FROM
    content.buy buy
JOIN
    content.shop shop on buy.shop_id = shop.id
JOIN
    content.products prod on buy.products_id = prod.id
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
