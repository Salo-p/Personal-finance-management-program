from tkinter import *
from tkinter import ttk

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Entry Form")

        self.label_0 = Label(self.root, text="Login Page", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)
        self.label_1 = Label(self.root, text="Full Name:", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=240, y=130)
        self.label_2 = Label(self.root, text="Password:", width=20, font=("bold", 10))
        self.label_2.place(x=80, y=180)
        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=240, y=180)
        self.label_3 = Label(self.root, text="Age:", width=20, font=("bold", 10))
        self.label_3.place(x=100, y=220)
        self.entry_3 = Entry(self.root)
        self.entry_3.place(x=240, y=220)
        Button(self.root, text='Submit', width=20, bg='blue', fg='white', command=self.submit_login).place(x=180, y=380)

    def creating_text_file(self):
        save_file = open("Accounts.txt", "a")
        title = "Accounts"
        line = "\n"
        save_file.write(title)
        save_file.write(line)
        save_file.close()

    def appending_to_text_file(self):
        save_file = open("Accounts.txt", "a")
        save_file.write(str(self.entry_1.get()))
        save_file.write("\n")
        save_file.write(str(self.entry_2.get()))
        save_file.write("\n")
        save_file.write(str(self.entry_3.get()))
        save_file.write("\n")
        save_file.close()

    def submit_login(self):
        self.appending_to_text_file()
        open_menu_window = OpenMenuWindow(self.root)

class OpenMenuWindow:
    def __init__(self, root):
        self.root = root
        self.menu_window = Toplevel()
        self.menu_window.title("Menu Page")
        self.menu_window.geometry("400x400")

        self.menubar = Menu(self.menu_window)
        self.menu_window.config(menu=self.menubar)

        # Budget menu
        budget_menu = Menu(self.menubar, tearoff=0)
        budget_menu.add_command(label="View Budget")
        budget_menu.add_command(label="Adjust Budget", command=self.open_budget_tracker)
        self.menubar.add_cascade(label="Budget", menu=budget_menu)

        # Expense menu
        expense_menu = Menu(self.menubar, tearoff=0)
        expense_menu.add_command(label="Add Expense")
        expense_menu.add_command(label="View Expenses")
        self.menubar.add_cascade(label="Expense", menu=expense_menu)
        # Goals menu
        goals_menu = Menu(self.menubar, tearoff=0)
        goals_menu.add_command(label="Set Goals")
        goals_menu.add_command(label="View Goals")
        self.menubar.add_cascade(label="Goals", menu=goals_menu)
        # Investment menu
        investment_menu = Menu(self.menubar, tearoff=0)
        investment_menu.add_command(label="Add Investment")
        investment_menu.add_command(label="View Investments")
        self.menubar.add_cascade(label="Investment", menu=investment_menu)
        # Setting menu
        setting_menu = Menu(self.menubar, tearoff=0)
        setting_menu.add_command(label="Account Settings")
        setting_menu.add_command(label="Notification Settings")
        self.menubar.add_cascade(label="Setting", menu=setting_menu)

    def open_budget_tracker(self):
        self.menu_window.withdraw()
        budget_window = Toplevel()
        budget_window.title("Budget Tracker")
        budget_window.geometry("400x400")
        month_label = Label(budget_window, text="Month")
        month_label.grid(row=2, column=0, sticky=W)
        spend_label = Label(budget_window, text="Amount spent")
        spend_label.grid(row=3, column=0, sticky=W)
        n = StringVar()
        monthchoosen = ttk.Combobox(budget_window, textvariable=n)
        monthchoosen['values'] = (
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December')
        monthchoosen.grid(row=2, column=1)
        monthchoosen.current(0)
        spend_var = IntVar()
        spend_entry = Entry(budget_window, textvariable=spend_var).grid(row=3, column=1)
        spent_dict = {}

        def add_data():
            val = spend_var.get()
            spent_dict[n.get()] = val

        btn_add = Button(budget_window, text="Add", command=add_data)
        btn_add.grid(row=4, column=0, columnspan=2)

        def sort_list():
            sorted_dict = sorted(spent_dict.items(), key=lambda x: x[1])
            labelS = Label(budget_window, text=sorted_dict)
            labelS.grid(row=7, column=0)

        def get_average():
            sum_val = 0
            n_val = 0
            for key, values in spent_dict.items():
                sum_val += values
                n_val += 1
            if n_val > 0:
                average = sum_val / n_val
                average_label = Label(budget_window, text=str(average))
                average_label.grid(row=8, column=0)

        btn_sort = Button(budget_window, text="Sort", command=sort_list).grid(row=5, column=0, columnspan=2)
        btn_average = Button(budget_window, text="Average", command=get_average).grid(row=6, column=0, columnspan=2)


root = Tk()
login_page = LoginPage(root)
root.mainloop()
print("Admission created...")
