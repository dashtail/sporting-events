from django.db import connection
from celery import shared_task

def get_update_query_by_id(id, data, table_name):
    query = f"UPDATE {table_name} set"

    data = list(data.items())
    for attr, value in data[:-1]:
        query = f"{query} {attr} = '{value}',"
    else:
        query = f"{query} {data[-1][0]} = '{data[-1][1]}'"

    query = f"{query} WHERE id={id} returning *"

    return query


@shared_task
def check_actives_sports(sport_id):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id FROM event_event WHERE sport_id={sport_id} AND active=True LIMIT 1")
        row = cursor.fetchone()
        
        if not row:
            cursor.execute(
            f"UPDATE sport_sport set active=False WHERE id={sport_id}")

@shared_task
def check_actives_events(event_id):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id FROM selection_selection WHERE event_id={event_id} AND active=True LIMIT 1")
        row = cursor.fetchone()
        
        if not row:
            cursor.execute(
            f"UPDATE event_event set active=False WHERE id={event_id} returning sport_id")
            sport_id = cursor.fetchone()[0]
            check_actives_sports.apply_async(args=[sport_id])

    return row

