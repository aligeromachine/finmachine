SQL_SHOP = """
SELECT 
    shop.id, 
    shop.created, 
    shop.title, 
    shop.address
FROM 
    content.shop shop
WHERE 
    shop.user_id = %s
ORDER BY 
    shop.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
SHOP_TOTAL = """
SELECT 
    1 id,
    count(1) c
FROM 
    content.shop shop
WHERE 
    shop.user_id = %s
"""
