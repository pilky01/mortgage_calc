#!usr/bin/python3

#------------------------------------------------------------#
#
#
#
#
#------------------------------------------------------------#

import tkinter as tk
import tkinter.ttk as ttk

root=tk.Tk()
root.title('Mortgage Calculator')

############################
## Main Application frame ##
############################

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createApplication()

    def createApplication(self):
        # Create instance of user input frame in main application
        uIF = userInputFrame(self, text="Mortgage Values",
                                  labelanchor="nw").pack()
        # Create instance of tabbed output frame in main application
        oF = outputFrame(self
                         ).pack(side = "left")

####################################################        
## Frame to hold information provided by the user ##
####################################################
        
class userInputFrame(ttk.LabelFrame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        principal = 252994
        term = 30
        interestrate = 1.39
        self.createWidgets()
        
    def createWidgets(self):
        # Principal
        principalFrame = ttk.Frame(self)
        principalFrame.pack(side = "left")
        principalLabel = ttk.Label(
            principalFrame, text = "Principal (£): ", justify = "left"
            ).pack(expand = 1)#(side = "left")
        principalEntry = ttk.Entry(
            principalFrame, textvariable="252,994"
            ).pack()#side = "left")
        # Term
        termFrame = ttk.Frame(self)
        termFrame.pack(side = "left")
        termLabel = ttk.Label(termFrame, text="Term (Years):"
                              ).pack()#side = "left")
        termEntry = ttk.Entry(termFrame
                              ).pack()#side = "left")
        # Interest Rate
        interestFrame = ttk.Frame(self)
        interestFrame.pack(side = "left")
        intrateLabel = ttk.Label(interestFrame, text="Interest Rate (%):"
                                 ).pack()#side = "left")
        intrateEntry = ttk.Entry(interestFrame
                                 ).pack()#side = "left")
        
#################################################
## Frame to hold information output by program ##
#################################################
        
class outputFrame(ttk.Notebook):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.createWidgets()

    ## add tabs to Notebook
    def createWidgets(self):
        normalMortgage = normalTab(self)
        self.add(normalMortgage, text = "Normal Mortgage")
        
        introductoryMortgage = introductoryTab(self)
        self.add(introductoryMortgage, text = "Introductory Rate Mortgage")
        
        overpaymentMortgage = overpaymentTab(self)
        self.add(overpaymentMortgage, text = "Mortgage Overpayment")

## Normal Mortgage Tab
class normalTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        monthlyPaymentLabel = ttk.Label(
            self, text = "Monthly Payment Amount (£)").pack()
        monthlyPaymentValue = ttk.Label(
            self).pack()
        totalPayableLabel = ttk.Label(
            self, text = "Total Amount Payable (£)").pack()
        totalPayableValue = ttk.Label(
            self).pack()
        totalInterestLabel = ttk.Label(
            self, text = "Total Interest Paid (£)").pack()
        totalInterestLabel = ttk.Label(
            self).pack()
        factorLabel = ttk.Label(
            self, text = "For each £ borrowed, you pay").pack()
        factorValue = ttk.Label(
            self).pack()
##        monthly payment
##        total amount payable
##        total interest paid
##        for each £ borrowed, you pay

## Introductory Rate Mortgage Tab
class introductoryTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        pass

## Overpayment Tab
class overpaymentTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        pass

app = Application(root)
app.mainloop()

##if __name__ == '__main__':
##    app.mainloop()
