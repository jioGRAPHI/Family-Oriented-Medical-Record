try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk
	import ttk

from tkcalendar import DateEntry
from tkinter import font  as tkfont
from functools import partial
from tkinter import messagebox
import datetime as dt
import mysql.connector

import database.config as cfg

def menu_frame(self, controller, num):
	menu_frame = tk.Frame(self, height = 60, width = 1200, bg = "#b1c3e6")
	menu_frame.pack(side="top")

	back_bttn = tk.Button(menu_frame, text="<", command=lambda: controller.show_frame("LandingPage"), height = 2, width = 5, bd = 0, bg = "#043c39", fg = "#ffffff")
	back_bttn.place(x=5, y=23)
	bttn1 = tk.Button(menu_frame, text="Patient Consultation Form", command=lambda: controller.show_frame("PatientForm"), height = 3, width = 30, bd = 0, bg = "#dbdbdb", wraplength = 180)
	bttn1.place(x=60, y=9)
	bttn2 = tk.Button(menu_frame, text="Geriatric Depression Scale – Short Form", command=lambda: controller.show_frame("GeriatricForm"), height = 3, width = 30, bd = 0, bg = "#dbdbdb", wraplength = 180)
	bttn2.place(x=285, y=9)
	bttn3 = tk.Button(menu_frame, text="First Consultation Record", command=lambda: controller.show_frame("FirstConsForm"), height = 3, width = 30, bd = 0, bg = "#dbdbdb", wraplength = 180)
	bttn3.place(x=510, y=9)
	bttn4 = tk.Button(menu_frame, text="Family Assessment Tools", command=lambda: controller.show_frame("FamAssessForm"), height = 3, width = 30, bd = 0, bg = "#dbdbdb", wraplength = 180)
	bttn4.place(x=735, y=9)
	bttn5 = tk.Button(menu_frame, text="Additional Form", command=lambda: controller.show_frame("followup_patient_form"), height = 3, width = 30, bd = 0, bg = "#dbdbdb", wraplength = 180)
	bttn5.place(x=960, y=9)

	if(num == 1):
		bttn1.config(height = 3, width = 30, bd = 0, wraplength = 180, bg = "SystemButtonFace")
	elif(num == 2):
		bttn2.config(height = 3, width = 30, bd = 0, wraplength = 180, bg = "SystemButtonFace")
	elif(num == 3):
		bttn3.config(height = 3, width = 30, bd = 0, wraplength = 180, bg = "SystemButtonFace")
	elif(num == 4):
		bttn4.config(height = 3, width = 30, bd = 0, wraplength = 180, bg = "SystemButtonFace")
	else:
		bttn5.config(height = 3, width = 30, bd = 0, wraplength = 180, bg = "SystemButtonFace")

