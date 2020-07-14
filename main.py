import tkinter as tk
from tkinter import messagebox
import os

from pylab import plot, show, xlabel, ylabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from bankaccount import BankAccount

win = tk.Tk()
# Set window size here to '440x640' pixels
win.geometry('460x640')
# Set window title here to 'FedUni Banking'
win.winfo_toplevel().title('FedUni Banking')

# The account number entry and associated variable
account_number_var = tk.StringVar()
account_number_entry = tk.Entry(win, textvariable=account_number_var)
account_number_entry.focus_set()

# The pin number entry and associated variable.
# Note: Modify this to 'show' PIN numbers as asterisks (i.e. **** not 1234)
pin_number_var = tk.StringVar()
account_pin_entry = tk.Entry(win, text='PIN Number', show='*', textvariable=pin_number_var)

# The balance label and associated variable
balance_var = tk.StringVar()
balance_var.set('Balance: $0.00')
balance_label = tk.Label(win, textvariable=balance_var)

# The Entry widget to accept a numerical value to deposit or withdraw
amount_entry = tk.Entry(win)
amount_entry.focus_set()

transaction_text_widget = tk.Text(win, height=10)
# The transaction text widget holds text of the accounts transactions
transaction_text_widget = tk.Text(win, height=10, width=48)

# The bank account object we will work with
account_obj = BankAccount()
# ---------- Button Handlers for Login Screen ----------

def clear_pin_entry(event):
    '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''
    # Clear the pin number entry here
    account_pin_entry.delete(0,"end")

def handle_pin_button(event):
    '''Function to add the number of the button clicked to the PIN number entry via its associated variable.''' 

    if win.focus_get()==account_number_entry:
        account_number_entry.insert("end", event)
    elif win.focus_get()==account_pin_entry:
        account_pin_entry.insert("end", event)

    # Limit to 4 chars in length
    length = len(account_pin_entry.get())
    if length >=4:
        messagebox.showerror("Error", "Not more than 4")

    # Set the new pin number on the pin_number_var
    pin_number_var = '  '
    

def log_in(event):
    '''Function to log in to the banking system using a known account number and PIN.'''
    global balance_var
    global account
    global pin_number_var
    global account_num_entry
    pin_number_var = account_pin_entry.get()
    account = account_number_entry.get()
    # Create the filename from the entered account number with '.txt' on the end
    file = './' + str(account) + '.txt'
    # Try to open the account file for reading
    # Open the account file for reading
    if os.path.exists(file):
        lines = []
        line = [line.rstrip('\n') for line in open(file)]
         # First line is account number
        account_number = line[0]
        # Second line is PIN number, raise exceptionk if the PIN entered doesn't match account PIN read 
        pin = line[1]
        read_line_from_account_file(account)
        if account == account_number and pin_number_var == pin:
            # show accout window
            remove_all_widgets()
            create_account_screen()
        else:
            messagebox.showerror("Error", "Account number and Pin invalid")
    else:
        messagebox.showerror("Error", "Account number doesnot exits")  
        
        # Read third and fourth lines (balance and interest rate) 
        
        # Section to read account transactions from file - start an infinite 'do-while' loop here

            # Attempt to read a line from the account file, break if we've hit the end of the file. If we
            # read a line then it's the transaction type, so read the next line which will be the transaction amount.
            # and then create a tuple from both lines and add it to the account's transaction_list            

        # Close the file now we're finished with it
        #file.close()
        
    # Catch exception if we couldn't open the file or PIN entered did not match account PIN
    
        # Show error messagebox and & reset BankAccount object to default...
        #messagebox.showerror('Error','Invalid PIN')

        #  ...also clear PIN entry and change focus to account number entry
        # pin_number_var = '  '
        
    # Got here without raising an exception? Then we can log in - so remove the widgets and display the account screen
    

# ---------- Button Handlers for Account Screen ----------

