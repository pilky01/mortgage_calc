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
        self.input_frame.grid(row = 0, column = 0, columnspan = "2")
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
        self.term_label = ttk.Label(self, text = "Term (Years)",
                                    anchor = "w")
        self.term_label.grid(row = 2, column = 0, sticky = "ew")
        self.term_entry = ttk.Entry(self, justify = "right", width = "5")
        self.term_entry.grid(row = 2, column = 1, sticky = "e")
        # Interest Rate
        self.interest_label = ttk.Label(self, text = "Interest Rate (%)",
                                        anchor = "w")
        self.interest_label.grid(row = 3, column = 0, sticky = "ew")
        self.interest_entry = ttk.Entry(self, justify = "right",
                                        width = "5")
        self.interest_entry.grid(row = 3, column = 1, sticky = "e")


class ResultsFrame(ttk.Frame):
    
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_results()
    
    def create_results(self):
        pass


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
