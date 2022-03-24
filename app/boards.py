from app.database import query


def get_all():
    return query("SELECT * FROM boards;")


def get_one(id):
    return query(
        "SELECT * FROM boards WHERE id = %(id)s",
        {"id": id},
        single=True,
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


def update(id, title):
    return query(
        "UPDATE boards SET title = %(title)s WHERE id = %(id)s RETURNING id;",
        {"id": id, "title": title},
        single=True,
    )


def delete(id):
    return query(
        "DELETE FROM boards WHERE id = %(id)s RETURNING id;",
        {"id": id},
        single=True,
    )
