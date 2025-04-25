SQL_PROFIT = """
SELECT 
	profit.id, 
	profit.created, 
	profit.title, 
	profit.amount, 
	src.title sources
FROM 
	content.profit profit
JOIN 
	content.source src on src.id = profit.source_id
WHERE 
    profit.user_id = %s
ORDER BY 
    profit.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
PROFIT_TOTAL = """
SELECT 
    1 id,
    count(1) c
FROM 
    content.profit profit
WHERE 
    profit.user_id = %s
"""
