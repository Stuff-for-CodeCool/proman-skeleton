from app.database import query


def get_all():
    return query("SELECT * FROM cards;")


def get_one(id):
    return query(
        "SELECT * FROM cards WHERE id = %(id)s",
        {"id": id},
        single=True,
    )


def get_by_board_and_status(bid, sid):
    return query(
        """
            SELECT
                id, title
            FROM cards
            WHERE
                board_id = %(bid)s AND
                status_id = %(sid)s
            ORDER BY card_order ASC;
        """,
        {
            "bid": bid,
            "sid": sid,
        },
    )


def add_one(title):
    return query(
        """
        INSERT INTO statuses (title) SELECT %(title)s
        WHERE NOT EXISTS (
            SELECT 1
            FROM statuses
            WHERE title = %(title)s
        );
        SELECT id FROM statuses WHERE title = %(title)s;
        """,
        {"title": title},
        single=True,
    )


def update(id, board_id, status_id, title, card_order):
    return query(
        """
            UPDATE cards SET
                board_id = %(board_id)s,
                status_id = %(status_id)s,
                title = %(title)s,
                card_order = %(card_order)s
            WHERE id = %(id)s
            RETURNING *;
        """,
        {
            "id": id,
            "board_id": board_id,
            "status_id": status_id,
            "title": title,
            "card_order": card_order,
        },
        single=True,
    )


def delete(id):
    return query(
        "DELETE FROM boards WHERE id = %(id)s RETURNING id;",
        {"id": id},
        single=True,
    )
