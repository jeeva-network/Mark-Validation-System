from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1000x750")
window.resizable(0, 0)

# Window Background Color

window["bg"] = "#ffffff"

# Background Color

bg_1 = "#ffffff"

# Font Color

font_color = "#000000"

# Pass Color

pass_color = "#4cd137"

# Fail Color

fail_color = "#e84118"

# Title for Window

window.title("Student Mark Validation")

# Label Font Style

label_font = ("sans", 20)

# Button and Entry Font Style

font_1 = ("sans", 15)


# Close the Window

def close():
    window.quit()


# Clear UG Entry Field

def clear_1():
    ug_entry_1.delete(0, END)
    ug_entry_2.delete(0, END)
    ug_total.config(text="")
    ug_output_label_1.config(text="")
    ug_output_label_2.config(text="")
    ug_output_label_3.config(text="")


# Clear PG Entry Field

def clear_2():
    pg_entry_1.delete(0, END)
    pg_entry_2.delete(0, END)
    pg_total.config(text="")
    pg_output_label_1.config(text="")
    pg_output_label_2.config(text="")
    pg_output_label_3.config(text="")


# UG Validation

def ug_validation():
    ug_value_1 = not ((ug_entry_1.get() == "") or (ug_entry_2.get() == ""))
    if ug_value_1:
        ug_value_2 = (ug_entry_1.get()).isdigit()
        ug_value_3 = (ug_entry_2.get()).isdigit()
        if ug_value_2 and ug_value_3:
            m_1 = int(ug_entry_1.get())
            m_2 = int(ug_entry_2.get())
            u_1_1 = m_1, m_2
            u_1_2 = sum(u_1_1)

            def ug_total_validation():
                if u_1_2 >= 40:
                    if (m_1 >= 15) and (m_2 >= 20):
                        ug_output_label_3.config(text="PASS", fg=pass_color)
                        ug_total.config(text=u_1_2)
                    else:
                        ug_output_label_3.config(text="FAIL", fg=fail_color)
                        ug_total.config(text=u_1_2)
                else:
                    ug_output_label_3.config(text="FAIL", fg=fail_color)
                    ug_total.config(text=u_1_2)

            def ug_total_validation_1():
                if m_2 >= 20:
                    ug_output_label_2.config(text="PASS", fg=pass_color)
                    ug_total_validation()
                else:
                    ug_output_label_2.config(text="FAIL", fg=fail_color)
                    ug_total_validation()

            if (m_1 <= 50) and (m_2 <= 50):
                if m_1 >= 15:
                    ug_output_label_1.config(text="PASS", fg=pass_color)
                    ug_total_validation_1()
                else:
                    ug_output_label_1.config(text="FAIL", fg=fail_color)
                    ug_total_validation_1()
            else:
                messagebox.showwarning("Warning", "Please Enter Your Valid UG Mark")
        else:
            messagebox.showwarning("Warning", "Please Enter Only Number in the UG Input Field and Without Whitespace")
    else:
        messagebox.showwarning("Warning", "Please Fill Out the all UG Input Field")


# PG Validation


def pg_validation():
    pg_value_1 = not ((pg_entry_1.get() == "") or (pg_entry_2.get() == ""))
    if pg_value_1:
        pg_value_2 = (pg_entry_1.get()).isdigit()
        pg_value_3 = (pg_entry_2.get()).isdigit()
        if pg_value_2 and pg_value_3:
            m_1_1 = int(pg_entry_1.get())
            m_1_2 = int(pg_entry_2.get())
            p_1_1 = m_1_1, m_1_2
            p_1_2 = sum(p_1_1)

            def pg_total_validation():
                if p_1_2 >= 50:
                    if (m_1_1 >= 20) and (m_1_2 >= 25):
                        pg_output_label_3.config(text="PASS", fg=pass_color)
                        pg_total.config(text=p_1_2)
                    else:
                        pg_output_label_3.config(text="FAIL", fg=fail_color)
                        pg_total.config(text=p_1_2)
                else:
                    pg_output_label_3.config(text="FAIL", fg=fail_color)
                    pg_total.config(text=p_1_2)

            def pg_total_validation_1():
                if m_1_2 >= 25:
                    pg_output_label_2.config(text="PASS", fg=pass_color)
                    pg_total_validation()
                else:
                    pg_output_label_2.config(text="FAIL", fg=fail_color)
                    pg_total_validation()

            if (m_1_1 <= 50) and (m_1_2 <= 50):
                if m_1_1 >= 20:
                    pg_output_label_1.config(text="PASS", fg=pass_color)
                    pg_total_validation_1()
                else:
                    pg_output_label_1.config(text="FAIL", fg=fail_color)
                    pg_total_validation_1()
            else:
                messagebox.showwarning("Warning", "Please Enter Your Valid PG Mark")
        else:
            messagebox.showwarning("Warning", "Please Enter Only Number in the PG Input Field and Without Whitespace")
    else:
        messagebox.showwarning("Warning", "Please Fill Out the all PG Input Field")


