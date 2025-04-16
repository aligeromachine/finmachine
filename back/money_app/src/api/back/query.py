SELECT_REPORT = """
SELECT
    hash.id,
    hash.password,
    hash.hash
FROM
    content.taskshash hash
JOIN
    content.tasks task on task.id = hash.task_id
WHERE
    not hash.modified is null 
AND
    task.id = %s
ORDER BY
    hash.modified desc
"""

SELECT_DT_MODIF = """
SELECT
    task.id,
    task.modified
FROM
    content.tasks task
WHERE
    task.id = %s
"""
