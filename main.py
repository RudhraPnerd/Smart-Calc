import tkinter as tk
import configs
import window_main # Import the module that contains Display_Configs

# ---- DISPLAY_CONFIGS INSTANCES (Only access variables that are simple data types here) ----
# IMPORTANT: DO NOT assign font objects here. They must be created AFTER tk.Tk() is made.
HEIGHT = window_main.Display_Configs.DISPLAY_HEIGHT
BG_COLOUR = window_main.Display_Configs.DISPLAY_BG_COLOUR
DISPLAY_LABEL_BG_COLOUR = window_main.Display_Configs.DISPLAY_LABEL_BG_COLOUR
DISPLAY_LABEL_FG_COLOUR = window_main.Display_Configs.DISPLAY_LABEL_FG_COLOUR
DISPLAY_PADX = window_main.Display_Configs.DISPLAY_LABEL_PADX
BUTTON_BG_COLOUR = '#FFFFFF'
BUTTONS_FONT = ("Inter", 24, "bold")
BUTTONS_BORDER_WIDTH = 0
# -----------------------------------------------------------------------------------------


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.display_total_label_font = window_main.Display_Configs.get_total_label_font()
        self.display_current_label_font = window_main.Display_Configs.get_current_label_font()

        self.window.geometry(f"{configs.SCREEN_WIDTH}x{configs.SCREEN_HEIGHT}")
        self.window.resizable(False, False)
        self.window.title('Smart Calc')

        self.total_expression = '0'
        self.current_expression = '0'

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4,1)
        }

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()

    def create_display_labels(self):

        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=DISPLAY_LABEL_BG_COLOUR,
                               fg=DISPLAY_LABEL_FG_COLOUR, padx=DISPLAY_PADX, font=self.display_total_label_font)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=DISPLAY_LABEL_BG_COLOUR,
                               fg=DISPLAY_LABEL_FG_COLOUR, padx=DISPLAY_PADX, font=self.display_current_label_font)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=HEIGHT, bg=BG_COLOUR)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_pos in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=BUTTON_BG_COLOUR, fg=DISPLAY_LABEL_FG_COLOUR,
                               font=BUTTONS_FONT, borderwidth=BUTTONS_BORDER_WIDTH)
            button.grid(row=grid_pos[0], column=grid_pos[1], sticky=tk.NSEW)
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()