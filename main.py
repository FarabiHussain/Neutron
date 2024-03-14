from lib import *
from components import *
import names, random


def render():
    # calculate x and y coordinates for the Tk root window

    h = 900
    w = 1200
    x = (vr.screen_w / 2) - (w / 2)
    y = (vr.screen_h / 2) - (h / 2) - 50

    system("cls")
    vr.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    vr.root.iconbitmap(rs.register("assets\\icons\\icon.ico"))
    vr.root.title(f"Neutron ({vr.form['version']})")

    container = Tabview(vr.root, ["Clients", "Documents", "Cases", "Finances"])
    container_tabs = container.get_tabs()
    clients_tbl = Table(
        container_tabs["Clients"], 
        ["UCI", "Given Name", "Last Name", "Current Status", "Cases"]
    )

    add_data = []

    for _ in range(50):
        client_name = names.get_full_name(gender=random.choice(['male', 'female']))
        given_name = client_name.split(" ")[0]
        last_name = client_name.split(" ")[1]
        uci = str(random.randint(1000000, 9999999))
        stats = random.choice(["PGWP", "SP", "SOWP", "TRP", "PR"])

        add_data.append([uci, given_name, last_name, stats, "0"])

    clients_tbl.set_rows(add_data)

    # vr.root.state('zoomed')
    vr.root.mainloop()


vr.init_vars()
render()
