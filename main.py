from tkinter import *
import customtkinter

customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.configure(background='black')
root.geometry('260x395')
root.resizable(0, 0)
root.title('Calculator')

expression = ''
input_text = StringVar()


def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 260
    window_height = 390

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


center_window(root)


def btn_click(character):
    global expression
    if input_text.get() == '0':
        expression = str(character)
    else:
        expression = expression + str(character)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ''
    input_text.set('')


def btn_backspace():
    current_text = input_text.get()
    updated_text = current_text[:-1]
    input_text.set(updated_text)


def btn_percentage():
    global expression
    result = eval(expression) / 100
    input_text.set(result)
    expression = str(result)


def btn_np():
    global expression
    if expression != '':
        result = eval(expression) * -1
        input_text.set(result)
        expression = str(result)


def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result


input_frame = customtkinter.CTkFrame(root, width=260)
input_frame.pack()

input_box = customtkinter.CTkEntry(input_frame, textvariable=input_text, width=260, justify=RIGHT, state='readonly',
                                   font=customtkinter.CTkFont(size=50), border_width=0, corner_radius=0,
                                   fg_color="#000")
input_box.grid()
input_box.pack(pady=(0, 2))

button_frame = customtkinter.CTkFrame(root, width=260)
button_frame.pack()

# Buttons
btn1 = customtkinter.CTkButton(button_frame, text="C", width=122, height=50, command=lambda: btn_clear())
btn1.grid(row=0, column=0, columnspan=2, padx=0, pady=2)

btn2 = customtkinter.CTkButton(button_frame, text="+ / -", width=60, height=50, command=lambda: btn_np())
btn2.grid(row=0, column=2, padx=0, pady=2)

btn2 = customtkinter.CTkButton(button_frame, text="/", width=60, height=50, command=lambda: btn_click('/'))
btn2.grid(row=0, column=3, padx=0, pady=2)

btn3 = customtkinter.CTkButton(button_frame, text="7", width=60, height=50, command=lambda: btn_click('7'))
btn3.grid(row=1, column=0, padx=0, pady=2)

btn4 = customtkinter.CTkButton(button_frame, text="8", width=60, height=50, command=lambda: btn_click('8'))
btn4.grid(row=1, column=1, padx=0, pady=2)

btn5 = customtkinter.CTkButton(button_frame, text="9", width=60, height=50, command=lambda: btn_click('9'))
btn5.grid(row=1, column=2, padx=0, pady=2)

btn6 = customtkinter.CTkButton(button_frame, text="*", width=60, height=50, command=lambda: btn_click('*'))
btn6.grid(row=1, column=3, padx=0, pady=2)

btn7 = customtkinter.CTkButton(button_frame, text="4", width=60, height=50, command=lambda: btn_click('4'))
btn7.grid(row=2, column=0, padx=0, pady=2)

btn8 = customtkinter.CTkButton(button_frame, text="5", width=60, height=50, command=lambda: btn_click('5'))
btn8.grid(row=2, column=1, padx=0, pady=2)

btn9 = customtkinter.CTkButton(button_frame, text="6", width=60, height=50, command=lambda: btn_click('6'))
btn9.grid(row=2, column=2, padx=0, pady=2)

btn10 = customtkinter.CTkButton(button_frame, text="-", width=60, height=50, command=lambda: btn_click('-'))
btn10.grid(row=2, column=3, padx=0, pady=2)

btn11 = customtkinter.CTkButton(button_frame, text="1", width=60, height=50, command=lambda: btn_click('1'))
btn11.grid(row=3, column=0, padx=0, pady=2)

btn12 = customtkinter.CTkButton(button_frame, text="2", width=60, height=50, command=lambda: btn_click('2'))
btn12.grid(row=3, column=1, padx=0, pady=2)

btn13 = customtkinter.CTkButton(button_frame, text="3", width=60, height=50, command=lambda: btn_click('3'))
btn13.grid(row=3, column=2, padx=0, pady=2)

btn14 = customtkinter.CTkButton(button_frame, text="+", width=60, height=50, command=lambda: btn_click('+'))
btn14.grid(row=3, column=3, padx=0, pady=2)

btn15 = customtkinter.CTkButton(button_frame, text="0", width=60, height=50, command=lambda: btn_click('0'))
btn15.grid(row=4, column=0, padx=0, pady=2)

btn16 = customtkinter.CTkButton(button_frame, text=".", width=60, height=50, command=lambda: btn_click('.'))
btn16.grid(row=4, column=1, padx=0, pady=2)

btn17 = customtkinter.CTkButton(button_frame, text="%", width=60, height=50, command=lambda: btn_percentage())
btn17.grid(row=4, column=2, padx=0, pady=2)

btn18 = customtkinter.CTkButton(button_frame, text="Mod", width=60, height=50, command=lambda: btn_click('%'))
btn18.grid(row=4, column=3, padx=0, pady=2)

btn19 = customtkinter.CTkButton(button_frame, text="=", width=185, height=50, command=lambda: btn_equal())
btn19.grid(row=5, column=0, columnspan=3, padx=(0, 2), pady=2)

btn20 = customtkinter.CTkButton(button_frame, text="Del", width=60, height=50, command=lambda: btn_backspace())
btn20.grid(row=5, column=3, padx=0, pady=2)

root.mainloop()
