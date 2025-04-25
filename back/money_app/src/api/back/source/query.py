SQL_SOURCE = """
SELECT 
    src.id, 
    src.created, 
    src.title
FROM 
    content.source src
WHERE 
    src.user_id = %s
ORDER BY 
    src.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
SOURCE_TOTAL = """
SELECT 
    1 id,
    count(1) c
FROM 
    content.source src
WHERE 
    src.user_id = %s
"""
