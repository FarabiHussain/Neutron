import os
from lib import *
from components import *
from database import *
import names, random


def render():
    system("cls")

    h = 900
    w = 1200
    x = (vr.screen_w / 2) - (w / 2)
    y = (vr.screen_h / 2) - (h / 2) - 50

    vr.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    vr.root.iconbitmap(rs.register("assets\\icons\\icon.ico"))
    vr.root.title(f"Neutron ({vr.form['version']})")

    container = Tabview(vr.root, ["Clients", "Documents", "Cases", "Finances"])
    container_tabs = container.get_tabs()
    clients_tbl = Table(
        container_tabs["Clients"],
        ["UCI", "Given Name", "Last Name", "Current Status", "Cases"],
    )

    add_data = []

    for _ in range(50):
        client_name = names.get_full_name(gender=random.choice(["male", "female"]))
        given_name = client_name.split(" ")[0]
        last_name = client_name.split(" ")[1]
        uci = str(random.randint(1000000, 9999999))
        stats = random.choice(["PGWP", "SP", "SOWP", "TRP", "PR"])

        add_data.append([uci, given_name, last_name, stats, "0"])

    clients_tbl.set_data(add_data)

    # vr.root.state('zoomed')
    vr.root.mainloop()

def setup_database():
    db = Database("data")

    db.create_table(
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

    db.create_table(
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
        }
    )

    db.create_table(
        "Application", 
        {
            "application_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "application_type": "TEXT",
            "application_number": "TEXT",
            "created_date": "TEXT",
            "client_id": "TEXT",
            'FOREIGN KEY ("client_id")': 'REFERENCES "Client"("client_id")',
        }
    )

    db.create_table(
        "Transaction", 
        {
            "transaction_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "transaction_amount": "TEXT",
            "transaction_number": "TEXT",
            "created_date": "TEXT",
            "client_id": "TEXT",
            "application_id": "INTEGER",
            'FOREIGN KEY ("client_id")': 'REFERENCES "Client"("client_id")',
            'FOREIGN KEY ("application_id")': 'REFERENCES "Application"("application_id")',
        }
    )



vr.init_vars()
os.system("del .\\data.db")
setup_database()
# render()
