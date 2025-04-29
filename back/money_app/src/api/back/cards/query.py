SQL_CARDS = """
SELECT
    cards.id,
    cards.created,
    cards.title,
    cards.amount,
    cards.number
FROM
    content.cards cards
WHERE
    cards.user_id = %s
ORDER BY
    cards.id desc
OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
"""
CARDS_TOTAL = """
SELECT
    1 id,
    count(1) c
FROM
    content.cards cards
WHERE
    cards.user_id = %s
"""