def save_and_log_out():
    '''Function  to overwrite the account file with the current state of
       the account object (i.e. including any new transactions), remove
       all widgets and display the login screen.'''
    global account

    # Save the account with any new transactions
    
    # Reset the bank acount object

    # Reset the account number and pin to blank
    account_number_entry = ' '
    account_pin_entry = ' '

    # Remove all widgets and display the login screen again
    remove_all_widgets()
    create_login_screen()

def perform_deposit(event):
    '''Function to add a deposit for the amount in the amount entry to the
       account's transaction list.'''
    global account    
    global amount_entry
    global balance_label
    global balance_var
    account_obj.deposit_funds(int(event), account)

    # Try to increase the account balance and append the deposit to the account file
    
        # Get the cash amount to deposit. Note: We check legality inside account's deposit method
        
        # Deposit funds
        
        # Update the transaction widget with the new transaction by calling account.get_transaction_string()
        # Note: Configure the text widget to be state='normal' first, then delete contents, then instert new
        #       contents, and finally configure back to state='disabled' so it cannot be user edited.

        # Change the balance label to reflect the new balance

        # Clear the amount entry
    
        # Update the interest graph with our new balance

    # Catch and display exception as a 'showerror' messagebox with a title of 'Transaction Error' and the text of the exception
    
      #  messagebox.showerror('Transaction Error','Invalid Transaction')
        
def perform_withdrawal(event):
    '''Function to withdraw the amount in the amount entry from the account balance and add an entry to the transaction list.'''
    global account    
    global amount_entry
    global balance_label
    global balance_var
    account_obj.withdraw_funds(int(event), account)

    # Try to increase the account balance and append the deposit to the account file
    
        # Get the cash amount to deposit. Note: We check legality inside account's withdraw_funds method
        
        # Withdraw funds        

        # Update the transaction widget with the new transaction by calling account.get_transaction_string()
        # Note: Configure the text widget to be state='normal' first, then delete contents, then instert new
        #       contents, and finally configure back to state='disabled' so it cannot be user edited.

        # Change the balance label to reflect the new balance

        # Clear the amount entry

        # Update the interest graph with our new balance

    # Catch and display any returned exception as a messagebox 'showerror'
        

# ---------- Utility functions ----------

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global win
    for widget in win.winfo_children():
        widget.grid_remove()

def read_line_from_account_file(file):
    '''Function to read a line from the accounts file but not the last newline character.
       Note: The account_file must be open to read from for this function to succeed.'''
    global account_file
    # global account_number
    # return account_file.readline()[0:-1]
    file = './' + str(file) + '.txt'
    try:
        line = [line.rstrip('\n') for line in open(file)]
        balance = line[2]
        balance_var.set('Balance $'+balance)
        for l in line[4:]:
            transaction_text_widget.insert(tk.END, l + '\n')
    except:
        pass
    return transaction_text_widget

def plot_interest_graph():
    '''Function to plot the cumulative interest for the next 12 months here.'''

    # YOUR CODE to generate the x and y lists here which will be plotted
    x = range(1,13) # for the 12 months
    y = range(1,13)
    #current balance
##    y = [current_balance]
##
##    for pos,item in enumerate(range(1,12)):
##        new_interest = current_balance * (account.interest_rate/12)
##        current_balance += new_interest
##        y.append(round(current_balance, 2))
    
    # This code to add the plots to the window is a little bit fiddly so you are provided with it.
    # Just make sure you generate a list called 'x' and a list called 'y' and the graph will be plotted correctly.
    figure = Figure(figsize=(5,2), dpi=100)
    figure.suptitle('Cumulative Interest 12 Months')
    a = figure.add_subplot(111)
    a.plot(x, y, marker='o')
    a.grid()
    
    canvas = FigureCanvasTkAgg(figure, master=win)
    canvas.draw()
    graph_widget = canvas.get_tk_widget()
    graph_widget.grid(row=4, column=0, columnspan=5, sticky='nsew')


# ---------- UI Screen Drawing Functions ----------