class PatientForm(tk.Frame): # Patient Consultation Form

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 1)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=8)
		self.value_font = tkfont.Font(family='Helvetica', size=11)

		page_title = tk.Label(self, text="PATIENT CONSULTATION FORM", font=self.title_font)
		page_title.place(x=480, y=75)

		patient_name_label = tk.Label(self, text="FAMILY NAME, First Name: ", font=self.label_font, fg="#636363")
		patient_name_label.place(x=305, y=120)

		self.patient_name = tk.Label(self, text="", font=self.value_font)
		self.patient_name.place(x=460, y=117)

		date_label = tk.Label(self, text="Date", font=self.label_font, fg="#636363")
		date_label.place(x=50, y=200)
		self.date_input = DateEntry(self, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd")
		self.date_input.place(x=50, y=220)

		diag_label = tk.Label(self, text="Diagnosis", font=self.label_font, fg="#636363")
		diag_label.place(x=150, y=200)
		self.diag_input = tk.Text(self, height = 3, width = 24, wrap="word")
		self.diag_input.place(x=150, y=220)

		phys_label = tk.Label(self, text="Physician's Name", font=self.label_font, fg="#636363")
		phys_label.place(x=350, y=200)
		self.phys_input = tk.Text(self, height = 3, width = 24, wrap="word")
		self.phys_input.place(x=350, y=220)

		diags_label = tk.Label(self, text="Diagnostics", font=self.label_font, fg="#636363")
		diags_label.place(x=550, y=200)
		self.diags_input = tk.Text(self, height = 3, width = 24, wrap="word")
		self.diags_input.place(x=550, y=220)

		med_label = tk.Label(self, text="Medications", font=self.label_font, fg="#636363")
		med_label.place(x=750, y=200)
		self.med_input = tk.Text(self, height = 3, width = 24, wrap="word")
		self.med_input.place(x=750, y=220)

		disp_label = tk.Label(self, text="Disposition", font=self.label_font, fg="#636363")
		disp_label.place(x=950, y=200)
		self.disp_input = tk.Text(self, height = 3, width = 24, wrap="word")
		self.disp_input.place(x=950, y=220)

		self.tree = ttk.Treeview(self, height = 12)
		self.tree.column("#0", minwidth=200, width=950, stretch="no") 
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=130, y=350)

		tk.Button(self, text="ADD", command=lambda: self.add_details(self.date_input.get_date().strftime('%Y-%m-%d'), self.diag_input.get('1.0', 'end-1c'), self.phys_input.get('1.0', 'end-1c'), self.diags_input.get('1.0', 'end-1c'), self.med_input.get('1.0', 'end-1c'), self.disp_input.get('1.0', 'end-1c')), height = 2, width = 25, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=510, y=300)
	
	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT last_name, first_name, middle_name FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.patient_name['text'] = res[0] + ", " + res[1] + " " + res[2]
		else:
			self.patient_name['text'] = ""

		cur.execute(("SELECT date_form, diagnosis, physician_name, diagnostics, medications, dispositions FROM patientconsultform WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree.delete(*self.tree.get_children())

		for i in range(len(res)):
			id = self.tree.insert('', 'end', text=res[i][0])
			sub_id_1 = self.tree.insert(id, 'end', text="Diagnosis:")
			self.tree.insert(sub_id_1, 'end', text=res[i][1])
			sub_id_2 = self.tree.insert(id, 'end', text="Physician's Name")
			self.tree.insert(sub_id_2, 'end', text=res[i][2])
			sub_id_3 = self.tree.insert(id, 'end', text="Diagnostics")
			self.tree.insert(sub_id_3, 'end', text=res[i][3])
			sub_id_4 = self.tree.insert(id, 'end', text="Medications")
			self.tree.insert(sub_id_4, 'end', text=res[i][4])
			sub_id_5 = self.tree.insert(id, 'end', text="Disposition")
			self.tree.insert(sub_id_5, 'end', text=res[i][5])

	def add_details(self, date_in, diag_in, phys_in, diags_in, med_in, dis_in):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		sql = "INSERT INTO patientconsultform (date_form, diagnosis, physician_name, diagnostics, medications, dispositions, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
		val = (date_in, diag_in, phys_in, diags_in, med_in, dis_in, int(self.controller.patient_id.get()))
		cur.execute(sql, val)
		mydb.commit()

		cur.execute("SELECT LAST_INSERT_ID()")

		self.date_input.set_date(dt.datetime.today())
		self.diag_input.delete('1.0', 'end')
		self.phys_input.delete('1.0', 'end')
		self.diags_input.delete('1.0', 'end')
		self.med_input.delete('1.0', 'end')
		self.disp_input.delete('1.0', 'end')

		id = self.tree.insert('', 'end', text=date_in)
		sub_id_1 = self.tree.insert(id, 'end', text="Diagnosis:")
		self.tree.insert(sub_id_1, 'end', text=diag_in)
		sub_id_2 = self.tree.insert(id, 'end', text="Physician's Name")
		self.tree.insert(sub_id_2, 'end', text=phys_in)
		sub_id_3 = self.tree.insert(id, 'end', text="Diagnostics")
		self.tree.insert(sub_id_3, 'end', text=diags_in)
		sub_id_4 = self.tree.insert(id, 'end', text="Medications")
		self.tree.insert(sub_id_4, 'end', text=med_in)
		sub_id_5 = self.tree.insert(id, 'end', text="Disposition")
		self.tree.insert(sub_id_5, 'end', text=dis_in)