# Create Frames


frame_1 = Frame(window, highlightbackground="black", highlightthickness=1, width=400, height=550, bg=bg_1)
frame_1.place(x=70, y=50)

frame_2 = Frame(window, highlightbackground="black", highlightthickness=1, width=400, height=550, bg=bg_1)
frame_2.place(x=525, y=50)

# Frame 1 Widgets

ug_label_1 = Label(frame_1, text="UG", width=5, height=2, bg=bg_1, fg=font_color, font=label_font)
ug_label_1.place(x=150, y=10)
ug_label_2 = Label(frame_1, text="CIA", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_label_2.place(x=25, y=130)
ug_label_3 = Label(frame_1, text="EOS", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_label_3.place(x=30, y=230)
ug_label_4 = Label(frame_1, text="TOTAL", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_label_4.place(x=40, y=330)
ug_u_1 = Label(frame_1, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_u_1.place(x=150, y=115)
ug_u_2 = Label(frame_1, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_u_2.place(x=150, y=215)
ug_u_3 = Label(frame_1, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
ug_u_3.place(x=150, y=315)
ug_output_label_1 = Label(frame_1, bg=bg_1, font=font_1)
ug_output_label_1.place(x=270, y=85, width=65, height=40)
ug_output_label_2 = Label(frame_1, bg=bg_1, font=font_1)
ug_output_label_2.place(x=270, y=185, width=65, height=40)
ug_output_label_3 = Label(frame_1, bg=bg_1, font=font_1)
ug_output_label_3.place(x=270, y=285, width=65, height=40)
ug_entry_1 = Entry(frame_1, fg=font_color, font=font_1)
ug_entry_1.place(x=250, y=130, width=100, height=40)
ug_entry_2 = Entry(frame_1, fg=font_color, font=font_1)
ug_entry_2.place(x=250, y=230, width=100, height=40)
ug_total = Label(frame_1, fg=font_color, bg=bg_1, font=font_1)
ug_total.place(x=250, y=330, width=100, height=40)
ug_button_1 = Button(frame_1, text="CLEAR", font=font_1, command=clear_1, fg=font_color, bg=bg_1)
ug_button_1.place(x=80, y=440)
ug_button_2 = Button(frame_1, text="VALIDATE", font=font_1, fg=font_color, bg=bg_1, command=ug_validation)
ug_button_2.place(x=200, y=440)

# Frame 2 Widgets

pg_label_1 = Label(frame_2, text="PG", width=5, height=2, bg=bg_1, fg=font_color, font=label_font)
pg_label_1.place(x=150, y=10)
pg_label_2 = Label(frame_2, text="CIA", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_label_2.place(x=25, y=130)
pg_label_3 = Label(frame_2, text="EOS", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_label_3.place(x=30, y=230)
pg_label_4 = Label(frame_2, text="TOTAL", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_label_4.place(x=40, y=330)
pg_u_1 = Label(frame_2, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_u_1.place(x=150, y=115)
pg_u_2 = Label(frame_2, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_u_2.place(x=150, y=215)
pg_u_3 = Label(frame_2, text="_", width=5, height=2, bg=bg_1, fg=font_color, font=font_1)
pg_u_3.place(x=150, y=315)
pg_output_label_1 = Label(frame_2, bg=bg_1, font=font_1)
pg_output_label_1.place(x=270, y=85, width=65, height=40)
pg_output_label_2 = Label(frame_2, bg=bg_1, font=font_1)
pg_output_label_2.place(x=270, y=185, width=65, height=40)
pg_output_label_3 = Label(frame_2, bg=bg_1, font=font_1)
pg_output_label_3.place(x=270, y=285, width=65, height=40)
pg_entry_1 = Entry(frame_2, fg=font_color, font=font_1)
pg_entry_1.place(x=250, y=130, width=100, height=40)
pg_entry_2 = Entry(frame_2, fg=font_color, font=font_1)
pg_entry_2.place(x=250, y=230, width=100, height=40)
pg_total = Label(frame_2, fg=font_color, bg=bg_1, font=font_1)
pg_total.place(x=250, y=330, width=100, height=40)
pg_button_1 = Button(frame_2, text="CLEAR", font=font_1, command=clear_2, fg=font_color, bg=bg_1)
pg_button_1.place(x=80, y=440)
pg_button_2 = Button(frame_2, text="VALIDATE", font=font_1, fg=font_color, bg=bg_1, command=pg_validation)
pg_button_2.place(x=200, y=440)


# Exit to Window

def close_1():
    window.quit()


exit_window = Button(window, text="EXIT", font=font_1, fg=font_color, bg=bg_1, command=close_1)
exit_window.place(x=800, y=650)

window.mainloop()
