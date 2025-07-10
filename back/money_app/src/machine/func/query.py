SQL_TOTAL_WEEK_MONTH: str = """
WITH buy_stat as (
    (SELECT 1 raw, SUM(amount) AS total
    FROM content.buy
    WHERE created BETWEEN 
        DATE_TRUNC('week', CURRENT_DATE)::date
        AND (DATE_TRUNC('week', CURRENT_DATE) + INTERVAL '6 days')::date
        AND user_id = %s
    )
    UNION ALL
    (
    SELECT 2 raw, SUM(amount) AS total
    FROM content.buy
    WHERE created BETWEEN 
        DATE_TRUNC('month', CURRENT_DATE)
        AND (DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month - 1 day')::date
        AND user_id = %s
    )
),
profit_stat as (
    (SELECT 1 raw, SUM(amount) AS total
    FROM content.profit
    WHERE created BETWEEN 
        DATE_TRUNC('week', CURRENT_DATE)::date
        AND (DATE_TRUNC('week', CURRENT_DATE) + INTERVAL '6 days')::date
        AND user_id = %s
    )
    UNION ALL
    (
    SELECT 2 raw, SUM(amount) AS total
    FROM content.profit
    WHERE created BETWEEN 
        DATE_TRUNC('month', CURRENT_DATE)
        AND (DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month - 1 day')::date
        AND user_id = %s
    )
)
SELECT
    1 id, buy_stat.raw, COALESCE(buy_stat.total, 0) buy, COALESCE(profit_stat.total, 0) profit
FROM
    buy_stat
FULL JOIN
    profit_stat 
ON
    buy_stat.raw = profit_stat.raw
"""
