from lib import *
from components import *
from database import *
from faker import Faker
from datetime import datetime, date
import names, random, os


db = Database("data.db")
fk = Faker()


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
    clients_tbl = Table(container_tabs["Clients"], ["UCI", "Given Name", "Last Name", "Current Status", "Cases"])
    # clients_tbl.set_data()
    # vr.root.mainloop()


def populate_tables():
    os.system("del .\\data.db")
    db = Database("data.db")
    db.initialize_tables()

    for _ in range(5):

        client_name = names.get_full_name(gender=random.choice(["male", "female"]))
        last_name = client_name.split(" ")[0]
        first_name = client_name.split(" ")[1]
        client_uci = str(random.randint(1000000, 9999999))

        db.conn.execute(
            (
                """
                INSERT INTO Client (
                    created_date,
                    client_uci,
                    first_name,
                    last_name,
                    date_of_birth,
                    sex,
                    marital_status,
                    email,
                    phone,
                    cases_qty
                )
                VALUES (?,?,?,?,?,?,?,?,?,?)
                """
            ),
            (
                datetime.now(),
                client_uci,
                last_name,
                first_name,
                fk.date_of_birth(minimum_age=21, maximum_age=45),
                random.choice(["Male", "Female"]),
                f"{last_name.lower()}_{first_name.lower()}@email.com",
                f"+1 ({str(random.randint(100,999))}) {str(random.randint(100,999))}-{str(random.randint(1000,9999))}",
                random.choice(["Married", "Single", "Common-Law", "Divorced"]),
                0,
            ),
        )

        fetched_id = db.conn.execute(
            f"""
            SELECT client_id
            FROM Client
            WHERE client_uci="{client_uci}"
            """
        ).fetchone()

        db.conn.execute(
            (
                """
                INSERT INTO Status (
                    status_type,
                    status_issued,
                    status_expiry,
                    current_status,
                    status_created,
                    client_id
                )
                VALUES (?,?,?,?,?,?)
                """
            ),
            (
                random.choice(["PGWP", "SP", "SOWP", "TRP", "PR"]),
                fk.date_of_birth(minimum_age=1, maximum_age=3),
                fk.date_between(date(2025, 1, 1), date(2026, 12, 31)),
                1,
                datetime.now(),
                fetched_id[0] 
            ),
        )

    db.conn.commit()


vr.init_vars()
# populate_tables()
render()
