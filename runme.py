import ibis
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

if __name__ == "__main__":
    connection = ibis.trino.connect(
        host="localhost",
        port=8080,
        user="test",
        password="",
        database="iceberg",
        schema="dev",
    )

    with connection.con.engine.connect() as conn:
        try:
            result=conn.execute(text("CREATE SCHEMA iceberg.dev WITH (location = 's3a://dev/')"))
        except ProgrammingError as e:
            pass

    
    first = ibis.schema({"a": "timestamp(6)"})
    connection.create_table("iceberg_table", schema=first)