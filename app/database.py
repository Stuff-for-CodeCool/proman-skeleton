def establish_connection():
    from psycopg2 import connect, DatabaseError
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()

    try:
        connection = connect(
            user=getenv("DB_USER"),
            password=getenv("DB_PASS"),
            host=getenv("DB_HOST"),
            database=getenv("DB_DB"),
        )
        connection.autocommit = True
        return connection

    except DatabaseError:
        raise RuntimeError("Could not connect to databse")


def query(statement, vars=None, single=False, debug=False):
    from psycopg2.extras import RealDictCursor

    with establish_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(statement, vars)

            if debug:
                print(f"\n\nRan query:\n\n{cursor.query.decode('utf-8')}\n\n")

            if single:
                return dict(cursor.fetchone())

            return [dict(element) for element in cursor.fetchall()]
