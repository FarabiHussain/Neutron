from lib import *
from customtkinter import *


# initalize the variables to be used throughout the app
def init_vars():
    global screen_w, screen_h, form, root, cwd, icons, font_family

    set_appearance_mode("dark")
    # set_default_color_theme("dark-blue")
    root = CTk()
    root.resizable(False, False)

    cwd = getcwd()
    font_family = CTkFont(family="Roboto Bold")
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    form = {"version": "v0.0.1"}
    icons = set_icons()


# populate the icons
def set_icons():
    icons = {}

    # icons_specs = {
    #     "folder": None,
    #     "clear": None,
    #     "search": None,
    #     "docx": None,
    #     "add": None,
    #     "open": None,
    # }

    # for icon_name in list(icons_specs.keys()):
    #     icons_specs[icon_name] = img.open(
    #         rs.register("assets\\icons\\" + icon_name + ".png")
    #     )

    #     img_size = icons_specs[icon_name].size
    #     img_ratio = img_size[0]/img_size[1]

    #     icons[icon_name] = CTkImage(
    #         light_image=None,
    #         dark_image=icons_specs[icon_name],
    #         size=(25*img_ratio, 25),
    #     )

    return icons
