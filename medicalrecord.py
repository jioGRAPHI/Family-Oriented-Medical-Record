try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk
	import ttk

import sys
sys.path.append('./data')

from tkcalendar import DateEntry
from tkinter import font  as tkfont
from functools import partial
from tkinter import messagebox
import datetime as dt
import gradient as gr
import config as cfg
import mysql.connector

from forms.patient_consultation_form import *
from forms.geriatric_form import *
from forms.first_consultation_record import *
from forms.family_assessment_tools import *
from forms.additional_forms import *

class MedSystem(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.title_font = tkfont.Font(family='Times New Roman', size=14, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=10)

		self.patient_id = tk.StringVar(self)

		self.frames = {}
		for F in (LandingPage, PatientForm, GeriatricForm, GeriatricFormRes, FirstConsForm, FamAssessForm, ReferralForm, ReferralForm_res, review_of_systems_form, review_of_systems_form_2, physical_examination_form, assessment_table, family_apgar_form, family_apgar_form_res,followup_patient_form, followup_patient_form_2,followup_assessment_table,followup_patient_form_res):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame


			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("LandingPage")

	def get_page(self, page_class):
		return self.frames[page_class]

	def show_frame(self, page_name):
		if page_name == "LandingPage":
			LandingPage = self.get_page("LandingPage")
			LandingPage.load_patients()
			frame = self.frames[page_name]
			frame.tkraise()
		elif page_name == "FirstConsForm" or page_name == "review_of_systems_form" or page_name == "review_of_systems_form_2":
			self.get_page(page_name).load_data()
			frame = self.frames[page_name]
			frame.tkraise()
		else:
			if self.patient_id.get() == "":
				messagebox.showwarning("Warning", "No patient selected! Please select one or create a new record before proceeding")
			else:
				self.get_page(page_name).load_data()
				frame = self.frames[page_name]
				frame.tkraise()

class LandingPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.title_font = tkfont.Font(family='Courier', size=16, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=8)

		gr.GradientFrame(self, from_color="#a2b6eb", to_color="#5b80e3", height=700).pack(fill="x")

		page_title = tk.Label(self, text="FAMILY ORIENTED MEDICAL RECORD", bg = "#90a8e9", fg = "#ffffff", font=self.title_font)
		page_title.place(x=400, y=165)

		self.list_of_patients = []
		self.list_of_patients_id = []

		self.w = ttk.Combobox(self, values=self.list_of_patients, postcommand=self.changeValue)
		self.w.config(height = 4, width = 63)
		self.w.place(x=400, y=220)
		self.w.bind("<<ComboboxSelected>>", self.get_index)

		self.continue_bttn = tk.Button(self, text="Continue", command=lambda: self.continue_login(), height = 2, width = 25, bd = 0, bg = "#043c39", fg = "#ffffff", activebackground = "#cf0007")
		self.continue_bttn.place(x=510, y=350)
		tk.Button(self, text="Add a New Patient", command=lambda: self.add_new(), height = 2, width = 25, bd = 0, bg = "#043c39", fg = "#ffffff", activebackground = "#cf0007").place(x=510, y=400)

		self.load_patients()

	def continue_login(self):
		if self.controller.patient_id.get() == "":
			messagebox.showwarning("Warning", "Please select a patient")
		else:
			for F in (PatientForm, GeriatricForm, FirstConsForm, FamAssessForm, review_of_systems_form, review_of_systems_form_2, family_apgar_form, family_apgar_form_res):
				page_name = F.__name__
				p = self.controller.get_page(page_name)
				p.load_data()

			self.controller.show_frame("PatientForm")

	def add_new(self):
		self.controller.patient_id = tk.StringVar()

		for F in (PatientForm, GeriatricForm, FirstConsForm, FamAssessForm, review_of_systems_form, review_of_systems_form_2, family_apgar_form, family_apgar_form_res):
			page_name = F.__name__
			p = self.controller.get_page(page_name)
			p.load_data()

		self.controller.show_frame("FirstConsForm")

	def get_index(self, event):
		self.controller.patient_id.set(self.list_of_patients_id[self.w.current()])

	def load_patients(self):
		self.list_of_patients.clear()
		self.list_of_patients_id.clear()
		self.w.delete('0', 'end')
		self.controller.patient_id.set("")

		cur.execute("SELECT patient_id, last_name, first_name, middle_name FROM patient")
		OPTIONS = cur.fetchall()
		for x in range(len(OPTIONS)):
			self.list_of_patients.append(OPTIONS[x][1] + ", " + OPTIONS[x][2] + " " + OPTIONS[x][3])
			self.list_of_patients_id.append(OPTIONS[x][0])

		if(len(self.list_of_patients) > 0):
			self.continue_bttn.config(state="normal")
		else:
			self.list_of_patients.append("None")
			self.continue_bttn.config(state="disabled")

	def changeValue(self):
		self.w["values"] = self.list_of_patients
				
if __name__ == "__main__":

	cn = cfg.dbconnect()
	cur = cn.cursor(buffered=True)

	app = MedSystem()
	app.title("Family Oriented Medical Record")
	app.geometry("1200x710")
	app.resizable(width=False, height=False)
	app.mainloop()