import sqlite3


class Database:

    def __init__(self, db_name: str):
        if not db_name.endswith(".db"):
            db_name = f"{db_name}.db"

        self.conn = sqlite3.connect(db_name)

    def create_table(self, table_name: str, columns: dict):

        table_fields = []
        for field, field_type in zip(columns.keys(), columns.values()):
            table_fields.append(f"{field} {field_type}")

        table_fields = (", ").join(table_fields)

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({table_fields})"

        print(query)

        self.conn.execute(query)