def create_login_screen():
    global account_number_entry
    global account_pin_entry
    '''Function to create the login screen.'''    
    
    # ----- Row 0 -----
    # 'FedUni Banking' label here. Font size is 32.
    fed = tk.Label(win,text = "FedUni Banking",font=('Arial', 32), anchor='center')
    fed.grid(row=0, column=0, columnspan=3, sticky='nsew')

     # ----- Row 1 -----

    # Acount Number / Pin label here
    accpin = tk.Label(win, text="Account/PIN")
    accpin.grid(row=1,column=0)

    # Account number entry here
    # account_num_entry = tk.Entry(win)
    account_number_entry.grid(row=1,column=1,sticky='nsew')


    # Account pin entry here
    # pin_entry = tk.Entry(win)
    account_pin_entry.grid(row=1,column=2,sticky='nsew')
    
    # ----- Row 2 -----

    # Buttons 1, 2 and 3 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    btn1 = tk.Button(win, text = '1', height=5, width=20, command = lambda:handle_pin_button(1))
    btn1.grid(row=2,column=0, sticky='nsew')
    # btn1.bind('<Button-1>', handle_pin_button)
    
    btn2 = tk.Button(win, text = '2', command = lambda:handle_pin_button(2))
    btn2.grid(row=2,column=1, sticky='nsew')
    # btn2.bind('<Button-1>', handle_pin_button)
    
    btn3 = tk.Button(win, text = '3', command = lambda:handle_pin_button(3))
    btn3.grid(row=2,column=2, sticky='nsew')
    # btn3.bind('<Button-1>', handle_pin_button)

    # ----- Row 3 -----

    # Buttons 4, 5 and 6 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    btn4 = tk.Button(win, text = '4', height=5, width=20, command = lambda:handle_pin_button(4))
    btn4.grid(row=3,column=0, sticky='nsew')
    # btn4.bind('<Button-1>', handle_pin_button)
    
    btn5 = tk.Button(win, text = '5', command = lambda:handle_pin_button(5))
    btn5.grid(row=3,column=1, sticky='nsew')
    # btn5.bind('<Button-1>', handle_pin_button)
    
    btn6 = tk.Button(win, text = '6', command = lambda:handle_pin_button(6))
    btn6.grid(row=3,column=2, sticky='nsew')
    # btn6.bind('<Button-1>', handle_pin_button)

    # ----- Row 4 -----

    # Buttons 7, 8 and 9 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    btn7 = tk.Button(win, text = '7', height=5, width=20,command = lambda:handle_pin_button(7))
    btn7.grid(row=4,column=0, sticky='nsew')
    #btn7.bind('<Button-1>', handle_pin_button(7))
    
    btn8 = tk.Button(win, text = '8', command = lambda:handle_pin_button(8))
    btn8.grid(row=4,column=1, sticky='nsew')
    # btn8.bind('<Button-1>', handle_pin_button)
    
    btn9 = tk.Button(win, text = '9', command = lambda:handle_pin_button(9))
    btn9.grid(row=4,column=2, sticky='nsew')
    # btn9.bind('<Button-1>', handle_pin_button)

    # ----- Row 5 -----

    # Cancel/Clear button here. 'bg' and 'activebackground' should be 'red'. But calls 'clear_pin_entry' function.
    btnC = tk.Button(win, text = 'Clear', height=5, width=20, bg='red')
    btnC.grid(row=5,column=0, sticky='nsew')
    btnC.bind('<Button-1>', clear_pin_entry)
    
    # Button 0 here
    btn0 = tk.Button(win, text = '0', command = lambda:handle_pin_button(0))
    btn0.grid(row=5,column=1, sticky='nsew')
    
    # Login button here. 'bg' and 'activebackground' should be 'green'). Button calls 'log_in' function.
    btnL = tk.Button(win, text = 'Login', bg='green')
    btnL.grid(row=5,column=2, sticky='nsew')
    btnL.bind('<Button-1>', log_in)

    # ----- Set column & row weights -----

    # Set column and row weights. There are 5 columns and 6 rows (0..4 and 0..5 respectively)
    
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)

    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    win.rowconfigure(3, weight=1)
    win.rowconfigure(4, weight=1)
    win.rowconfigure(5, weight=1)

