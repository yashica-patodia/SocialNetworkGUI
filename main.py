from tkinter import *
from ast import literal_eval
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


# create all of the main containers
def createLayout(root):
    top_frame = Frame(root, bg='cyan', width=450, height=25, pady=3)
    center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
    btm_frame1 = Frame(root, bg='white', width=450, height=35, pady=3)
    btm_frame2 = Frame(root, bg='black', width=450, height=35, pady=3)
    # btm_frame3=Frame(root, bg='white', width=450, height=35, pady=3)
    # btm_frame4 = Frame(root, bg='black', width=450, height=35, pady=3)

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame1.grid(row=3, sticky="ew")
    btm_frame2.grid(row=4, sticky="ew")
    # btm_frame3.grid(row=5, sticky="ew")
    # btm_frame4.grid(row=6, sticky="ew")

    # create the widgets for the top frame
    model_label = Label(top_frame, text='Expression Evaluator')

    # layout the widgets in the top frame
    model_label.pack(padx=20)
    # model_label.grid(row=0, column=4, columnspan=2)

    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg='blue', width=100, height=190)
    ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
    ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)
    btm_left1 = Frame(btm_frame1, bg="white", width=400, height=35)
    btm_right1 = Frame(btm_frame1, bg="white", width=400, height=35, padx=3, pady=3)

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")
    btm_left1.grid(row=0, column=0, sticky="nsew")
    btm_right1.grid(row=0, column=2, sticky="nsew")
    width_label = Label(ctr_mid, text='Expression(x):')
    # x_label = Label(ctr_mid, text="X:")
    length_label = Label(ctr_mid, text='Lower Range:')
    breadth_label = Label(ctr_mid, text='Upper Range:')

    # taking input
    entry_E = Entry(ctr_mid, background="orange")
    # entry_X = Entry(ctr_mid, background="orange")
    entry_L = Entry(ctr_mid, background="orange")
    entry_B = Entry(ctr_mid, background="orange")

    # Inserting the command
    entry_E.insert(0, "Enter the expression")
    # entry_X.insert(0, "Enter the value of X")
    entry_L.insert(0, "Enter the lower bound ")
    entry_B.insert(0, "Enter the upper bound ")
    # entry_E.configure(state="readonly")

    # Storing input
    expression = entry_E.get()
    # x_value = entry_X.get()
    lower_bound = entry_L.get()
    upper_bound = entry_B.get()

    # Place the labels
    width_label.grid(row=1, column=0, padx=5, pady=10)
    # x_label.grid(row=3, column=0, padx=5, pady=10)
    length_label.grid(row=3, column=0, padx=5, pady=10)
    breadth_label.grid(row=5, column=0, padx=5, pady=10)
    # submit_label.grid(row=12,column=5,padx=5,pady=10)
    entry_E.grid(row=1, column=1, padx=5, pady=10)
    # entry_X.grid(row=3, column=1, padx=5, pady=10)
    entry_L.grid(row=3, column=1, padx=5, pady=10)
    entry_B.grid(row=5, column=1, padx=5, pady=10)

    # Creating label for first Bottom window
    output_label = Label(btm_left1, text='OUTPUT')
    # output_label.pack()
    output_label.grid(row=0, column=0, padx=200)

    # Creating label for third Bottom window
    plot_label = Label(btm_right1, text='')
    # plot_label.pack()
    plot_label.grid(row=0, column=0, padx=150)

    # Creating label for second Bottom window

    btm_frame2.grid_rowconfigure(0, weight=1)
    btm_frame2.grid_columnconfigure(1, weight=1)
    # btm_frame4.grid_rowconfigure(0, weight=1)
    # btm_frame4.grid_columnconfigure(1, weight=1)
    # btm_mid4=Frame(btm_frame4,bg='black',width=450,height=190,padx=3,pady=3)
    btm_left = Frame(btm_frame2, bg='black', width=400, height=300)
    # btm_mid = Frame(btm_frame2, bg='white', width=250, height=300, padx=3, pady=3)
    btm_right = Frame(btm_frame2, bg='white', width=400, height=300, padx=3, pady=3)
    btm_left.grid(row=0, column=0, sticky="ns")
    # btm_mid.grid(row=0, column=1, sticky="nsew")
    btm_right.grid(row=0, column=2, sticky="ns")

    submit_label = Button(ctr_mid, text="Submit", bg='black', fg='white',
                          command=lambda: evaluate(root, entry_E, entry_L, entry_B, btm_left,
                                                   btm_right))
    submit_label.grid(row=8, column=0, padx=5, pady=10)
    plot_label = Button(ctr_mid, text="PLOT", bg='black', fg='white',
                        command=lambda: plot(root, entry_E, entry_L, entry_B, btm_left,
                                             btm_right))
    plot_label.grid(row=9, column=0, padx=5, pady=10)

    # evaluate(root, expression, x_value, lower_bound, upper_bound)


def evaluate(root, entry_E, entry_L, entry_B, btm_left, btm_right):
    expression = entry_E.get()
    # x_value = entry_X.get()
    lower_bound = entry_L.get()
    upper_bound = entry_B.get()
    expression.strip()
    # x_value.strip()
    lower_bound.strip()
    upper_bound.strip()
    # x = int(x_value)
    lb = int(lower_bound)
    ub = int(upper_bound)
    output1 = Text(btm_left, width=40, height=10, padx=5, pady=10)
    output1.grid(row=0, column=0, padx=5, pady=10)
    index = 0
    for x in np.linspace(lb, ub, 10):
        expr = expression.strip('\n')
        y = eval(expr)
        print(expr + ' ( ' + str(x) + ' ) ' + ' = ' + str(y))
        output1.insert(END, expr + ' ( ' + str(x) + ' ) ' + ' = ' + str(y) + '\n')
        index += 1


def plot(root, entry_E, entry_L, entry_B, btm_left, btm_right):
    expression = entry_E.get()
    # x_value = entry_X.get()
    lower_bound = entry_L.get()
    upper_bound = entry_B.get()
    expression.strip()
    # x_value.strip()
    lower_bound.strip()
    upper_bound.strip()
    # x = int(x_value)
    lb = int(lower_bound)
    ub = int(upper_bound)
    y = []
    for x in np.linspace(lb, ub, 100):
        expr = expression.strip('\n')
        y_value = eval(expr)
        y.append(y_value)
    fig = Figure(figsize=(5, 5),
                 dpi=100)
    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig,
                               master=btm_right)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   btm_right)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


if __name__ == "__main__":
    # create a GUI window
    root = Tk()
    root.title('Expression Evaluator')
    root.geometry('{}x{}'.format(800, 800))
    createLayout(root)

    root.mainloop()
# create an exit button
# create a message box
# increase height of window
