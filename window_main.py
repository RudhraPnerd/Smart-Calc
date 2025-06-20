import tkinter as tk
import tkinter.font as tkFont

class Display_Configs:

    DISPLAY_HEIGHT = 150
    DISPLAY_BG_COLOUR = "#FFFFFF"
    DISPLAY_LABEL_BG_COLOUR = "#FFFFFF"
    DISPLAY_LABEL_FG_COLOUR = "#000000"

    DISPLAY_LABEL_PADX = 20

    FONT_TOTAL_PARAMS = ("Arial", 18, "normal")
    FONT_CURRENT_PARAMS = ("Arial", 32, "bold")

    @staticmethod
    def get_total_label_font():
        return tkFont.Font(family=Display_Configs.FONT_TOTAL_PARAMS[0],
                           size=Display_Configs.FONT_TOTAL_PARAMS[1],
                           weight=Display_Configs.FONT_TOTAL_PARAMS[2])

    @staticmethod
    def get_current_label_font():
        return tkFont.Font(family=Display_Configs.FONT_CURRENT_PARAMS[0],
                           size=Display_Configs.FONT_CURRENT_PARAMS[1],
                           weight=Display_Configs.FONT_CURRENT_PARAMS[2])