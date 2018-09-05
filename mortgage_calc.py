#!/usr/bin/python3

import tkinter as tk
import matplotlib
from tkinter import ttk

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Mortgage Calculator")

####Custom ttk styles
style = ttk.Style()
style.configure("TLabel", padding=4)
style.configure("TEntry", padding="3", width="12", padx = 10)

def mortMonPay(P, r, n):
    """Returns the monthly payment for a mortgage. P = Principal amount,
       r is yearly interest rate and, n is length of term in years."""

    r = r/1200
    n = n*12

    A = P*(r*((1+r)**n))/(((1+r)**n)-1)
    return(A)

def morTotPaid(F, I, T, L):
    """Returns overall total amount paid.
       F is full price payment in £,
       I is interim term payment in £,
       T is total mortgage term in years,
       L is length of interim term in years."""

    A = (L*12*I) + ((T-L)*12*F)
    return(A)

def morRemPrin(P, r, n, x):
    """Returns remaining principal after defined time.
       P is principal amount in £,
       r is yearly interest rate
       n is length of payment in years
       x is the monthly payment amount in £"""

    r = r/1200
##    n = n*12

    A = (P*(1+r)**n) - (x*((((1+r)**n)-1)/r))
    return(A)

def mortFunc(P, r, i, n, L, O):
    """Returns a list with mortgage values.
       P is Principal amount in £,
       r is yearly interest rate,
       i is the interim yearly interest rate,
       n is length of term in years,
       L is the interim term length in years,
       O is the overpayment amount in £ per month."""

    fullpay = mortMonPay(P, r, n)

    interimpay = mortMonPay(P, i, n)

    if L>0:
        rembal = morRemPrin(P, i, L, interimpay)
        increasepay = mortMonPay(rembal, r, n-L)
        totalpaid = morTotPaid(increasepay, interimpay, n, L)
    else:
        rembal = None
        increasepay = None
        totalpaid = morTotPaid(fullpay,0, n, 0)

    mlist = [fullpay,interimpay,increasepay,totalpaid,rembal]
    print(mlist)

def calcmortpay(*args):
    try:
        A = float(principal_entry.get())
        B = float(term_entry.get())
        C = float(fullRate_entry.get())

        Z = [A,C,B] ## to calculate monthly payment

        D = float(after_years.get())
        E = float(after_months.get())
        F = D*12+E

        Y = [A, C, F,mortMonPay(*Z)] ## to calculate remaining principle after n time

##      calculations for calculate button press event
        monthlypayment = Y[3]
        totalpaid = monthlypayment*B*12
        totalinterest = totalpaid-A
        payratio = totalpaid/A
        afterprincipal = morRemPrin(*Y)

##      set text variables to calculation results        
        abcd.set(monthlypayment)
        totpay.set(totalpaid)
        totint.set(totalinterest)
        payrat.set(payratio)
        nortabplot.updateplot()
        afterprin.set(afterprincipal)
    except ValueError:
        pass
    
##matt = [252994,3.74,1.39,30,26/12,1]
##mortFunc(*matt)

class mortgage_app(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        inputframe = input_frame()
        inputframe.pack()
        resultsframe = results_frame()
        resultsframe.pack()

class input_frame(ttk.LabelFrame):

    def __init__(self, master = None):
        super().__init__(master)
        self.config(text="Mortgage Values", padding=10)
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        principal_label = ttk.Label(self, text="Principal (£)")
        principal_label.pack(side = "left")
        global principal_entry
        principal_entry = ttk.Entry(self)
        principal_entry.insert(0,100000)
        principal_entry.pack(side = "left")
        term_label = ttk.Label(self, text="Term (Years)")
        term_label.pack(side = "left")
        global term_entry
        term_entry = ttk.Entry(self)
        term_entry.insert(0,25)
        term_entry.pack(side = "left")
        fullRate_label = ttk.Label(self, text="Interest Rate (%)")
        fullRate_label.pack(side = "left")
        global fullRate_entry
        fullRate_entry = ttk.Entry(self)
        fullRate_entry.insert(0,1)
        fullRate_entry.pack(side = "left")
        calculate_button = ttk.Button(self, text="Calculate", command=calcmortpay)
        calculate_button.pack()
##        initterm_label = ttk.Label(self, text="Introductory Term (Years)")
##        initterm_label.pack(side = "left")
##        initterm_entry = ttk.Entry(self)
##        initterm_entry.pack(side = "left")
        
        
class results_frame(ttk.Notebook):

    def __init__(self, master = None):
        super().__init__(master)
        normaltab = normal_tab()
        self.add(normaltab, text='Normal Mortgage')
        introdtab = introductory_tab()
        self.add(introdtab, text='Introductory Rate Mortgage')
        overpaytab = overpayment_tab()
        self.add(overpaytab, text='Mortgage Overpayment')


class normal_tab(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        nortabdata = normaltab_data(self)
        nortabdata.pack(side = "left")
        global nortabplot
        nortabplot = normaltab_plot(self)
        nortabplot.pack(side = "left")

class normaltab_data(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.create_widgets()
        
    def create_widgets(self):
        monpay_label = ttk.Label(self, text="Monthly Payment:")
        monpay_label.pack()
        global abcd
        abcd = tk.StringVar()
        monpayresult_label = ttk.Label(self, textvariable = abcd)
        monpayresult_label.pack()
        totpay_label = ttk.Label(self, text="Total Amount Payable:")
        totpay_label.pack()
        global totpay
        totpay = tk.StringVar()        
        totpayresult_label = ttk.Label(self, textvariable = totpay)
        totpayresult_label.pack()
        totint_label = ttk.Label(self, text="Total Interest Paid:")
        totint_label.pack()
        global totint
        totint = tk.StringVar()        
        totintresult_label = ttk.Label(self, textvariable = totint)
        totintresult_label.pack()
        payrat_label = ttk.Label(self, text="For each £ borrowed, you pay:")
        payrat_label.pack()
        global payrat
        payrat = tk.StringVar()        
        payrat_result = ttk.Label(self, textvariable = payrat)
        payrat_result.pack()

        
        ttk.Label(self, text = "After").pack()
        global after_years
        after_years = ttk.Entry(self)
        after_years.insert(0,0)
        after_years.pack()
        ttk.Label(self, text = "years and").pack()
        global after_months
        after_months = ttk.Entry(self)
        after_months.insert(0,0)
        after_months.pack()
        ttk.Label(self, text = "months, the amount owed is:").pack()

        global afterprin
        afterprin = tk.StringVar()
        afterprin_result = ttk.Label(self, textvariable = afterprin)
        afterprin_result.pack()


class normaltab_plot(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.pack
        self.initialplot()


    def initialplot(self):
        
        xvalues = []
        yvalues = []
        
        f = Figure(figsize=(6,5), dpi=90)
        
        self.a = f.add_subplot(1,1,1)
        self.a.plot(xvalues,yvalues)

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack()

    def updateplot(self):

        xvalues = []
        yvalues = []
        
        prin = int(principal_entry.get())
        term = int(term_entry.get())
        rate = float(fullRate_entry.get())

        A = [prin, rate, term]

        payment = mortMonPay(*A)

        for i in range((term*12)+1):
            xvalues.append(i)

            B = [prin, rate, i, payment]

            C= morRemPrin(*B)
            yvalues.append(C)

        self.a.cla()
        self.a.plot(xvalues,yvalues)
        self.canvas.show()        

class introductory_tab(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        pass


class overpayment_tab(ttk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        pass

root.bind('<Return>', calcmortpay)
app = mortgage_app(master = root)
app.mainloop()
