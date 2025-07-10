TASK_TO_LOAD: str = """
SELECT
    task.id,
    task.hash_type,
    COALESCE(jsonb_agg(jsonb_build_object(
        'id', hash.id,
        'login', hash.hash_login,
        'hash', hash.hash
    )) FILTER (WHERE hash.id is not null), '[]') js
FROM
    content.taskshash hash
JOIN
    content.tasks task on task.id = hash.task_id
WHERE
    task.crusher = 'VIRIFY'
AND
    hash.modified is null
GROUP BY
    task.id
"""
BUY_GROUP: str = """
SELECT
    EXTRACT(YEAR FROM created) AS year,
    SUM(amount) AS total_amount,
    COUNT(*) AS orders_count,
    user_id
FROM 
    content.buy
GROUP BY 
    EXTRACT(YEAR FROM created),
    user_id
ORDER BY year;
"""

GROUP_USER_YEAR_BUY_PROFIT: str = """
WITH buy_stat as (
SELECT
    EXTRACT(YEAR FROM created) AS year,
    SUM(amount) AS total_buy,
    user_id
FROM 
    content.buy
GROUP BY 
    EXTRACT(YEAR FROM created),
    user_id
),
profit_stat as (
SELECT
    EXTRACT(YEAR FROM created) AS year,
    SUM(amount) AS total_profit,
    user_id
FROM 
    content.profit
GROUP BY 
    EXTRACT(YEAR FROM created),
    user_id
)
SELECT
    1 id,
    buy_stat.user_id, 
    COALESCE(jsonb_agg(jsonb_build_object(
        'year', buy_stat.year,
        'buy', buy_stat.total_buy,
        'profit', profit_stat.total_profit
    )) FILTER (WHERE buy_stat.user_id is not null), '[]') payload
FROM
    buy_stat
FULL JOIN
    profit_stat 
ON
    buy_stat.year = profit_stat.year and buy_stat.user_id = profit_stat.user_id
GROUP BY
    buy_stat.user_id
"""
