#!usr/bin/env python3

#------------------------------------------------------------#
#
#
#
#
#------------------------------------------------------------#

import tkinter as tk
import tkinter.ttk as ttk
import numpy as numpy

root=tk.Tk()
root.title('Mortgage Calculator')

############################
## Main Application frame ##
############################

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master = master)
        self.pack()
        self.createApplication()

    def createApplication(self):
        # Create instance of user input frame in main application
        self.uIF = userInputFrame(self, text = "Mortgage Values",
                                  labelanchor = "nw")
        self.uIF.pack(anchor = "w", expand = 1)
        # Create instance of tabbed output frame in main application
        self.oF = outputFrame(self)
        self.oF.pack(side = "left", expand = 1)

####################################################        
## Frame to hold information provided by the user ##
####################################################
        
class userInputFrame(ttk.LabelFrame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        ## Create Input Widgets
        self.createWidgets()
                
    def createWidgets(self):
        ## Create Initial Value Variables
        self.initprin = tk.StringVar()
        self.initprin.set("252994")
        self.initterm = tk.StringVar()
        self.initterm.set("30")
        self.initintrate = tk.StringVar()
        self.initintrate.set("1.39")
        # Principal
        self.principalFrame = ttk.Frame(self)
        self.principalFrame.pack(side = "left")
        self.principalLabel = ttk.Label(self.principalFrame,
                                       text = "Principal (£): ")
        self.principalLabel.pack(anchor = "w")
        self.principalEntry = ttk.Entry(self.principalFrame,
                                        textvariable = self.initprin,
                                        justify = "right", width = "10")
        self.principalEntry.pack(anchor = "w")
        # Term
        self.termFrame = ttk.Frame(self)
        self.termFrame.pack(side = "left")
        self.termLabel = ttk.Label(self.termFrame, text="Term (Years):")
        self.termLabel.pack(anchor = "w")
        self.termEntry = ttk.Entry(self.termFrame,
                                   textvariable = self.initterm,
                                   justify = "right", width = "10")
        self.termEntry.pack(anchor = "w")
        # Interest Rate
        self.interestFrame = ttk.Frame(self)
        self.interestFrame.pack(side = "left")
        self.intrateLabel = ttk.Label(self.interestFrame,
                                      text="Interest Rate (%):")
        self.intrateLabel.pack(anchor = "w")
        self.intrateEntry = ttk.Entry(self.interestFrame,
                                      textvariable = self.initintrate,
                                      justify = "right", width = "10")
        self.intrateEntry.pack(anchor = "w")
        # Calculate button
        self.calcButton = ttk.Button(self, text = "Calculate",
                                     command = self.calcButtonUpdate)
        self.calcButton.pack(side = "left", anchor = "s")

    def calcButtonUpdate(self):
        ## Update Normal Mortgage Tab Parameters
        self.P = float(str(self.principalEntry.get()))
        self.r = float(str(self.intrateEntry.get()))
        self.t = float(str(self.termEntry.get()))
        
        norMor = self.master.oF.normalMortgage
        norMor.monPay.set(numpy.pmt(self.r/1200, self.t*12,
                                    self.P, 0 ,0))
        norMor.totPay.set(float(norMor.monPay.get())*self.t*12)
        norMor.totInt.set(float(norMor.totPay.get())+self.P)
        norMor.intFac.set(float(norMor.totPay.get())/self.P)

        ## Update Introductory Rate Mortgage Tab Parameters
        
#################################################
## Frame to hold information output by program ##
#################################################
        
class outputFrame(ttk.Notebook):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        self.createWidgets()

    ## add tabs to Notebook
    def createWidgets(self):
        self.normalMortgage = normalTab(self)
        self.add(self.normalMortgage,
                 text = "Normal Mortgage")
        
        self.introductoryMortgage = introductoryTab(self)
        self.add(self.introductoryMortgage,
                 text = "Introductory Rate Mortgage")
        
        self.overpaymentMortgage = overpaymentTab(self)
        self.add(self.overpaymentMortgage,
                 text = "Mortgage Overpayment")

## Normal Mortgage Tab
class normalTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        self.createVariables()
        self.createWidgets()

    def createVariables(self):
        self.monPay = tk.StringVar()
        self.totPay = tk.StringVar()
        self.totInt = tk.StringVar()
        self.intFac = tk.StringVar()

    def createWidgets(self):
        self.monthlyPaymentLabel = ttk.Label(
            self, text = "Monthly Payment Amount (£)")
        self.monthlyPaymentLabel.pack(anchor = "w")
        self.monthlyPaymentValue = ttk.Label(self,
                                             textvariable = self.monPay)
        self.monthlyPaymentValue.pack()
        self.totalPayableLabel = ttk.Label(
            self, text = "Total Amount Payable (£)")
        self.totalPayableLabel.pack(anchor = "w")
        self.totalPayableValue = ttk.Label(self,
                                           textvariable = self.totPay)
        self.totalPayableValue.pack()
        self.totalInterestLabel = ttk.Label(
            self, text = "Total Interest Paid (£)")
        self.totalInterestLabel.pack(anchor = "w")
        self.totalInterestValue = ttk.Label(self,
                                            textvariable = self.totInt)
        self.totalInterestValue.pack()
        self.factorLabel = ttk.Label(
            self, text = "For each £ borrowed, you pay")
        self.factorLabel.pack(anchor = "w")
        self.factorValue = ttk.Label(self,
                                     textvariable = self.intFac)
        self.factorValue.pack()

## Introductory Rate Mortgage Tab
class introductoryTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        pass

## Overpayment Tab
class overpaymentTab(ttk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master = master, *args, **kwargs)
        self.createWidgets()

    def createWidgets(self):
        pass

##app = Application(root)
##app.mainloop()

if __name__ == '__main__':
    app = Application(root)
    app.mainloop()
