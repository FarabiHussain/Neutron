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

        self.conn.execute(query)

    def initialize_tables(self):

        self.create_table(
            "Status", 
            {
                "status_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "status_type": "TEXT",
                "status_issued": "TEXT",
                "status_expiry": "TEXT",
                "current_status": "INTEGER",
                "status_created": "TEXT",
                "client_id": "TEXT",
                'FOREIGN KEY ("client_id")': 'REFERENCES "Client"("client_id")',
            }
        )

        self.create_table(
            'Client', 
            {
                'client_id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'created_date': 'TEXT',
                'client_uci': 'TEXT',
                'first_name': 'TEXT',
                'last_name': 'TEXT',
                'date_of_birth': 'TEXT',
                'sex': 'TEXT',
                'marital_status': 'TEXT',
                'email': 'TEXT',
                'phone': 'TEXT',
                'street': 'TEXT',
                'city': 'TEXT',
                'province': 'TEXT',
                'postal': 'TEXT',
                'country': 'TEXT',
                'cases_qty': 'INTEGER'
            }
        )

        self.create_table(
            "Application", 
            {
                'application_id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'application_type': 'TEXT',
                'application_number': 'TEXT',
                'created_date': 'TEXT',
                'client_id': 'TEXT',
                'FOREIGN KEY ("client_id")': 'REFERENCES "Client"("client_id")',
            }
        )

        self.create_table(
            "Payments", 
            {
                'payments_id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'payments_amount': 'TEXT',
                'payments_number': 'TEXT',
                'created_date': 'TEXT',
                'client_id': 'TEXT',
                'application_id': 'INTEGER',
                'FOREIGN KEY ("client_id")': 'REFERENCES "Client"("client_id")',
                'FOREIGN KEY ("application_id")': 'REFERENCES "Application"("application_id")',
            }
        )

