#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

import mortgage_functions as mfunc

class Application(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_application()
    
    def create_application(self):
        self.input_frame = InputFrame(self, text = "Input Values")
        self.input_frame.grid(row = 0, column = 0, columnspan = "2",
                              sticky = "ew")
        self.results_frame = ResultsFrame(self)
        self.results_frame.grid(row = 1, column = 0)
        self.data_frame = DataFrame(self)
        self.data_frame.grid(row = 1, column = 1)


class InputFrame(ttk.Labelframe):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_inputs()
    
    def create_inputs(self):
        # Principal
        self.principal_label = ttk.Label(self, text = "Principal (£)",
                                         anchor = "w")
        self.principal_label.grid(row = 0, column = 0, sticky = "ew")
        self.principal_entry = ttk.Entry(self, justify = "right")
        self.principal_entry.grid(row = 1, column = 0, columnspan = "2")
        # Term
        self.term_label = ttk.Label(self, text = "Term (Years)", anchor = "w")
        self.term_label.grid(row = 2, column = 0, sticky = "ew")
        self.term_entry = ttk.Entry(self, justify = "right", width = "5")
        self.term_entry.grid(row = 2, column = 1, sticky = "e")
        # Interest Rate
        self.interest_label = ttk.Label(self, text = "Interest Rate (%)",
                                        anchor = "w")
        self.interest_label.grid(row = 3, column = 0, sticky = "ew")
        self.interest_entry = ttk.Entry(self, justify = "right", width = "5")
        self.interest_entry.grid(row = 3, column = 1, sticky = "e")
        # Introductory Rate
        self.introductory_rate_labelframe_label_widget = ttk.Frame(self)
        self.introductory_rate_label =\
                      ttk.Label(self.introductory_rate_labelframe_label_widget,
                                text = "Introductory Rate")
        self.introductory_rate_label.grid(row = 0, column = 0)
        self.introductory_rate_checkbutton =\
                ttk.Checkbutton(self.introductory_rate_labelframe_label_widget,
                                )
        self.introductory_rate_checkbutton.grid(row = 0, column = 1)
        self.introductory_rate_labelframe = ttk.Labelframe(self,
                  labelwidget = self.introductory_rate_labelframe_label_widget)
        self.introductory_rate_labelframe.grid(row = 0, column = 2,
                                               sticky = "ns", rowspan = "4")
        self.introductory_duration_label =\
                                   ttk.Label(self.introductory_rate_labelframe,
                                             text = "Duration (Months)")
        self.introductory_duration_label.grid(row = 0, column = 0)
        self.introductory_duration_entry =\
                                   ttk.Entry(self.introductory_rate_labelframe,
                                             )
        self.introductory_duration_entry.grid(row = 0, column = 1)
        self.introductory_rate_label =\
                                   ttk.Label(self.introductory_rate_labelframe,
                                             text = "Rate (%)")
        self.introductory_rate_label.grid(row = 1, column = 0)
        self.introductory_rate_entry =\
                                   ttk.Entry(self.introductory_rate_labelframe,
                                             )
        self.introductory_rate_entry.grid(row = 1, column = 1)
        # Overpayment
        self.overpayment_labelframe_label_widget = ttk.Frame(self)
        self.overpayment_label =\
                            ttk.Label(self.overpayment_labelframe_label_widget,
                                      text = "Overpayment")
        self.overpayment_label.grid(row = 0, column = 0)
        self.overpayment_checkbutton =\
                      ttk.Checkbutton(self.overpayment_labelframe_label_widget,
                                      )
        self.overpayment_checkbutton.grid(row = 0, column = 1)
        self.overpayment_labelframe = ttk.Labelframe(self,
                        labelwidget = self.overpayment_labelframe_label_widget)
        self.overpayment_labelframe.grid(row = 0, column = 3, sticky = "ns",
                                         rowspan = "3")
        self.overpayment_label = ttk.Label(self.overpayment_labelframe,
                                           text = "Overpayment Amount")
        self.overpayment_label.grid(row = 0, column = 0)
        self.overpayment_entry = ttk.Entry(self.overpayment_labelframe)
        self.overpayment_entry.grid(row = 1, column = 0)
        # Calculate Button
        self.calculate_button =\
                    ttk.Button(self, text = "Calculate",
                               command = lambda: self.calculate_button_click())
        self.calculate_button.grid(row = 3, column = 3)
    
    def calculate_button_click(self):
#        mainApplication.results_frame
        pass


class ResultsFrame(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_results()
    
    def create_results(self):
        # Monthly Payment
        self.monthly_payment_label = ttk.Label(self,
                                               text = "Monthly Payment (£)",
                                               )
        self.monthly_payment_label.grid(row = 0, column = 0)
        self.monthly_payment_var = tk.DoubleVar(self)
        self.monthly_payment_result = ttk.Label(self,
                                       textvariable = self.monthly_payment_var)
        self.monthly_payment_result.grid(row = 1, column = 0)
        # Total Amount
        self.total_amount_label = ttk.Label(self,
                                            text = "Total Amount Payable (£)",
                                           )
        self.total_amount_label.grid(row = 2, column = 0)
        self.total_amount_var = tk.DoubleVar(self)
        self.total_amount_result = ttk.Label(self,
                                          textvariable = self.total_amount_var)
        self.total_amount_result.grid(row = 3, column = 0)
        # Total Interest
        self.total_interest_label = ttk.Label(self,
                                              text = "Total Interest Paid (£)",
                                              )
        self.total_interest_label.grid(row = 4, column = 0)
        self.total_interest_var = tk.DoubleVar(self)
        self.total_interest_result = ttk.Label(self,
                                        textvariable = self.total_interest_var)
        self.total_interest_result.grid(row = 5, column = 0)
        # Borrowing Factor
        self.borrowing_factor_label = ttk.Label(self,
                                     text = "For each £ borrowed, you pay (£)",
                                     )
        self.borrowing_factor_label.grid(row = 6, column = 0)
        self.borrowing_factor_var = tk.DoubleVar(self)
        self.borrowing_factor_result = ttk.Label(self,
                                      textvariable = self.borrowing_factor_var)
        self.borrowing_factor_result.grid(row = 7, column = 0)
        # Remaining Balance
        self.remaining_balance_frame = ttk.Frame(self)
        self.remaining_balance_frame.grid(row = 8, column = 0)
        
        self.remaining_balance_after_label =\
                        ttk.Label(self.remaining_balance_frame, text = "After")
        self.remaining_balance_after_label.grid(row = 0, column = 0)
        
        self.remaining_balance_years_entry =\
                                        ttk.Entry(self.remaining_balance_frame,
                                                  width = 3)
        self.remaining_balance_years_entry.grid(row = 0, column = 1)
        
        self.remaining_balance_years_label =\
                    ttk.Label(self.remaining_balance_frame, text = "years and")
        self.remaining_balance_years_label.grid(row = 0, column = 2)
        
        self.remaining_balance_months_entry =\
                                        ttk.Entry(self.remaining_balance_frame,
                                                  width = 3)
        self.remaining_balance_months_entry.grid(row = 0, column = 3)
        
        self.remaining_balance_months_label =\
                                        ttk.Label(self.remaining_balance_frame,
                                                  text = "months")
        self.remaining_balance_months_label.grid(row = 0, column = 4)
        
        self.remaining_balance_label = ttk.Label(self,
                                                 text = "the amount owed is")
        self.remaining_balance_label.grid(row = 9, column = 0)
        self.remaining_balance_var = tk.DoubleVar()
        self.remaining_balance_result = ttk.Label(self,
                                     textvariable = self.remaining_balance_var)


class DataFrame(ttk.Notebook):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_data()
    
    def create_data(self):
        self.graph_tab = GraphTab(self)
        self.add(self.graph_tab, text = "Graph")
        self.schedule_tab = ScheduleTab(self)
        self.add(self.schedule_tab, text = "Amortisation Schedule")


class GraphTab(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_graph()
    
    def create_graph(self):
        pass


class ScheduleTab(ttk.Treeview):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_schedule()
    
    def create_schedule(self):
        pass
