from config.db import connection


def format_result(cursor, result):
    "formats cursor result to list of dictionaries"
    data = []
    for res in result:
        d = dict()
        for idx, c in enumerate(cursor.description):
            d[c[0]] = res[idx]
        data.append(d)
    return data


def get_all_users():
    "get all current users from database"
    cursor = connection.cursor()
    result = cursor.execute(
        """
    SELECT * FROM usersTable
    """
    ).fetchall()
    data = format_result(cursor=cursor, result=result)
    return data
