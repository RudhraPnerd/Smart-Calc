import tkinter as tk
import configs
import window_main # Import the module that contains Display_Configs

# -- WINDOW_MAIN.py INSTANCES FROM DISPLAY_CONFIGS, BUTTONS_CONFIGS & OPERATORS_CONFIGS --
HEIGHT = window_main.Display_Configs.DISPLAY_HEIGHT
BG_COLOUR = window_main.Display_Configs.DISPLAY_BG_COLOUR
DISPLAY_LABEL_BG_COLOUR = window_main.Display_Configs.DISPLAY_LABEL_BG_COLOUR
DISPLAY_LABEL_FG_COLOUR = window_main.Display_Configs.DISPLAY_LABEL_FG_COLOUR
DISPLAY_PADX = window_main.Display_Configs.DISPLAY_LABEL_PADX

# NEW: Import button foreground colors
BUTTON_BG_COLOUR = window_main.Buttons_Configs.Digits.BUTTON_BG_COLOUR
BUTTONS_FONT = window_main.Buttons_Configs.Digits.BUTTONS_FONT
BUTTONS_BORDER_WIDTH = window_main.Buttons_Configs.Digits.BORDER_WIDTH
BUTTON_FG_COLOUR = window_main.Buttons_Configs.Digits.BUTTON_FG_COLOUR # <-- NEW

OPERATORS_FONT = window_main.Buttons_Configs.Operators.OPERATORS_FONT
OPERATORS_BG_COLOUR = window_main.Buttons_Configs.Operators.OPERATORS_BG_COLOUR
OPERATORS_BORDERWIDTH = window_main.Buttons_Configs.Operators.OPERATORS_BORDER_WIDTH
OPERATORS_FG_COLOUR = window_main.Buttons_Configs.Operators.OPERATORS_FG_COLOUR # <-- NEW
# ----------------------------------------------------------------------------------------


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.display_total_label_font = window_main.Display_Configs.get_total_label_font()
        self.display_current_label_font = window_main.Display_Configs.get_current_label_font()

        self.window.geometry(f"{configs.SCREEN_WIDTH}x{configs.SCREEN_HEIGHT}")
        self.window.resizable(True, True)
        self.window.title('Smart Calc')

        self.total_expression = ''
        self.current_expression = '0'

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4,1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.display_frame = self.create_display_frame()
        self.display_frame.pack(expand=True, fill="both")

        self.total_label, self.label = self.create_display_labels()
        self.update_total_label()
        self.update_label()

        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()

    # --- Display Update Methods ---
    def update_label(self):
        self.label.config(text=self.current_expression[:12])

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    # --- Button Press Handlers ---
    def add_to_current_expression(self, value):
        if self.current_expression == "0" and value != ".":
            self.current_expression = str(value)
        elif value == '.' and '.' in self.current_expression:
            pass
        else:
            self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator_symbol):
        if operator_symbol == "\u00F7":
            op_for_eval = "/"
        elif operator_symbol == "\u00D7":
            op_for_eval = "*"
        else:
            op_for_eval = operator_symbol

        if not self.total_expression:
            if self.current_expression == 'Error':
                self.clear()
                return
            self.total_expression = self.current_expression + op_for_eval
        elif self.total_expression and self.total_expression[-1] in ["/", "*", "-", "+"]:
            self.total_expression = self.total_expression[:-1] + op_for_eval
        else:
            self.total_expression += self.current_expression + op_for_eval

        self.current_expression = "0"
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.total_expression = ''
        self.current_expression = '0'
        self.update_total_label()
        self.update_label()

    def evaluate(self):
        try:
            expression_to_eval = self.total_expression + self.current_expression
            expression_to_eval = expression_to_eval.replace('\u00F7', '/')
            expression_to_eval = expression_to_eval.replace('\u00D7', '*')

            result = str(eval(expression_to_eval))

            if result.endswith('.0'):
                result = result[:-2]

            self.current_expression = result
            self.total_expression = ''

        except (SyntaxError, ZeroDivisionError):
            self.current_expression = "Error"
            self.total_expression = ''
        except Exception:
            self.current_expression = "Error"
            self.total_expression = ''
        finally:
            self.update_label()
            self.update_total_label()

    # --- UI Creation Methods ---
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
        return frame

    def create_operator_buttons(self):
        operator_positions = {
            "\u00F7": 0,
            "\u00D7": 1,
            "-": 2,
            "+": 3
        }

        for symbol, row_idx in operator_positions.items():
            button = tk.Button(self.buttons_frame, text=symbol, font=OPERATORS_FONT,
                               bg=OPERATORS_BG_COLOUR, fg=OPERATORS_FG_COLOUR, # <-- Changed to OPERATORS_FG_COLOUR
                               borderwidth=OPERATORS_BORDERWIDTH,
                               command=lambda op=symbol: self.append_operator(op))
            button.grid(row=row_idx, column=4, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", font=OPERATORS_FONT,
                           bg=OPERATORS_BG_COLOUR, fg=OPERATORS_FG_COLOUR, # <-- Changed to OPERATORS_FG_COLOUR
                           borderwidth=OPERATORS_BORDERWIDTH,
                           command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", font=OPERATORS_FONT,
                           bg=OPERATORS_BG_COLOUR, fg=OPERATORS_FG_COLOUR, # <-- Changed to OPERATORS_FG_COLOUR
                           borderwidth=OPERATORS_BORDERWIDTH,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)
        return frame

    def create_digit_buttons(self):
        for digit, grid_pos in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=BUTTON_BG_COLOUR, fg=BUTTON_FG_COLOUR, # <-- Changed to BUTTON_FG_COLOUR
                               font=BUTTONS_FONT, borderwidth=BUTTONS_BORDER_WIDTH,
                               command=lambda d=digit: self.add_to_current_expression(d))
            button.grid(row=grid_pos[0], column=grid_pos[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()