def create_account_screen():
    '''Function to create the account screen.'''
    global amount_text
    global amount_label
    global transaction_text_widget
    global balance_var
    
    # ----- Row 0 -----
    
    # FedUni Banking label here. Font size should be 24.
    display_label = tk.Label(win,text = "FedUni Banking",font=('Arial', 24), anchor='center')
    display_label.grid(row=0, column=0, columnspan=5, sticky='nsew')

    # ----- Row 1 -----

    # Account number label here
    show_account = tk.Label(win, text='Account:'+account,width=20)
    show_account.grid(row=1, column=0,columnspan=2, sticky='nsew')

    # Balance label here
    # amount_label = tk.Label(win, text='Balance:$')
    balance_label.grid(row=1, column=2,sticky='nsew')

    # Log out button here
    logout_button = tk.Button(win,text='Logout', command = save_and_log_out)  
    logout_button.grid(row=1, column=3, columnspan=2, sticky='nsew')

    # ----- Row 2 -----

    # Amount label here
    balance_var = tk.Label(win, text='Amount($)')
    balance_var.grid(row=2, column=0,columnspan=2, sticky='nsew')
    
    # Amount entry here
    amount_entry = tk.Entry(win, text='',width=20)
    amount_entry.grid(row=2, column=2, sticky='nsew')

    # Deposit button here
    deposit_button = tk.Button(win,text='Deposit', command = lambda:perform_deposit(amount_entry.get()))  
    deposit_button.grid(row=2, column=3, sticky='nsew')

    # Withdraw button here
    withdraw_button = tk.Button(win,text='Withdraw', command = lambda:perform_withdrawal(amount_entry.get()))  
    withdraw_button.grid(row=2, column=4, sticky='nsew')

    # NOTE: Bind Deposit and Withdraw buttons via the command attribute to the relevant deposit and withdraw
    #       functions in this file. If we "BIND" these buttons then the button being pressed keeps looking as
    #       if it is still pressed if an exception is raised during the deposit or withdraw operation, which is
    #       offputting.
    
    
    # ----- Row 3 -----
    
    # Declare scrollbar (text_scrollbar) here (BEFORE transaction text widget)
    text_scrollbar = tk.Scrollbar(win)
    
    # Add transaction Text widget and configure to be in 'disabled' mode so it cannot be edited.
    # transaction_text_widget = tk.Text(win, height=10)
    
    transaction_text_widget.configure(state='disabled')
    transaction_text_widget.grid(row=3,column=0,columnspan=5, sticky='nsew')
    #transaction_text_widget.insert('end',(123456,'r').read())
    
    # Note: Set the yscrollcommand to be 'text_scrollbar.set' here so that it actually scrolls the Text widget
    transaction_text_widget.configure(yscrollcommand=text_scrollbar.set)
    #transaction_text_widget.configure(yscrollcommand = text_scrollbar.set)
    
    # Note: When updating the transaction text widget it must be set back to 'normal mode' (i.e. state='normal') for it to be edited
    transaction_text_widget.configure(state = 'normal')
    
    # Now add the scrollbar and set it to change with the yview of the text widget
    text_scrollbar.configure(command=transaction_text_widget.yview)
    text_scrollbar.grid(row=3, column=5, sticky='W')

    # ----- Row 4 - Graph -----

    # Call plot_interest_graph() here to display the graph
    plot_interest_graph()

    # ----- Set column & row weights -----

    # Set column and row weights here - there are 5 rows and 5 columns (numbered 0 through 4 not 1 through 5!)
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.columnconfigure(3, weight=1)
    win.columnconfigure(4, weight=1)

    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    win.rowconfigure(3, weight=1)
    win.rowconfigure(4, weight=1)
    
# ---------- Display Login Screen & Start Main loop ----------

create_login_screen()
win.mainloop()
