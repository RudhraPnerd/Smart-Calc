# window_main.py

import tkinter.font as tkFont

class Display_Configs:
    DISPLAY_HEIGHT = 150 # Example height, adjust as needed
    DISPLAY_BG_COLOUR = "#282828" # Dark gray background for the entire display frame
    DISPLAY_LABEL_BG_COLOUR = "#282828" # Same dark gray for the label background
    DISPLAY_LABEL_FG_COLOUR = "#FFFFFF" # White text for display numbers
    DISPLAY_LABEL_PADX = 15

    @staticmethod
    def get_total_label_font():
        # Changed weight from "light" to "normal"
        return tkFont.Font(family="Helvetica Neue", size=30, weight="normal")
    @staticmethod
    def get_current_label_font():
        # Changed weight from "light" to "normal"
        return tkFont.Font(family="Helvetica Neue", size=45, weight="normal")

class Buttons_Configs:
    class Digits:
        BUTTON_BG_COLOUR = "#505050" # Darker gray for digit buttons
        # Note: Font for buttons can also be a tuple like ("Helvetica Neue", 24, "bold")
        # If you are using tkFont.Font objects for buttons as well, apply the same weight restriction.
        BUTTONS_FONT = ("Helvetica Neue", 24)
        BORDER_WIDTH = 0
        BUTTON_FG_COLOUR = "#FFFFFF" # White text for digit buttons

    class Operators:
        OPERATORS_FONT = ("Helvetica Neue", 24)
        OPERATORS_BG_COLOUR = "#FF9500" # Distinct orange for operators
        OPERATORS_BORDER_WIDTH = 0
        OPERATORS_FG_COLOUR = "#FFFFFF" # White text for operator buttons