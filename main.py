from lib import *
from components import *


def render():
    # calculate x and y coordinates for the Tk root window

    h = 900
    w = 1600
    x = (vr.screen_w / 2) - (w / 2)
    y = (vr.screen_h / 2) - (h / 2)

    system("cls")
    vr.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    vr.root.iconbitmap(rs.register("assets\\icons\\icon.ico"))
    vr.root.title(f"Neutron ({vr.form['version']})")

    container = Tabview(vr.root, ["Clients", "Documents", "Cases", "Finances"])
    container_tabs = container.get_tabs()
    clients_tbl = Table(container_tabs["Clients"], ["UCI", "Given Name", "Last Name", "Current Status", "Cases", ""])

    vr.root.mainloop()


vr.init_vars()
render()
