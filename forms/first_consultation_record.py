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

def submenu_buttons_1(self, controller, num):
	side_menu_frame = tk.Frame(self, height = 720, width = 200)
	side_menu_frame.pack(side="left")

	b1 = tk.Button(side_menu_frame, text="Consultation Record", command=lambda: controller.show_frame("FirstConsForm"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b1.place(x=25, y=160)
	b2 = tk.Button(side_menu_frame, text="Physical Examination and Assessment", command=lambda: controller.show_frame("physical_examination_form"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b2.place(x=25, y=220)

	if(num == 1):
		b1.config(bg = "#2553a8")
	else:
		b2.config(bg = "#2553a8")

class FirstConsForm(tk.Frame): # Form for First consultation Record for patient's details up to present medication

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_1(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)

		page_title = tk.Label(form_frame, text="FIRST CONSULTATION RECORD", font=self.title_font)
		page_title.place(x=375, y=15)

		self.p_lname = tk.Text(form_frame, height = 1, width = 25, wrap="word")
		self.p_lname.place(x=25, y=60)
		p_lname_label = tk.Label(form_frame, text="Family Name", font=self.label_font, fg="#636363")
		p_lname_label.place(x=25, y=80)

		self.p_fname = tk.Text(form_frame, height = 1, width = 44, wrap="word")
		self.p_fname.place(x=245, y=60)
		p_fname_label = tk.Label(form_frame, text="First Name", font=self.label_font, fg="#636363")
		p_fname_label.place(x=245, y=80)

		self.p_mname = tk.Text(form_frame, height = 1, width = 25, wrap="word")
		self.p_mname.place(x=625, y=60)
		p_mname_label = tk.Label(form_frame, text="Middle Name", font=self.label_font, fg="#636363")
		p_mname_label.place(x=625, y=80)

		self.p_addr = tk.Text(form_frame, height = 1, width = 113, wrap="word")
		self.p_addr.place(x=25, y=110)
		p_addr_label = tk.Label(form_frame, text="Address", font=self.label_font, fg="#636363")
		p_addr_label.place(x=25, y=130)

		self.p_bday = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd")
		self.p_bday.place(x=25, y=160)
		p_bday_label = tk.Label(form_frame, text="Birthdate (YYYY-MM-DD)", font=self.label_font, fg="#636363")
		p_bday_label.place(x=25, y=185)

		self.p_age = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.p_age.place(x=175, y=160)
		p_age_label = tk.Label(form_frame, text="Age", font=self.label_font, fg="#636363")
		p_age_label.place(x=175, y=185)

		self.p_gender = tk.Text(form_frame, height = 1, width = 15, wrap="word")
		self.p_gender.place(x=285, y=160)
		p_gender_label = tk.Label(form_frame, text="Gender", font=self.label_font, fg="#636363")
		p_gender_label.place(x=285, y=185)

		self.p_civil_stat = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.p_civil_stat.place(x=425, y=160)
		p_civil_stat_label = tk.Label(form_frame, text="Civil Status", font=self.label_font, fg="#636363")
		p_civil_stat_label.place(x=425, y=185)

		self.p_contact = tk.Text(form_frame, height = 1, width = 30, wrap="word")
		self.p_contact.place(x=625, y=160)
		p_contact_label = tk.Label(form_frame, text="Contact No(s).", font=self.label_font, fg="#636363")
		p_contact_label.place(x=625, y=185)
		
		self.p_occup = tk.Text(form_frame, height = 1, width = 85, wrap="word")
		self.p_occup.place(x=25, y=215)
		p_occup_label = tk.Label(form_frame, text="Occupation", font=self.label_font, fg="#636363")
		p_occup_label.place(x=25, y=240)

		self.p_datecons = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd")
		self.p_datecons.place(x=725, y=215)
		p_datecons_label = tk.Label(form_frame, text="Date of Consult", font=self.label_font, fg="#636363")
		p_datecons_label.place(x=725, y=240)

		self.p_compliant = tk.Text(form_frame, height = 5, width = 113, wrap="word")
		self.p_compliant.place(x=25, y=270)
		p_compliant_label = tk.Label(form_frame, text="Chief Complaint", font=self.label_font, fg="#636363")
		p_compliant_label.place(x=25, y=360)

		self.p_hist_illness = tk.Text(form_frame, height = 5, width = 113, wrap="word")
		self.p_hist_illness.place(x=25, y=390)
		p_hist_illness_label = tk.Label(form_frame, text="History of Present Illness", font=self.label_font, fg="#636363")
		p_hist_illness_label.place(x=25, y=485)

		self.p_context = tk.Text(form_frame, height = 1, width = 113, wrap="word")
		self.p_context.place(x=25, y=515)
		p_context_label = tk.Label(form_frame, text="Context", font=self.label_font, fg="#636363")
		p_context_label.place(x=25, y=545)

		self.p_pres_med = tk.Text(form_frame, height = 1, width = 113, wrap="word")
		self.p_pres_med.place(x=25, y=565)
		p_pres_med_label = tk.Label(form_frame, text="Present Medication", font=self.label_font, fg="#636363")
		p_pres_med_label.place(x=25, y=595)

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("review_of_systems_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

		self.edit_button = tk.Button(form_frame, text="edit", command=lambda: self.edit_details(), height = 1, width = 3, bd = 0, fg = "#0060ba")
		self.edit_button.place(x=590, y=15)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.p_lname.delete('1.0', 'end')
		self.p_fname.delete('1.0', 'end')
		self.p_mname.delete('1.0', 'end')
		self.p_addr.delete('1.0', 'end')
		self.p_age.delete('1.0', 'end')
		self.p_gender.delete('1.0', 'end')
		self.p_civil_stat.delete('1.0', 'end')
		self.p_contact.delete('1.0', 'end')
		self.p_occup.delete('1.0', 'end')
		
		cur.execute(("SELECT last_name, first_name, middle_name, address, birthdate, age, gender, civil_status, contact_no, occupation FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		
		if res is not None:
			if res[0] is not None:
				self.p_lname.insert('1.0', res[0])
			if res[1] is not None:
				self.p_fname.insert('1.0', res[1])
			if res[2] is not None:
				self.p_mname.insert('1.0', res[2])
			if res[3] is not None:
				self.p_addr.insert('1.0', res[3])
			if res[4] is not None:
				self.p_bday.set_date(res[4])
			if res[5] is not None:
				self.p_age.insert('1.0', res[5])
			if res[6] is not None:
				self.p_gender.insert('1.0', res[6])
			if res[7] is not None:
				self.p_civil_stat.insert('1.0', res[7])
			if res[8] is not None:
				self.p_contact.insert('1.0', res[8])
			if res[9] is not None:
				self.p_occup.insert('1.0', res[9])
			
			self.p_lname.config(state = "disabled", bg = "#e8e8e8")
			self.p_fname.config(state = "disabled", bg = "#e8e8e8")
			self.p_mname.config(state = "disabled", bg = "#e8e8e8")
			self.p_addr.config(state = "disabled", bg = "#e8e8e8")
			self.p_age.config(state = "disabled", bg = "#e8e8e8")
			self.p_gender.config(state = "disabled", bg = "#e8e8e8")
			self.p_civil_stat.config(state = "disabled", bg = "#e8e8e8")
			self.p_contact.config(state = "disabled", bg = "#e8e8e8")
			self.p_occup.config(state = "disabled", bg = "#e8e8e8")
			self.p_bday.config(state = "disabled")

		else:
			self.p_lname.delete('1.0', 'end')
			self.p_fname.delete('1.0', 'end')
			self.p_mname.delete('1.0', 'end')
			self.p_addr.delete('1.0', 'end')
			self.p_age.delete('1.0', 'end')
			self.p_gender.delete('1.0', 'end')
			self.p_civil_stat.delete('1.0', 'end')
			self.p_contact.delete('1.0', 'end')
			self.p_occup.delete('1.0', 'end')
			self.p_lname.config(state = "normal", bg = "#ffffff")
			self.p_fname.config(state = "normal", bg = "#ffffff")
			self.p_mname.config(state = "normal", bg = "#ffffff")
			self.p_addr.config(state = "normal", bg = "#ffffff")
			self.p_age.config(state = "normal", bg = "#ffffff")
			self.p_gender.config(state = "normal", bg = "#ffffff")
			self.p_civil_stat.config(state = "normal", bg = "#ffffff")
			self.p_contact.config(state = "normal", bg = "#ffffff")
			self.p_occup.config(state = "normal", bg = "#ffffff")
			self.p_bday.config(state = "normal")

		cur.execute(("SELECT date_of_consult, complaint, history_of_illness, context, present_medication FROM patientconsultation WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		
		if res is not None:
			if res[0] is not None:
				self.p_datecons.set_date(res[0])
			if res[1] is not None:
				self.p_compliant.insert('1.0', res[1])
			if res[2] is not None:
				self.p_hist_illness.insert('1.0', res[2])
			if res[3] is not None:
				self.p_context.insert('1.0', res[3])
			if res[4] is not None:
				self.p_pres_med.insert('1.0', res[4])

			self.p_datecons.config(state = "disabled")
			self.p_compliant.config(state = "disabled", bg = "#e8e8e8")
			self.p_hist_illness.config(state = "disabled", bg = "#e8e8e8")
			self.p_context.config(state = "disabled", bg = "#e8e8e8")
			self.p_pres_med.config(state = "disabled", bg = "#e8e8e8")

		else:
			self.p_datecons.set_date(dt.datetime.today())
			self.p_compliant.delete('1.0', 'end')
			self.p_hist_illness.delete('1.0', 'end')
			self.p_context.delete('1.0', 'end')
			self.p_pres_med.delete('1.0', 'end')

			self.p_datecons.config(state = "normal")
			self.p_compliant.config(state = "normal", bg = "#ffffff")
			self.p_hist_illness.config(state = "normal", bg = "#ffffff")
			self.p_context.config(state = "normal", bg = "#ffffff")
			self.p_pres_med.config(state = "normal", bg = "#ffffff")

	def edit_details(self):
		self.p_lname.config(state = "normal", bg = "#ffffff")
		self.p_fname.config(state = "normal", bg = "#ffffff")
		self.p_mname.config(state = "normal", bg = "#ffffff")
		self.p_addr.config(state = "normal", bg = "#ffffff")
		self.p_age.config(state = "normal", bg = "#ffffff")
		self.p_gender.config(state = "normal", bg = "#ffffff")
		self.p_civil_stat.config(state = "normal", bg = "#ffffff")
		self.p_contact.config(state = "normal", bg = "#ffffff")
		self.p_occup.config(state = "normal", bg = "#ffffff")
		self.p_bday.config(state = "normal")

class review_of_systems_form(tk.Frame): # Form containing the Review of Systems before "Past/Medical History"

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_1(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")

		y_value = 60

		self.heent_var = []
		self.respi_var = []
		self.cardio_var = []
		self.gastro_var = []
		self.genito_var = []
		self.meta_var = []
		self.neuro_var = []
		self.musculo_var = []
		self.skin_var = []

		self.heent_cb = []
		self.respi_cb = []
		self.cardio_cb = []
		self.gastro_cb = []
		self.genito_cb = []
		self.meta_cb = []
		self.neuro_cb = []
		self.musculo_cb = []
		self.skin_cb = []

		label = tk.Label(form_frame, text="Review of Systems:", font=self.label_font_2)
		label.place(x=25, y=15)

		with open("./data/heent.txt", 'r') as f:
			self.heent_opt = f.read().splitlines()
		f.close()

		heent_label = tk.Label(form_frame, text="HEENT", font=self.label_font, fg="#636363")
		heent_label.place(x=25, y=35)

		for i in range(len(self.heent_opt)):
			self.heent_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.heent_opt[i], variable=self.heent_var[i])
			cb.place(x=25, y=y_value)
			self.heent_cb.append(cb)
			y_value = y_value + 20

		self.heent_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.heent_var[len(self.heent_opt)])
		cb.place(x=25, y=y_value)
		self.heent_cb.append(cb)
		y_value = y_value + 20

		self.other_heent = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_heent.place(x=50, y=y_value)
		y_value = y_value + 30


		with open("./data/respiratory.txt", 'r') as f:
			self.respi_opt = f.read().splitlines()
		f.close()

		respi_label = tk.Label(form_frame, text="Respiratory", font=self.label_font, fg="#636363")
		respi_label.place(x=25, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.respi_opt)):
			self.respi_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.respi_opt[i], variable=self.respi_var[i])
			cb.place(x=25, y=y_value)
			self.respi_cb.append(cb)
			y_value = y_value + 20

		self.respi_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.respi_var[len(self.respi_opt)])
		cb.place(x=25, y=y_value)
		self.respi_cb.append(cb)
		y_value = y_value + 20

		self.other_respi = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_respi.place(x=50, y=y_value)
		y_value = y_value + 30


		with open("./data/cardiovascular.txt", 'r') as f:
			self.cardio_opt = f.read().splitlines()
		f.close()

		cardio_label = tk.Label(form_frame, text="Cardiovascular", font=self.label_font, fg="#636363")
		cardio_label.place(x=25, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.cardio_opt)):
			self.cardio_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.cardio_opt[i], variable=self.cardio_var[i])
			cb.place(x=25, y=y_value)
			self.cardio_cb.append(cb)
			y_value = y_value + 20

		self.cardio_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.cardio_var[len(self.cardio_opt)])
		cb.place(x=25, y=y_value)
		self.cardio_cb.append(cb)
		y_value = y_value + 20

		self.other_cardio = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_cardio.place(x=50, y=y_value)


		y_value = 15

		with open("./data/gastro.txt", 'r') as f:
			self.gastro_opt = f.read().splitlines()
		f.close()

		gastro_label = tk.Label(form_frame, text="Gastrointestinal", font=self.label_font, fg="#636363")
		gastro_label.place(x=300, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.gastro_opt)):
			self.gastro_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.gastro_opt[i], variable=self.gastro_var[i])
			cb.place(x=300, y=y_value)
			self.gastro_cb.append(cb)
			y_value = y_value + 20

		self.gastro_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.gastro_var[len(self.gastro_opt)])
		cb.place(x=300, y=y_value)
		self.gastro_cb.append(cb)
		y_value = y_value + 20

		self.other_gastro = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_gastro.place(x=325, y=y_value)
		y_value = y_value + 30


		with open("./data/genito.txt", 'r') as f:
			self.genito_opt = f.read().splitlines()
		f.close()

		genito_label = tk.Label(form_frame, text="Genitourinary", font=self.label_font, fg="#636363")
		genito_label.place(x=300, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.genito_opt)):
			self.genito_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.genito_opt[i], variable=self.genito_var[i])
			cb.place(x=300, y=y_value)
			self.genito_cb.append(cb)
			y_value = y_value + 20

		self.genito_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.genito_var[len(self.genito_opt)])
		cb.place(x=300, y=y_value)
		self.genito_cb.append(cb)
		y_value = y_value + 20

		self.other_genito = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_genito.place(x=325, y=y_value)
		y_value = y_value + 30


		with open("./data/metabolic.txt", 'r') as f:
			self.meta_opt = f.read().splitlines()
		f.close()

		meta_label = tk.Label(form_frame, text="Metabolic/Endocrine", font=self.label_font, fg="#636363")
		meta_label.place(x=300, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.meta_opt)):
			self.meta_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.meta_opt[i], variable=self.meta_var[i])
			cb.place(x=300, y=y_value)
			self.meta_cb.append(cb)
			y_value = y_value + 20

		self.meta_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.meta_var[len(self.meta_opt)])
		cb.place(x=300, y=y_value)
		self.meta_cb.append(cb)
		y_value = y_value + 20

		self.other_meta = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_meta.place(x=325, y=y_value)


		y_value = 15

		with open("./data/neuro.txt", 'r') as f:
			self.neuro_opt = f.read().splitlines()
		f.close()

		neuro_label = tk.Label(form_frame, text="Neurologic", font=self.label_font, fg="#636363")
		neuro_label.place(x=575, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.neuro_opt)):
			self.neuro_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.neuro_opt[i], variable=self.neuro_var[i])
			cb.place(x=575, y=y_value)
			self.neuro_cb.append(cb)
			y_value = y_value + 20

		self.neuro_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.neuro_var[len(self.neuro_opt)])
		cb.place(x=575, y=y_value)
		self.neuro_cb.append(cb)
		y_value = y_value + 20

		self.other_neuro = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_neuro.place(x=600, y=y_value)
		y_value = y_value + 30


		with open("./data/musculoskeletal.txt", 'r') as f:
			self.musculo_opt = f.read().splitlines()
		f.close()

		musculo_label = tk.Label(form_frame, text="Musculoskeletal", font=self.label_font, fg="#636363")
		musculo_label.place(x=575, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.musculo_opt)):
			self.musculo_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.musculo_opt[i], variable=self.musculo_var[i])
			cb.place(x=575, y=y_value)
			self.musculo_cb.append(cb)
			y_value = y_value + 20

		self.musculo_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.musculo_var[len(self.musculo_opt)])
		cb.place(x=575, y=y_value)
		self.musculo_cb.append(cb)
		y_value = y_value + 20

		self.other_musculo = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_musculo.place(x=600, y=y_value)
		y_value = y_value + 30


		with open("./data/skin.txt", 'r') as f:
			self.skin_opt = f.read().splitlines()
		f.close()

		skin_label = tk.Label(form_frame, text="Skin Integument", font=self.label_font, fg="#636363")
		skin_label.place(x=575, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.skin_opt)):
			self.skin_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.skin_opt[i], variable=self.skin_var[i])
			cb.place(x=575, y=y_value)
			self.skin_cb.append(cb)
			y_value = y_value + 20

		self.skin_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.skin_var[len(self.skin_opt)])
		cb.place(x=575, y=y_value)
		self.skin_cb.append(cb)
		y_value = y_value + 20

		self.other_skin = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_skin.place(x=600, y=y_value)

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("review_of_systems_form_2"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=65)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("FirstConsForm"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def add_details(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT heent_1, heent_2, heent_3, heent_4, heent_5, heent_6, heent_7, heent_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (heent_1, heent_2, heent_3, heent_4, heent_5, heent_6, heent_7, heent_8, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.heent_var[0].get(), self.heent_var[1].get(), self.heent_var[2].get(), self.heent_var[3].get(), self.heent_var[4].get(), 
				self.heent_var[5].get(), self.heent_var[6].get(),self.heent_var[7].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET heent_1 = %s, heent_2 = %s, heent_3 = %s, heent_4 = %s, heent_5 = %s, heent_6 = %s, heent_7 = %s, heent_8 = %s WHERE patient_id = %s"
			val = (self.heent_var[0].get(), self.heent_var[1].get(), self.heent_var[2].get(), self.heent_var[3].get(), self.heent_var[4].get(), 
				self.heent_var[5].get(), self.heent_var[6].get(),self.heent_var[7].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.heent_var[len(self.heent_opt)].get() == 1:
			cur.execute(("SELECT heent_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (heent_others, patient_id) VALUES (%s, %s)"), (self.other_heent.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET heent_others = %s WHERE patient_id = %s"), (self.other_heent.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT heent_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (heent_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET heent_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT respi_1, respi_2, respi_3, respi_4, respi_5 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (respi_1, respi_2, respi_3, respi_4, respi_5 patient_id) VALUES (%s, %s, %s, %s, %s, %s)"
			val = (self.respi_var[0].get(), self.respi_var[1].get(), self.respi_var[2].get(), self.respi_var[3].get(), self.respi_var[4].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET respi_1 = %s, respi_2 = %s, respi_3 = %s, respi_4 = %s, respi_5 = %s WHERE patient_id = %s"
			val = (self.respi_var[0].get(), self.respi_var[1].get(), self.respi_var[2].get(), self.respi_var[3].get(), self.respi_var[4].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.respi_var[len(self.respi_opt)].get() == 1:
			cur.execute(("SELECT respi_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (respi_others, patient_id) VALUES (%s, %s)"), (self.other_respi.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET respi_others = %s WHERE patient_id = %s"), (self.other_respi.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT respi_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (respi_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET respi_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()


		####################################

		cur.execute(("SELECT cardio_1, cardio_2, cardio_3, cardio_4, cardio_5, cardio_6, cardio_7 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (cardio_1, cardio_2, cardio_3, cardio_4, cardio_5, cardio_6, cardio_7, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.cardio_var[0].get(), self.cardio_var[1].get(), self.cardio_var[2].get(), self.cardio_var[3].get(), self.cardio_var[4].get(), 
				self.cardio_var[5].get(), self.cardio_var[6].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET cardio_1 = %s, cardio_2 = %s, cardio_3 = %s, cardio_4 = %s, cardio_5 = %s, cardio_6 = %s, cardio_7 = %s WHERE patient_id = %s"
			val = (self.cardio_var[0].get(), self.cardio_var[1].get(), self.cardio_var[2].get(), self.cardio_var[3].get(), self.cardio_var[4].get(), 
				self.cardio_var[5].get(), self.cardio_var[6].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.cardio_var[len(self.cardio_opt)].get() == 1:
			cur.execute(("SELECT cardio_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (cardio_others, patient_id) VALUES (%s, %s)"), (self.other_cardio.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET cardio_others = %s WHERE patient_id = %s"), (self.other_cardio.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT cardio_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (cardio_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET cardio_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT gastro_1, gastro_2, gastro_3, gastro_4, gastro_5, gastro_6, gastro_7, gastro_8, gastro_9 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (gastro_1, gastro_2, gastro_3, gastro_4, gastro_5, gastro_6, gastro_7, gastro_8, gastro_9, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.gastro_var[0].get(), self.gastro_var[1].get(), self.gastro_var[2].get(), self.gastro_var[3].get(), self.gastro_var[4].get(), 
				self.gastro_var[5].get(), self.gastro_var[6].get(),self.gastro_var[7].get(),self.gastro_var[8].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET gastro_1 = %s, gastro_2 = %s, gastro_3 = %s, gastro_4 = %s, gastro_5 = %s, gastro_6 = %s, gastro_7 = %s, gastro_8 = %s, gastro_9 = %s WHERE patient_id = %s"
			val = (self.gastro_var[0].get(), self.gastro_var[1].get(), self.gastro_var[2].get(), self.gastro_var[3].get(), self.gastro_var[4].get(), 
				self.gastro_var[5].get(), self.gastro_var[6].get(),self.gastro_var[7].get(),self.gastro_var[8].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.gastro_var[len(self.gastro_opt)].get() == 1:
			cur.execute(("SELECT gastro_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (gastro_others, patient_id) VALUES (%s, %s)"), (self.other_gastro.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET gastro_others = %s WHERE patient_id = %s"), (self.other_gastro.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT gastro_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (gastro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET gastro_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT genito_1, genito_2, genito_3, genito_4, genito_5, genito_6, genito_7, genito_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (genito_1, genito_2, genito_3, genito_4, genito_5, genito_6, genito_7, genito_8, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.genito_var[0].get(), self.genito_var[1].get(), self.genito_var[2].get(), self.genito_var[3].get(), self.genito_var[4].get(), 
				self.genito_var[5].get(), self.genito_var[6].get(),self.genito_var[7].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET genito_1 = %s, genito_2 = %s, genito_3 = %s, genito_4 = %s, genito_5 = %s, genito_6 = %s, genito_7 = %s, genito_8 = %s WHERE patient_id = %s"
			val = (self.genito_var[0].get(), self.genito_var[1].get(), self.genito_var[2].get(), self.genito_var[3].get(), self.genito_var[4].get(), 
				self.genito_var[5].get(), self.genito_var[6].get(),self.genito_var[7].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.genito_var[len(self.genito_opt)].get() == 1:
			cur.execute(("SELECT genito_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (genito_others, patient_id) VALUES (%s, %s)"), (self.other_genito.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET genito_others = %s WHERE patient_id = %s"), (self.other_genito.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT genito_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (genito_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET genito_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT meta_1, meta_2, meta_3, meta_4, meta_5, meta_6 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (meta_1, meta_2, meta_3, meta_4, meta_5, meta_6, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			val = (self.meta_var[0].get(), self.meta_var[1].get(), self.meta_var[2].get(), self.meta_var[3].get(), self.meta_var[4].get(), 
				self.meta_var[5].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET meta_1 = %s, meta_2 = %s, meta_3 = %s, meta_4 = %s, meta_5 = %s, meta_6 = %s WHERE patient_id = %s"
			val = (self.meta_var[0].get(), self.meta_var[1].get(), self.meta_var[2].get(), self.meta_var[3].get(), self.meta_var[4].get(), 
				self.meta_var[5].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.meta_var[len(self.meta_opt)].get() == 1:
			cur.execute(("SELECT meta_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (meta_others, patient_id) VALUES (%s, %s)"), (self.other_meta.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET meta_others = %s WHERE patient_id = %s"), (self.other_meta.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT meta_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (meta_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET meta_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT neuro_1, neuro_2, neuro_3, neuro_4, neuro_5, neuro_6, neuro_7, neuro_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (neuro_1, neuro_2, neuro_3, neuro_4, neuro_5, neuro_6, neuro_7, neuro_8, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.neuro_var[0].get(), self.neuro_var[1].get(), self.neuro_var[2].get(), self.neuro_var[3].get(), self.neuro_var[4].get(), 
				self.neuro_var[5].get(), self.neuro_var[6].get(),self.neuro_var[7].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET neuro_1 = %s, neuro_2 = %s, neuro_3 = %s, neuro_4 = %s, neuro_5 = %s, neuro_6 = %s, neuro_7 = %s, neuro_8 = %s WHERE patient_id = %s"
			val = (self.neuro_var[0].get(), self.neuro_var[1].get(), self.neuro_var[2].get(), self.neuro_var[3].get(), self.neuro_var[4].get(), 
				self.neuro_var[5].get(), self.neuro_var[6].get(),self.neuro_var[7].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.neuro_var[len(self.neuro_opt)].get() == 1:
			cur.execute(("SELECT neuro_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (neuro_others, patient_id) VALUES (%s, %s)"), (self.other_neuro.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET neuro_others = %s WHERE patient_id = %s"), (self.other_neuro.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT neuro_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (neuro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET neuro_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT musculo_1, musculo_2, musculo_3, musculo_4, musculo_5 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (musculo_1, musculo_2, musculo_3, musculo_4, musculo_5, patient_id) VALUES (%s, %s, %s, %s, %s, %s)"
			val = (self.musculo_var[0].get(), self.musculo_var[1].get(), self.musculo_var[2].get(), self.musculo_var[3].get(), self.musculo_var[4].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET musculo_1 = %s, musculo_2 = %s, musculo_3 = %s, musculo_4 = %s, musculo_5 = %s WHERE patient_id = %s"
			val = (self.musculo_var[0].get(), self.musculo_var[1].get(), self.musculo_var[2].get(), self.musculo_var[3].get(), self.musculo_var[4].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.musculo_var[len(self.musculo_opt)].get() == 1:
			cur.execute(("SELECT musculo_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (musculo_others, patient_id) VALUES (%s, %s)"), (self.other_musculo.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET musculo_others = %s WHERE patient_id = %s"), (self.other_musculo.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT musculo_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (musculo_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET musculo_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		cur.execute(("SELECT skin_1, skin_2, skin_3, skin_4, skin_5, skin_6, skin_7 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientrevofsys (skin_1, skin_2, skin_3, skin_4, skin_5, skin_6, skin_7, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.skin_var[0].get(), self.skin_var[1].get(), self.skin_var[2].get(), self.skin_var[3].get(), self.skin_var[4].get(), 
				self.skin_var[5].get(), self.skin_var[6].get(),self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientrevofsys SET skin_1 = %s, skin_2 = %s, skin_3 = %s, skin_4 = %s, skin_5 = %s, skin_6 = %s, skin_7 = %s WHERE patient_id = %s"
			val = (self.skin_var[0].get(), self.skin_var[1].get(), self.skin_var[2].get(), self.skin_var[3].get(), self.skin_var[4].get(), 
				self.skin_var[5].get(), self.skin_var[6].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.skin_var[len(self.skin_opt)].get() == 1:
			cur.execute(("SELECT skin_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (skin_others, patient_id) VALUES (%s, %s)"), (self.other_skin.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET skin_others = %s WHERE patient_id = %s"), (self.other_skin.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT skin_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientrevofsys (skin_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientrevofsys SET skin_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		####################################

		for i in range(len(self.heent_var)):
			if i >= len(self.heent_opt):
				if self.heent_var[i].get() == 1:
					self.other_heent.delete('1.0', 'end') 
			self.heent_var[i] = tk.IntVar(self)

		for i in range(len(self.respi_var)):
			if i >= len(self.respi_opt):
				if self.respi_var[i].get() == 1:
					self.other_respi.delete('1.0', 'end') 
			self.respi_var[i] = tk.IntVar(self)

		for i in range(len(self.cardio_var)):
			if i >= len(self.cardio_opt):
				if self.cardio_var[i].get() == 1:
					self.other_cardio.delete('1.0', 'end') 
			self.cardio_var[i] = tk.IntVar(self)

		for i in range(len(self.gastro_var)):
			if i >= len(self.gastro_opt):
				if self.gastro_var[i].get() == 1:
					self.other_gastro.delete('1.0', 'end') 
			self.gastro_var[i] = tk.IntVar(self)

		for i in range(len(self.genito_var)):
			if i >= len(self.genito_opt):
				if self.genito_var[i].get() == 1:
					self.other_genito.delete('1.0', 'end') 
			self.genito_var[i] = tk.IntVar(self)

		for i in range(len(self.meta_var)):
			if i >= len(self.meta_opt):
				if self.meta_var[i].get() == 1:
					self.other_meta.delete('1.0', 'end') 
			self.meta_var[i] = tk.IntVar(self)

		for i in range(len(self.neuro_var)):
			if i >= len(self.neuro_opt):
				if self.neuro_var[i].get() == 1:
					self.other_neuro.delete('1.0', 'end') 
			self.neuro_var[i] = tk.IntVar(self)

		for i in range(len(self.musculo_var)):
			if i >= len(self.musculo_opt):
				if self.musculo_var[i].get() == 1:
					self.other_musculo.delete('1.0', 'end') 
			self.musculo_var[i] = tk.IntVar(self)

		for i in range(len(self.skin_var)):
			if i >= len(self.skin_opt):
				if self.skin_var[i].get() == 1:
					self.other_skin.delete('1.0', 'end') 
			self.skin_var[i] = tk.IntVar(self)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)

		cur.execute(("SELECT heent_1, heent_2, heent_3, heent_4, heent_5, heent_6, heent_7, heent_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.heent_var)):
				if res[i] is not None:
					self.heent_var[i].set(res[i])
					self.heent_cb[i].config(state = "disabled")
		else:
			for i in range(8):
				self.heent_var[i].set(0)
				self.heent_cb[i].config(state = "normal")

		cur.execute(("SELECT respi_1, respi_2, respi_3, respi_4, respi_5 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.respi_var)):
				if res[i] is not None:
					self.respi_var[i].set(res[i])
					self.respi_cb[i].config(state = "disabled")
		else:
			for i in range(5):
				self.respi_var[i].set(0)
				self.respi_cb[i].config(state = "normal")

		cur.execute(("SELECT cardio_1, cardio_2, cardio_3, cardio_4, cardio_5, cardio_6, cardio_7 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.cardio_var)):
				if res[i] is not None:
					self.cardio_var[i].set(res[i])
					self.cardio_cb[i].config(state = "disabled")
		else:
			for i in range(7):
				self.cardio_var[i].set(0)
				self.cardio_cb[i].config(state = "normal")

		cur.execute(("SELECT gastro_1, gastro_2, gastro_3, gastro_4, gastro_5, gastro_6, gastro_7, gastro_8, gastro_9 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.gastro_var)):
				if res[i] is not None:
					self.gastro_var[i].set(res[i])
					self.gastro_cb[i].config(state = "disabled")
		else:
			for i in range(9):
				self.gastro_var[i].set(0)
				self.gastro_cb[i].config(state = "normal")

		cur.execute(("SELECT genito_1, genito_2, genito_3, genito_4, genito_5, genito_6, genito_7, genito_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.genito_var)):
				if res[i] is not None:
					self.genito_var[i].set(res[i])
					self.genito_cb[i].config(state = "disabled")
		else:
			for i in range(8):
				self.genito_var[i].set(0)
				self.genito_cb[i].config(state = "normal")

		cur.execute(("SELECT meta_1, meta_2, meta_3, meta_4, meta_5, meta_6 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.meta_var)):
				if res[i] is not None:
					self.meta_var[i].set(res[i])
					self.meta_cb[i].config(state = "disabled")
		else:
			for i in range(6):
				self.meta_var[i].set(0)
				self.meta_cb[i].config(state = "normal")

		cur.execute(("SELECT neuro_1, neuro_2, neuro_3, neuro_4, neuro_5, neuro_6, neuro_7, neuro_8 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.neuro_var)):
				if res[i] is not None:
					self.neuro_var[i].set(res[i])
					self.neuro_cb[i].config(state = "disabled")
		else:
			for i in range(8):
				self.neuro_var[i].set(0)
				self.neuro_cb[i].config(state = "normal")

		cur.execute(("SELECT musculo_1, musculo_2, musculo_3, musculo_4, musculo_5 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.musculo_var)):
				if res[i] is not None:
					self.musculo_var[i].set(res[i])
					self.musculo_cb[i].config(state = "disabled")
		else:
			for i in range(5):
				self.musculo_var[i].set(0)
				self.musculo_cb[i].config(state = "normal")

		cur.execute(("SELECT skin_1, skin_2, skin_3, skin_4, skin_5, skin_6, skin_7 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.skin_var)):
				if res[i] is not None:
					self.skin_var[i].set(res[i])
					self.skin_cb[i].config(state = "disabled")
		else:
			for i in range(7):
				self.skin_var[i].set(0)
				self.skin_cb[i].config(state = "normal")

		self.other_heent.delete('1.0', 'end')
		self.other_respi.delete('1.0', 'end')
		self.other_cardio.delete('1.0', 'end')
		self.other_gastro.delete('1.0', 'end')
		self.other_genito.delete('1.0', 'end')
		self.other_meta.delete('1.0', 'end')
		self.other_neuro.delete('1.0', 'end')
		self.other_musculo.delete('1.0', 'end')
		self.other_skin.delete('1.0', 'end')

		cur.execute(("SELECT heent_others, respi_others, cardio_others, gastro_others, genito_others, meta_others, neuro_others, musculo_others, skin_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				self.other_heent.insert('1.0', res[0])
			if res[1] is not None:
				self.other_respi.insert('1.0', res[1])
			if res[2] is not None:
				self.other_cardio.insert('1.0', res[2])
			if res[3] is not None:
				self.other_gastro.insert('1.0', res[3])
			if res[4] is not None:
				self.other_genito.insert('1.0', res[4])
			if res[5] is not None:
				self.other_meta.insert('1.0', res[5])
			if res[6] is not None:
				self.other_neuro.insert('1.0', res[6])
			if res[7] is not None:
				self.other_musculo.insert('1.0', res[7])
			if res[8] is not None:
				self.other_skin.insert('1.0', res[8])
			

			self.other_heent.config(state = "disabled", bg = "#e8e8e8")
			self.other_respi.config(state = "disabled", bg = "#e8e8e8")
			self.other_cardio.config(state = "disabled", bg = "#e8e8e8")
			self.other_gastro.config(state = "disabled", bg = "#e8e8e8")
			self.other_genito.config(state = "disabled", bg = "#e8e8e8")
			self.other_meta.config(state = "disabled", bg = "#e8e8e8")
			self.other_neuro.config(state = "disabled", bg = "#e8e8e8")
			self.other_musculo.config(state = "disabled", bg = "#e8e8e8")
			self.other_skin.config(state = "disabled", bg = "#e8e8e8")
		else:
			self.other_heent.delete('1.0', 'end')
			self.other_respi.delete('1.0', 'end')
			self.other_cardio.delete('1.0', 'end')
			self.other_gastro.delete('1.0', 'end')
			self.other_genito.delete('1.0', 'end')
			self.other_meta.delete('1.0', 'end')
			self.other_neuro.delete('1.0', 'end')
			self.other_musculo.delete('1.0', 'end')
			self.other_skin.delete('1.0', 'end')
			self.other_heent.config(state = "normal", bg = "#ffffff")
			self.other_respi.config(state = "normal", bg = "#ffffff")
			self.other_cardio.config(state = "normal", bg = "#ffffff")
			self.other_gastro.config(state = "normal", bg = "#ffffff")
			self.other_genito.config(state = "normal", bg = "#ffffff")
			self.other_meta.config(state = "normal", bg = "#ffffff")
			self.other_neuro.config(state = "normal", bg = "#ffffff")
			self.other_musculo.config(state = "normal", bg = "#ffffff")
			self.other_skin.config(state = "normal", bg = "#ffffff")

class review_of_systems_form_2(tk.Frame): # Form containing the Past/Medical History before Physical Examination

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_1(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")

		y_value = 25

		medhist_label = tk.Label(form_frame, text="Family History: relationship", font=self.label_font_2, fg="#636363")
		medhist_label.place(x=25, y=y_value)
		y_value = y_value + 15

		illness_label = tk.Label(form_frame, text="Illness:", font=self.label_font, fg="#636363")
		illness_label.place(x=25, y=y_value)
		y_value = y_value + 25

		self.medhist_illness = tk.Text(form_frame, height = 4, width = 23, wrap="word")
		self.medhist_illness.place(x=25, y=y_value)
		y_value = y_value + 80

		hospt_label = tk.Label(form_frame, text="Hospitalization, pls list/dates:", font=self.label_font, fg="#636363")
		hospt_label.place(x=25, y=y_value)
		y_value = y_value + 25

		self.medhist_hospt = tk.Text(form_frame, height = 4, width = 23, wrap="word")
		self.medhist_hospt.place(x=25, y=y_value)
		y_value = y_value + 80

		allergy_label = tk.Label(form_frame, text="Allergies, please list:", font=self.label_font, fg="#636363")
		allergy_label.place(x=25, y=y_value)
		y_value = y_value + 25

		self.medhist_allergy = tk.Text(form_frame, height = 4, width = 23, wrap="word")
		self.medhist_allergy.place(x=25, y=y_value)
		y_value = y_value + 80

		self.famhist_var = []
		self.immunohist_var = []

		self.famhist_cb = []
		self.immunohist_cb = []

		with open("./data/famhistory.txt", 'r') as f:
			self.famhist_opt = f.read().splitlines()
		f.close()

		famhist_label = tk.Label(form_frame, text="Family History: relationship", font=self.label_font_2, fg="#636363")
		famhist_label.place(x=25, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.famhist_opt)):
			self.famhist_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.famhist_opt[i], variable=self.famhist_var[i])
			cb.place(x=25, y=y_value)
			self.famhist_cb.append(cb)
			y_value = y_value + 20

		self.famhist_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.famhist_var[len(self.famhist_opt)])
		cb.place(x=25, y=y_value)
		self.famhist_cb.append(cb)
		y_value = y_value + 20

		self.other_famhist = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_famhist.place(x=50, y=y_value)
		y_value = y_value + 30

		with open("./data/immunohist.txt", 'r') as f:
			self.immunohist_opt = f.read().splitlines()
		f.close()

		y_value = 25

		immunohist_label = tk.Label(form_frame, text="Immunization History:", font=self.label_font_2, fg="#636363")
		immunohist_label.place(x=250, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.immunohist_opt)):
			self.immunohist_var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text=self.immunohist_opt[i], variable=self.immunohist_var[i])
			cb.place(x=250, y=y_value)
			self.immunohist_cb.append(cb)
			y_value = y_value + 20

		self.immunohist_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Boosters:", variable=self.immunohist_var[len(self.immunohist_opt)])
		cb.place(x=250, y=y_value)
		self.immunohist_cb.append(cb)
		y_value = y_value + 20

		self.other_booster = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_booster.place(x=300, y=y_value)
		y_value = y_value + 30

		self.immunohist_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Combination:", variable=self.immunohist_var[len(self.immunohist_opt)+1])
		cb.place(x=250, y=y_value)
		self.immunohist_cb.append(cb)
		y_value = y_value + 20

		self.other_combi = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_combi.place(x=300, y=y_value)
		self.immunohist_cb.append(cb)
		y_value = y_value + 30

		self.immunohist_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Others:", variable=self.immunohist_var[len(self.immunohist_opt)+2])
		cb.place(x=250, y=y_value)
		self.immunohist_cb.append(cb)
		y_value = y_value + 20

		self.other_immunohist = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_immunohist.place(x=300, y=y_value)
		y_value = y_value + 30

		phistory_label = tk.Label(form_frame, text="Personal/Social History:", font=self.label_font_2, fg="#636363")
		phistory_label.place(x=250, y=y_value)
		y_value = y_value + 15
		smoker_label = tk.Label(form_frame, text="Smoker", font=self.label_font, fg="#636363")
		smoker_label.place(x=250, y=y_value)
		y_value = y_value + 20

		self.smoker_var = 0

		self.smoker_var_arr = []
		self.smoker_cb = []
		self.smoker_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Yes", variable=self.smoker_var_arr[0])
		cb.place(x=270, y=y_value)
		self.smoker_cb.append(cb)

		self.smoker_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="No", variable=self.smoker_var_arr[1])
		cb.place(x=320, y=y_value)
		self.smoker_cb.append(cb)

		self.smoker_cb[0].config(command=partial(self.check_cb, self.smoker_cb, self.smoker_var_arr, 0, 1))
		self.smoker_cb[1].config(command=partial(self.check_cb, self.smoker_cb, self.smoker_var_arr, 1, 1))

		y_value = y_value + 30

		pack_label = tk.Label(form_frame, text="Pack years?", font=self.label_font, fg="#636363")
		pack_label.place(x=250, y=y_value)
		self.pack_smoke = tk.Text(form_frame, height = 1, width = 5, wrap="word")
		self.pack_smoke.place(x=320, y=y_value)
		y_value = y_value + 30

		self.quit_var = tk.IntVar(self)
		self.quit_cb = tk.Checkbutton(form_frame, text="Quit, when?", variable=self.quit_var)
		self.quit_cb.place(x=250, y=y_value)

		self.quit_cb_text = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.quit_cb_text.place(x=360, y=y_value)
		y_value = y_value + 30

		y_value = 25

		alcohol_label = tk.Label(form_frame, text="Alcohol Beverage Drinker?", font=self.label_font, fg="#636363")
		alcohol_label.place(x=475, y=y_value)
		y_value = y_value + 20

		self.alcohol_var = 0

		self.alcohol_var_arr = []
		self.alcohol_cb = []
		self.alcohol_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Yes", variable=self.alcohol_var_arr[0])
		cb.place(x=495, y=y_value)
		self.alcohol_cb.append(cb)

		self.alcohol_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="No", variable=self.alcohol_var_arr[1])
		cb.place(x=545, y=y_value)
		self.alcohol_cb.append(cb)

		self.alcohol_cb[0].config(command=partial(self.check_cb, self.alcohol_cb, self.alcohol_var_arr, 0, 2))
		self.alcohol_cb[1].config(command=partial(self.check_cb, self.alcohol_cb, self.alcohol_var_arr, 1, 2))
		y_value = y_value + 30

		alco_freq_label = tk.Label(form_frame, text="Frequency?", font=self.label_font, fg="#636363")
		alco_freq_label.place(x=475, y=y_value)
		self.alco_freq = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.alco_freq.place(x=595, y=y_value)
		y_value = y_value + 30

		alco_dur_label = tk.Label(form_frame, text="Duration: ", font=self.label_font, fg="#636363")
		alco_dur_label.place(x=475, y=y_value)
		self.alco_dur = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.alco_dur.place(x=595, y=y_value)
		y_value = y_value + 30

		alco_type_label = tk.Label(form_frame, text="Type of Drink?", font=self.label_font, fg="#636363")
		alco_type_label.place(x=475, y=y_value)
		self.alco_type = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.alco_type.place(x=595, y=y_value)
		y_value = y_value + 30

		exercise_label = tk.Label(form_frame, text="Exercises regularly?", font=self.label_font, fg="#636363")
		exercise_label.place(x=475, y=y_value)
		y_value = y_value + 20

		self.exercise_var = 0

		self.exercise_var_arr = []
		self.exercise_cb = []
		self.exercise_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Yes", variable=self.exercise_var_arr[0])
		cb.place(x=495, y=y_value)
		self.exercise_cb.append(cb)

		self.exercise_var_arr.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="No", variable=self.exercise_var_arr[1])
		cb.place(x=545, y=y_value)
		self.exercise_cb.append(cb)

		self.exercise_cb[0].config(command=partial(self.check_cb, self.exercise_cb, self.exercise_var_arr, 0, 3))
		self.exercise_cb[1].config(command=partial(self.check_cb, self.exercise_cb, self.exercise_var_arr, 1, 3))
		y_value = y_value + 30

		exercise_type_label = tk.Label(form_frame, text="Type of exercise: ", font=self.label_font, fg="#636363")
		exercise_type_label.place(x=475, y=y_value)
		self.exercise_type = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.exercise_type.place(x=595, y=y_value)
		y_value = y_value + 30

		ob_label = tk.Label(form_frame, text="Obstetric/Menstrual History:", font=self.label_font_2, fg="#636363")
		ob_label.place(x=475, y=y_value)
		y_value = y_value + 20

		g_type_label = tk.Label(form_frame, text="G ", font=self.label_font, fg="#636363")
		g_type_label.place(x=475, y=y_value)
		self.g_type = tk.Text(form_frame, height = 1, width = 7, wrap="word")
		self.g_type.place(x=505, y=y_value)
		p_type_label = tk.Label(form_frame, text="P ", font=self.label_font, fg="#636363")
		p_type_label.place(x=575, y=y_value)
		self.p_type = tk.Text(form_frame, height = 1, width = 7, wrap="word")
		self.p_type.place(x=605, y=y_value)
		y_value = y_value + 30

		menarche_label = tk.Label(form_frame, text="Age of menarche", font=self.label_font, fg="#636363")
		menarche_label.place(x=475, y=y_value)
		self.menarche = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.menarche.place(x=595, y=y_value)
		y_value = y_value + 30

		menopause_label = tk.Label(form_frame, text="Age of menopause", font=self.label_font, fg="#636363")
		menopause_label.place(x=475, y=y_value)
		self.menopause = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.menopause.place(x=595, y=y_value)
		y_value = y_value + 30

		coitus_label = tk.Label(form_frame, text="Age at first coitus", font=self.label_font, fg="#636363")
		coitus_label.place(x=475, y=y_value)
		self.coitus = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.coitus.place(x=595, y=y_value)
		y_value = y_value + 30

		bm_label = tk.Label(form_frame, text="Birth/Maternal History:", font=self.label_font_2, fg="#636363")
		bm_label.place(x=475, y=y_value)
		y_value = y_value + 20

		born_label = tk.Label(form_frame, text="Born: ", font=self.label_font, fg="#636363")
		born_label.place(x=475, y=y_value)
		self.born = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.born.place(x=505, y=y_value)
		y_value = y_value + 30

		via_label = tk.Label(form_frame, text="Via: ", font=self.label_font, fg="#636363")
		via_label.place(x=475, y=y_value)
		self.via = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.via.place(x=505, y=y_value)
		y_value = y_value + 30

		to_a_g_label = tk.Label(form_frame, text="to a G", font=self.label_font, fg="#636363")
		to_a_g_label.place(x=475, y=y_value)
		self.to_a_g = tk.Text(form_frame, height = 1, width = 7, wrap="word")
		self.to_a_g.place(x=515, y=y_value)

		bm_p_label = tk.Label(form_frame, text="P", font=self.label_font, fg="#636363")
		bm_p_label.place(x=585, y=y_value)
		self.bm_p = tk.Text(form_frame, height = 1, width = 7, wrap="word")
		self.bm_p.place(x=605, y=y_value)
		y_value = y_value + 30

		bm_year_label = tk.Label(form_frame, text="- year old", font=self.label_font, fg="#636363")
		bm_year_label.place(x=545, y=y_value)
		self.bm_year = tk.Text(form_frame, height = 1, width = 7, wrap="word")
		self.bm_year.place(x=485, y=y_value)
		y_value = y_value + 30

		mbcompli_label = tk.Label(form_frame, text="Mother birth complications?", font=self.label_font, fg="#636363")
		mbcompli_label.place(x=475, y=y_value)
		y_value = y_value + 20
		self.mb_compli = tk.Text(form_frame, height = 1, width = 25, wrap="word")
		self.mb_compli.place(x=485, y=y_value)
		y_value = y_value + 30

		self.add_button = tk.Button(form_frame, text="ADD", command=lambda: self.add_details(), height = 2, width = 10, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007")
		self.add_button.place(x=875, y=65)

		# add selected details from checkboxes
		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("review_of_systems_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def add_details(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		try:
			val = int(self.controller.get_page("FirstConsForm").p_age.get("1.0",'end-1c'))
		except ValueError:
			try:
				val = float(self.controller.get_page("FirstConsForm").p_age.get("1.0",'end-1c'))
			except ValueError:
				messagebox.showwarning("Warning", "Invalid age input! Enter a number")
		else:
			cur.execute(("SELECT patient_id FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				FirstConsForm = self.controller.get_page("FirstConsForm")
				sql = "INSERT INTO patient (last_name, first_name, middle_name, address, birthdate, age, gender, civil_status, contact_no, occupation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
				val = (FirstConsForm.p_lname.get("1.0",'end-1c'), FirstConsForm.p_fname.get("1.0",'end-1c'), FirstConsForm.p_mname.get("1.0",'end-1c'), FirstConsForm.p_addr.get("1.0",'end-1c'), 
					FirstConsForm.p_bday.get_date().strftime('%Y-%m-%d'), int(FirstConsForm.p_age.get("1.0",'end-1c')), FirstConsForm.p_gender.get("1.0",'end-1c'), FirstConsForm.p_civil_stat.get("1.0",'end-1c'), 
					FirstConsForm.p_contact.get("1.0",'end-1c'), FirstConsForm.p_occup.get("1.0",'end-1c'))

				cur.execute(sql, val)
				mydb.commit()

				cur.execute("SELECT LAST_INSERT_ID()")

				FirstConsForm.p_lname.delete('1.0', 'end')
				FirstConsForm.p_fname.delete('1.0', 'end')
				FirstConsForm.p_mname.delete('1.0', 'end')
				FirstConsForm.p_addr.delete('1.0', 'end')
				FirstConsForm.p_age.delete('1.0', 'end')
				FirstConsForm.p_gender.delete('1.0', 'end')
				FirstConsForm.p_civil_stat.delete('1.0', 'end')
				FirstConsForm.p_contact.delete('1.0', 'end')
				FirstConsForm.p_occup.delete('1.0', 'end')
				FirstConsForm.p_bday.set_date(dt.datetime.today())
				
				self.controller.patient_id.set(cur.fetchone()[0])

				sql = "INSERT INTO patientconsultation (date_of_consult, complaint, history_of_illness, context, present_medication, patient_id) VALUES (%s, %s, %s, %s, %s, %s)"
				val = (FirstConsForm.p_datecons.get_date().strftime('%Y-%m-%d'), FirstConsForm.p_compliant.get("1.0",'end-1c'), FirstConsForm.p_hist_illness.get("1.0",'end-1c'), FirstConsForm.p_context.get("1.0",'end-1c'), FirstConsForm.p_pres_med.get("1.0",'end-1c'), int(self.controller.patient_id.get()))

				cur.execute(sql, val)
				mydb.commit()

				FirstConsForm.p_datecons.set_date(dt.datetime.today())
				FirstConsForm.p_compliant.delete('1.0', 'end')
				FirstConsForm.p_hist_illness.delete('1.0', 'end')
				FirstConsForm.p_context.delete('1.0', 'end')
				FirstConsForm.p_pres_med.delete('1.0', 'end')
				FirstConsForm.p_gender.delete('1.0', 'end')

				review_of_systems_form = self.controller.get_page("review_of_systems_form")
				review_of_systems_form.add_details()

				cur.execute(("SELECT famhist_illness FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (famhist_illness, patient_id) VALUES (%s, %s)"), (self.medhist_illness.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET famhist_illness = %s WHERE patient_id = %s"), (self.medhist_illness.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT famhist_hospt FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (famhist_hospt, patient_id) VALUES (%s, %s)"), (self.medhist_hospt.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET famhist_hospt = %s WHERE patient_id = %s"), (self.medhist_hospt.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT famhist_allergy FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (famhist_allergy, patient_id) VALUES (%s, %s)"), (self.medhist_allergy.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET famhist_allergy = %s WHERE patient_id = %s"), (self.medhist_allergy.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				self.medhist_illness.delete('1.0', 'end') 
				self.medhist_hospt.delete('1.0', 'end') 
				self.medhist_allergy.delete('1.0', 'end') 


				cur.execute(("SELECT famhist_1, famhist_2, famhist_3, famhist_4, famhist_5, famhist_6, famhist_7 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (famhist_1, famhist_2, famhist_3, famhist_4, famhist_5, famhist_6, famhist_7, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
					val = (self.famhist_var[0].get(), self.famhist_var[1].get(), self.famhist_var[2].get(), self.famhist_var[3].get(), self.famhist_var[4].get(), 
						self.famhist_var[5].get(), self.famhist_var[6].get(),self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET famhist_1 = %s, famhist_2 = %s, famhist_3 = %s, famhist_4 = %s, famhist_5 = %s, famhist_6 = %s, famhist_7 = %s WHERE patient_id = %s"
					val = (self.famhist_var[0].get(), self.famhist_var[1].get(), self.famhist_var[2].get(), self.famhist_var[3].get(), self.famhist_var[4].get(), 
						self.famhist_var[5].get(), self.famhist_var[6].get(), self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.famhist_var[len(self.famhist_opt)].get() == 1:
					cur.execute(("SELECT famhist_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (famhist_others, patient_id) VALUES (%s, %s)"), (self.other_famhist.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET famhist_others = %s WHERE patient_id = %s"), (self.other_famhist.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT famhist_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (famhist_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET famhist_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				cur.execute(("SELECT immuno_1, immuno_2, immuno_3, immuno_4, immuno_5, immuno_6, immuno_7, immuno_8, immuno_9, immuno_10, immuno_11, immuno_12, immuno_13, immuno_14, immuno_15 FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (immuno_1, immuno_2, immuno_3, immuno_4, immuno_5, immuno_6, immuno_7, immuno_8, immuno_9, immuno_10, immuno_11, immuno_12, immuno_13, immuno_14, immuno_15, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
					val = (self.immunohist_var[0].get(), self.immunohist_var[1].get(), self.immunohist_var[2].get(), self.immunohist_var[3].get(), self.immunohist_var[4].get(), 
						self.immunohist_var[5].get(), self.immunohist_var[6].get(), self.immunohist_var[7].get(), self.immunohist_var[8].get(), self.immunohist_var[9].get(), 
						self.immunohist_var[10].get(), self.immunohist_var[11].get(), self.immunohist_var[12].get(), self.immunohist_var[13].get(), self.immunohist_var[14].get(), self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET immuno_1 = %s, immuno_2 = %s, immuno_3 = %s, immuno_4 = %s, immuno_5 = %s, immuno_6 = %s, immuno_7 = %s, immuno_8 = %s, immuno_9 = %s, immuno_10 = %s, immuno_11 = %s, immuno_12 = %s, immuno_13 = %s, immuno_14 = %s, immuno_15 = %s WHERE patient_id = %s"
					val = (self.immunohist_var[0].get(), self.immunohist_var[1].get(), self.immunohist_var[2].get(), self.immunohist_var[3].get(), self.immunohist_var[4].get(), 
						self.immunohist_var[5].get(), self.immunohist_var[6].get(), self.immunohist_var[7].get(), self.immunohist_var[8].get(), self.immunohist_var[9].get(), 
						self.immunohist_var[10].get(), self.immunohist_var[11].get(), self.immunohist_var[12].get(), self.immunohist_var[13].get(), self.immunohist_var[14].get(), self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.immunohist_var[len(self.immunohist_opt)].get() == 1:
					cur.execute(("SELECT immuno_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_others, patient_id) VALUES (%s, %s)"), (self.other_immunohist.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_others = %s WHERE patient_id = %s"), (self.other_immunohist.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT immuno_others FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				if self.immunohist_var[len(self.immunohist_opt)+1].get() == 1:
					cur.execute(("SELECT immuno_booster FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_booster, patient_id) VALUES (%s, %s)"), (self.other_booster.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_booster = %s WHERE patient_id = %s"), (self.other_booster.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT immuno_booster FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_booster, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_booster = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				if self.immunohist_var[len(self.immunohist_opt)+2].get() == 1:
					cur.execute(("SELECT immuno_combi FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_combi, patient_id) VALUES (%s, %s)"), (self.other_combi.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_combi = %s WHERE patient_id = %s"), (self.other_combi.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT immuno_combi FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (immuno_combi, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET immuno_combi = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				for i in range(len(self.famhist_var)):
					if i >= len(self.famhist_opt):
						if self.famhist_var[i].get() == 1:
							self.other_famhist.delete('1.0', 'end') 
					self.famhist_var[i] = tk.IntVar(self)

				for i in range(len(self.immunohist_var)):
					if i >= len(self.immunohist_opt):
						if i == len(self.immunohist_opt):
							if self.immunohist_var[i].get() == 1:
								self.other_booster.delete('1.0', 'end')
						elif i == len(self.immunohist_opt)+1:
							if self.immunohist_var[i].get() == 1:
								self.other_combi.delete('1.0', 'end')
						elif i == len(self.immunohist_opt)+2:
							if self.immunohist_var[i].get() == 1:
								self.other_immunohist.delete('1.0', 'end')
					self.immunohist_var[i] = tk.IntVar(self)

				cur.execute(("SELECT smoker FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (smoker, patient_id) VALUES (%s, %s)"
					val = (self.smoker_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET smoker = %s WHERE patient_id = %s"
					val = (self.smoker_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.smoker_var == 1:
					cur.execute(("SELECT smoker_pack FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (smoker_pack, patient_id) VALUES (%s, %s)"), (self.pack_smoke.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET smoker_pack = %s WHERE patient_id = %s"), (self.pack_smoke.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT smoker_pack FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (smoker_pack, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET smoker_pack = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				cur.execute(("SELECT smoker_quit FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (smoker_quit, patient_id) VALUES (%s, %s)"
					val = (self.quit_var.get(), self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET smoker_quit = %s WHERE patient_id = %s"
					val = (self.quit_var.get(), self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.quit_var.get() == 1:
					cur.execute(("SELECT smoker_quit_when FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (smoker_quit_when, patient_id) VALUES (%s, %s)"), (self.quit_cb_text.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET smoker_quit_when = %s WHERE patient_id = %s"), (self.quit_cb_text.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT smoker_quit_when FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (smoker_quit_when, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET smoker_quit_when = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				cur.execute(("SELECT drinker FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (drinker, patient_id) VALUES (%s, %s)"
					val = (self.alcohol_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET drinker = %s WHERE patient_id = %s"
					val = (self.alcohol_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.alcohol_var == 1:
					cur.execute(("SELECT drinker_freq FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_freq, patient_id) VALUES (%s, %s)"), (self.alco_freq.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_freq = %s WHERE patient_id = %s"), (self.alco_freq.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()

					cur.execute(("SELECT drinker_dur FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_dur, patient_id) VALUES (%s, %s)"), (self.alco_dur.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_dur = %s WHERE patient_id = %s"), (self.alco_dur.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()

					cur.execute(("SELECT drinker_type FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_type, patient_id) VALUES (%s, %s)"), (self.alco_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_type = %s WHERE patient_id = %s"), (self.alco_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT drinker_freq FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_freq, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_freq = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

					cur.execute(("SELECT drinker_dur FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_dur, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_dur = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

					cur.execute(("SELECT drinker_type FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (drinker_type, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET drinker_type = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				cur.execute(("SELECT exercise FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					sql = "INSERT INTO patientrevofsys (exercise, patient_id) VALUES (%s, %s)"
					val = (self.exercise_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()
				else:
					sql = "UPDATE patientrevofsys SET exercise = %s WHERE patient_id = %s"
					val = (self.exercise_var, self.controller.patient_id.get())
					cur.execute(sql, val)
					mydb.commit()

				if self.exercise_var == 1:
					cur.execute(("SELECT exercise_type FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (exercise_type, patient_id) VALUES (%s, %s)"), (self.exercise_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET exercise_type = %s WHERE patient_id = %s"), (self.exercise_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
						mydb.commit()
				else:
					cur.execute(("SELECT exercise_type FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
					res = cur.fetchone()
					if res is None:
						cur.execute(("INSERT INTO patientrevofsys (exercise_type, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
						mydb.commit()
					else:
						cur.execute(("UPDATE patientrevofsys SET exercise_type = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
						mydb.commit()

				####################################

				cur.execute(("SELECT ob_g FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (ob_g, patient_id) VALUES (%s, %s)"), (self.g_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET ob_g = %s WHERE patient_id = %s"), (self.g_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT ob_p FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (ob_p, patient_id) VALUES (%s, %s)"), (self.p_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET ob_p = %s WHERE patient_id = %s"), (self.p_type.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT menarche FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (menarche, patient_id) VALUES (%s, %s)"), (self.menarche.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET menarche = %s WHERE patient_id = %s"), (self.menarche.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT menopause FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (menopause, patient_id) VALUES (%s, %s)"), (self.menopause.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET menopause = %s WHERE patient_id = %s"), (self.menopause.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT coitus FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (coitus, patient_id) VALUES (%s, %s)"), (self.coitus.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET coitus = %s WHERE patient_id = %s"), (self.coitus.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT bm_born FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_born, patient_id) VALUES (%s, %s)"), (self.born.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_born = %s WHERE patient_id = %s"), (self.born.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT bm_via FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_via, patient_id) VALUES (%s, %s)"), (self.via.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_via = %s WHERE patient_id = %s"), (self.via.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				
				cur.execute(("SELECT bm_g FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_g, patient_id) VALUES (%s, %s)"), (self.to_a_g.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_g = %s WHERE patient_id = %s"), (self.to_a_g.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				
				cur.execute(("SELECT bm_p FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_p, patient_id) VALUES (%s, %s)"), (self.bm_p.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_p = %s WHERE patient_id = %s"), (self.bm_p.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				
				cur.execute(("SELECT bm_year FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_year, patient_id) VALUES (%s, %s)"), (self.bm_year.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_year = %s WHERE patient_id = %s"), (self.bm_year.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()

				cur.execute(("SELECT bm_compli FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
				res = cur.fetchone()
				if res is None:
					cur.execute(("INSERT INTO patientrevofsys (bm_compli, patient_id) VALUES (%s, %s)"), (self.mb_compli.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				else:
					cur.execute(("UPDATE patientrevofsys SET bm_compli = %s WHERE patient_id = %s"), (self.mb_compli.get("1.0",'end-1c'), self.controller.patient_id.get()))
					mydb.commit()
				

				self.pack_smoke.delete('1.0', 'end') 
				self.quit_cb_text.delete('1.0', 'end') 
				self.alco_freq.delete('1.0', 'end') 
				self.alco_dur.delete('1.0', 'end') 
				self.alco_type.delete('1.0', 'end') 
				self.exercise_type.delete('1.0', 'end') 
				self.g_type.delete('1.0', 'end') 
				self.p_type.delete('1.0', 'end') 
				self.menarche.delete('1.0', 'end') 
				self.menopause.delete('1.0', 'end') 
				self.coitus.delete('1.0', 'end') 
				self.born.delete('1.0', 'end') 
				self.via.delete('1.0', 'end') 
				self.to_a_g.delete('1.0', 'end') 
				self.bm_p.delete('1.0', 'end') 
				self.bm_year.delete('1.0', 'end') 
				self.mb_compli.delete('1.0', 'end') 
				
				self.controller.show_frame("FirstConsForm")

			else:
				FirstConsForm = self.controller.get_page("FirstConsForm")
				sql = "UPDATE patient SET last_name = %s, first_name = %s, middle_name = %s, address = %s, birthdate = %s, age = %s, gender = %s, civil_status = %s, contact_no = %s, occupation = %s WHERE patient_id = %s"
				val = (FirstConsForm.p_lname.get("1.0",'end-1c'), FirstConsForm.p_fname.get("1.0",'end-1c'), FirstConsForm.p_mname.get("1.0",'end-1c'), FirstConsForm.p_addr.get("1.0",'end-1c'), 
					FirstConsForm.p_bday.get_date().strftime('%Y-%m-%d'), int(FirstConsForm.p_age.get("1.0",'end-1c')), FirstConsForm.p_gender.get("1.0",'end-1c'), FirstConsForm.p_civil_stat.get("1.0",'end-1c'), 
					FirstConsForm.p_contact.get("1.0",'end-1c'), FirstConsForm.p_occup.get("1.0",'end-1c'), self.controller.patient_id.get())

				cur.execute(sql, val)
				mydb.commit()

				FirstConsForm.p_lname.delete('1.0', 'end')
				FirstConsForm.p_fname.delete('1.0', 'end')
				FirstConsForm.p_mname.delete('1.0', 'end')
				FirstConsForm.p_addr.delete('1.0', 'end')
				FirstConsForm.p_age.delete('1.0', 'end')
				FirstConsForm.p_gender.delete('1.0', 'end')
				FirstConsForm.p_civil_stat.delete('1.0', 'end')
				FirstConsForm.p_contact.delete('1.0', 'end')
				FirstConsForm.p_occup.delete('1.0', 'end')
				FirstConsForm.p_bday.set_date(dt.datetime.today())

				self.controller.show_frame("FirstConsForm")

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT famhist_1, famhist_2, famhist_3, famhist_4, famhist_5, famhist_6, famhist_7, immuno_1, immuno_2, immuno_3, immuno_4, immuno_5, immuno_6, immuno_7, immuno_8, immuno_9, immuno_10, immuno_11, immuno_12, immuno_13, immuno_14, immuno_15, smoker, drinker, exercise FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(len(self.famhist_var)):
				if res[i] is not None:
					self.famhist_var[i].set(res[i])

			for i in range(len(self.immunohist_var)):
				if res[i+7] is not None:
					self.immunohist_var[i].set(res[i+7])

			if res[22] is not None:
				if res[22] == 0:
					self.smoker_var_arr[0].set(0)
					self.smoker_var_arr[1].set(1)
				elif res[22] == 1:
					self.smoker_var_arr[0].set(1)
					self.smoker_var_arr[1].set(0)
				else:
					self.smoker_var_arr[0].set(0)
				self.smoker_var_arr[1].set(0)

			if res[23] is not None:
				if res[23] == 0:
					self.alcohol_var_arr[0].set(0)
					self.alcohol_var_arr[1].set(1)
				elif res[23] == 1:
					self.alcohol_var_arr[0].set(1)
					self.alcohol_var_arr[1].set(0)
				else:
					self.alcohol_var_arr[0].set(0)
					self.alcohol_var_arr[1].set(0)

			if res[24] is not None:
				if res[24] == 0:
					self.exercise_var_arr[0].set(0)
					self.exercise_var_arr[1].set(1)
				elif res[24] == 1:
					self.exercise_var_arr[0].set(1)
					self.exercise_var_arr[1].set(0)
				else:
					self.exercise_var_arr[0].set(0)
					self.exercise_var_arr[1].set(0)


		else:
			for i in range(7):
				self.famhist_var[i].set(0)

			for i in range(15):
				self.immunohist_var[i].set(0)
			for i in range(2):
				self.smoker_var_arr[i].set(0)
				self.alcohol_var_arr[i].set(0)
				self.exercise_var_arr[i].set(0)

		self.medhist_illness.delete('1.0', 'end')
		self.medhist_hospt.delete('1.0', 'end')
		self.medhist_allergy.delete('1.0', 'end')
		self.other_famhist.delete('1.0', 'end')
		self.other_booster.delete('1.0', 'end')
		self.other_combi.delete('1.0', 'end')
		self.other_immunohist.delete('1.0', 'end')
		self.pack_smoke.delete('1.0', 'end')
		self.quit_cb_text.delete('1.0', 'end')
		self.alco_freq.delete('1.0', 'end')
		self.alco_dur.delete('1.0', 'end')
		self.alco_type.delete('1.0', 'end')
		self.exercise_type.delete('1.0', 'end')
		self.g_type.delete('1.0', 'end')
		self.p_type.delete('1.0', 'end')
		self.menarche.delete('1.0', 'end')
		self.menopause.delete('1.0', 'end')
		self.coitus.delete('1.0', 'end')
		self.born.delete('1.0', 'end')
		self.via.delete('1.0', 'end')
		self.to_a_g.delete('1.0', 'end')
		self.bm_p.delete('1.0', 'end')
		self.bm_year.delete('1.0', 'end')
		self.mb_compli.delete('1.0', 'end')
		
		cur.execute(("SELECT famhist_illness, famhist_hospt, famhist_allergy, famhist_others, immuno_booster, immuno_combi, immuno_others, smoker_pack, smoker_quit_when, drinker_freq, drinker_dur, drinker_type, exercise_type, ob_g, ob_p, menarche, menopause, coitus, bm_born, bm_via, bm_g, bm_p, bm_year, bm_compli FROM patientrevofsys WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				self.medhist_illness.insert('1.0', res[0])
			if res[1] is not None:
				self.medhist_hospt.insert('1.0', res[1])
			if res[2] is not None:
				self.medhist_allergy.insert('1.0', res[2])
			if res[3] is not None:
				self.other_famhist.insert('1.0', res[3])
			if res[4] is not None:
				self.other_booster.insert('1.0', res[4])
			if res[5] is not None:
				self.other_combi.insert('1.0', res[5])
			if res[6] is not None:
				self.other_immunohist.insert('1.0', res[6])
			if res[7] is not None:
				self.pack_smoke.insert('1.0', res[7])
			if res[8] is not None:
				self.quit_cb_text.insert('1.0', res[8])
			if res[9] is not None:
				self.alco_freq.insert('1.0', res[9])
			if res[10] is not None:
				self.alco_dur.insert('1.0', res[10])
			if res[11] is not None:
				self.alco_type.insert('1.0', res[11])
			if res[12] is not None:
				self.exercise_type.insert('1.0', res[12])
			if res[13] is not None:
				self.g_type.insert('1.0', res[13])
			if res[14] is not None:
				self.p_type.insert('1.0', res[14])
			if res[15] is not None:
				self.menarche.insert('1.0', res[15])
			if res[16] is not None:
				self.menopause.insert('1.0', res[16])
			if res[17] is not None:
				self.coitus.insert('1.0', res[17])
			if res[18] is not None:
				self.born.insert('1.0', res[18])
			if res[19] is not None:
				self.via.insert('1.0', res[19])
			if res[20] is not None:
				self.to_a_g.insert('1.0', res[20])
			if res[21] is not None:
				self.bm_p.insert('1.0', res[21])
			if res[22] is not None:
				self.bm_year.insert('1.0', res[22])
			if res[23] is not None:
				self.mb_compli.insert('1.0', res[23])

			for i in range(len(self.famhist_cb)):
				self.famhist_cb[i].config(state = "disabled")

			for i in range(len(self.immunohist_cb)):
				self.immunohist_cb[i].config(state = "disabled")

			self.smoker_cb[0].config(state = "disabled")
			self.smoker_cb[1].config(state = "disabled")
			self.alcohol_cb[0].config(state = "disabled")
			self.alcohol_cb[1].config(state = "disabled")
			self.exercise_cb[0].config(state = "disabled")
			self.exercise_cb[1].config(state = "disabled")
			self.medhist_illness.config(state = "disabled", bg = "#e8e8e8")
			self.medhist_hospt.config(state = "disabled", bg = "#e8e8e8")
			self.medhist_allergy.config(state = "disabled", bg = "#e8e8e8")
			self.other_famhist.config(state = "disabled", bg = "#e8e8e8")
			self.other_booster.config(state = "disabled", bg = "#e8e8e8")
			self.other_combi.config(state = "disabled", bg = "#e8e8e8")
			self.other_immunohist.config(state = "disabled", bg = "#e8e8e8")
			self.pack_smoke.config(state = "disabled", bg = "#e8e8e8")
			self.quit_cb.config(state = "disabled")
			self.quit_cb_text.config(state = "disabled", bg = "#e8e8e8")
			self.alco_freq.config(state = "disabled", bg = "#e8e8e8")
			self.alco_dur.config(state = "disabled", bg = "#e8e8e8")
			self.alco_type.config(state = "disabled", bg = "#e8e8e8")
			self.exercise_type.config(state = "disabled", bg = "#e8e8e8")
			self.g_type.config(state = "disabled", bg = "#e8e8e8")
			self.p_type.config(state = "disabled", bg = "#e8e8e8")
			self.menarche.config(state = "disabled", bg = "#e8e8e8")
			self.menopause.config(state = "disabled", bg = "#e8e8e8")
			self.coitus.config(state = "disabled", bg = "#e8e8e8")
			self.born.config(state = "disabled", bg = "#e8e8e8")
			self.via.config(state = "disabled", bg = "#e8e8e8")
			self.to_a_g.config(state = "disabled", bg = "#e8e8e8")
			self.bm_p.config(state = "disabled", bg = "#e8e8e8")
			self.bm_year.config(state = "disabled", bg = "#e8e8e8")
			self.mb_compli.config(state = "disabled", bg = "#e8e8e8")
			self.add_button.config(state = "disabled")
		else:
			self.medhist_illness.delete('1.0', 'end')
			self.medhist_hospt.delete('1.0', 'end')
			self.medhist_allergy.delete('1.0', 'end')
			self.other_famhist.delete('1.0', 'end')
			self.other_booster.delete('1.0', 'end')
			self.other_combi.delete('1.0', 'end')
			self.other_immunohist.delete('1.0', 'end')
			self.pack_smoke.delete('1.0', 'end')
			self.quit_cb_text.delete('1.0', 'end')
			self.alco_freq.delete('1.0', 'end')
			self.alco_dur.delete('1.0', 'end')
			self.alco_type.delete('1.0', 'end')
			self.exercise_type.delete('1.0', 'end')
			self.g_type.delete('1.0', 'end')
			self.p_type.delete('1.0', 'end')
			self.menarche.delete('1.0', 'end')
			self.menopause.delete('1.0', 'end')
			self.coitus.delete('1.0', 'end')
			self.born.delete('1.0', 'end')
			self.via.delete('1.0', 'end')
			self.to_a_g.delete('1.0', 'end')
			self.bm_p.delete('1.0', 'end')
			self.bm_year.delete('1.0', 'end')
			self.mb_compli.delete('1.0', 'end')
			for i in range(len(self.famhist_cb)):
				self.famhist_cb[i].config(state = "normal")

			for i in range(len(self.immunohist_cb)):
				self.immunohist_cb[i].config(state = "normal")

			self.smoker_cb[0].config(state = "normal")
			self.smoker_cb[1].config(state = "normal")
			self.alcohol_cb[0].config(state = "normal")
			self.alcohol_cb[1].config(state = "normal")
			self.exercise_cb[0].config(state = "normal")
			self.exercise_cb[1].config(state = "normal")
			self.medhist_illness.config(state = "normal", bg = "#ffffff")
			self.medhist_hospt.config(state = "normal", bg = "#ffffff")
			self.medhist_allergy.config(state = "normal", bg = "#ffffff")
			self.other_famhist.config(state = "normal", bg = "#ffffff")
			self.other_booster.config(state = "normal", bg = "#ffffff")
			self.other_combi.config(state = "normal", bg = "#ffffff")
			self.other_immunohist.config(state = "normal", bg = "#ffffff")
			self.pack_smoke.config(state = "normal", bg = "#ffffff")
			self.quit_cb.config(state = "normal")
			self.quit_cb_text.config(state = "normal", bg = "#ffffff")
			self.alco_freq.config(state = "normal", bg = "#ffffff")
			self.alco_dur.config(state = "normal", bg = "#ffffff")
			self.alco_type.config(state = "normal", bg = "#ffffff")
			self.exercise_type.config(state = "normal", bg = "#ffffff")
			self.g_type.config(state = "normal", bg = "#ffffff")
			self.p_type.config(state = "normal", bg = "#ffffff")
			self.menarche.config(state = "normal", bg = "#ffffff")
			self.menopause.config(state = "normal", bg = "#ffffff")
			self.coitus.config(state = "normal", bg = "#ffffff")
			self.born.config(state = "normal", bg = "#ffffff")
			self.via.config(state = "normal", bg = "#ffffff")
			self.to_a_g.config(state = "normal", bg = "#ffffff")
			self.bm_p.config(state = "normal", bg = "#ffffff")
			self.bm_year.config(state = "normal", bg = "#ffffff")
			self.mb_compli.config(state = "normal", bg = "#ffffff")
			self.add_button.config(state = "normal")

	def check_cb(self, cb_arr, cb_var_arr, i, question):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				if question == 1:
					self.smoker_var = 1
				elif question == 2:
					self.alcohol_var = 1
				else:
					self.exercise_var = 1
				cb_arr[i+1].config(state="disabled")
			else:
				if question == 1:
					self.smoker_var = 2
				elif question == 2:
					self.alcohol_var = 2
				else:
					self.exercise_var = 2
				cb_arr[i+1].config(state="normal")
		else:
			if cb_var_arr[i].get() == 1:
				if question == 1:
					self.smoker_var = 0
				elif question == 2:
					self.alcohol_var = 0
				else:
					self.exercise_var = 0
				cb_arr[i-1].config(state="disabled")
			else:
				if question == 1:
					self.smoker_var = 2
				elif question == 2:
					self.alcohol_var = 2
				else:
					self.exercise_var = 2
				cb_arr[i-1].config(state="normal")

class physical_examination_form(tk.Frame): # Form containing the Physical Examination before the Assessment Table

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_1(self, self.controller, 2)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		y_value = 25

		pe_label = tk.Label(form_frame, text="Physical Examination", font=self.label_font_2, fg="#636363")
		pe_label.place(x=25, y=y_value)

		hr_label = tk.Label(form_frame, text="HR:", font=self.label_font, fg="#636363")
		hr_label.place(x=150, y=y_value)

		self.hr = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.hr.place(x=175, y=y_value)

		bp_label = tk.Label(form_frame, text="BP:", font=self.label_font, fg="#636363")
		bp_label.place(x=220, y=y_value)

		self.bp = tk.Text(form_frame, height = 1, width = 6, wrap="word")
		self.bp.place(x=245, y=y_value)

		rr_label = tk.Label(form_frame, text="RR:", font=self.label_font, fg="#636363")
		rr_label.place(x=300, y=y_value)

		self.rr = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.rr.place(x=325, y=y_value)

		temp_label = tk.Label(form_frame, text="Temperature:", font=self.label_font, fg="#636363")
		temp_label.place(x=375, y=y_value)

		self.temp = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.temp.place(x=445, y=y_value)

		height_label = tk.Label(form_frame, text="Height:", font=self.label_font, fg="#636363")
		height_label.place(x=490, y=y_value)

		self.height = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.height.place(x=530, y=y_value)

		bmi_label = tk.Label(form_frame, text="BMI:", font=self.label_font, fg="#636363")
		bmi_label.place(x=580, y=y_value)

		self.bmi = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.bmi.place(x=605, y=y_value)

		ibw_label = tk.Label(form_frame, text="IBW:", font=self.label_font, fg="#636363")
		ibw_label.place(x=660, y=y_value)

		self.ibw = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.ibw.place(x=690, y=y_value)

		hipcirc_label = tk.Label(form_frame, text="Hip Circ.:", font=self.label_font, fg="#636363")
		hipcirc_label.place(x=740, y=y_value)

		self.hipcirc = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.hipcirc.place(x=790, y=y_value)

		y_value = y_value + 30

		waistcirc_label = tk.Label(form_frame, text="Waist Circ.:", font=self.label_font, fg="#636363")
		waistcirc_label.place(x=520, y=y_value)

		self.waistcirc = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.waistcirc.place(x=585, y=y_value)

		headcirc_label = tk.Label(form_frame, text="Head Circ.:", font=self.label_font, fg="#636363")
		headcirc_label.place(x=630, y=y_value)

		self.headcirc = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.headcirc.place(x=690, y=y_value)

		abw_label = tk.Label(form_frame, text="ABW:", font=self.label_font, fg="#636363")
		abw_label.place(x=755, y=y_value)

		self.abw = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.abw.place(x=790, y=y_value)

		y_value = y_value + 15
		ge_label = tk.Label(form_frame, text="General Survey:", font=self.label_font_2, fg="#636363")
		ge_label.place(x=25, y=y_value)

		self.listvar = []

		self.ge_var = []
		self.ge_cb = []
		self.ge_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ge_var[0])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)
		y_value = y_value + 25

		self.ge_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ge_var[1])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)

		self.ge_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ge_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.ge_cb[0].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 0, 0))
		self.ge_cb[1].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 1, 0))

		y_value = y_value + 25
		sk_label = tk.Label(form_frame, text="Skin/Integument:", font=self.label_font_2, fg="#636363")
		sk_label.place(x=25, y=y_value)

		self.sk_var = []
		self.sk_cb = []
		self.sk_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.sk_var[0])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)
		y_value = y_value + 25

		self.sk_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.sk_var[1])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)

		self.sk_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.sk_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.sk_cb[0].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 0, 1))
		self.sk_cb[1].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 1, 1))

		y_value = y_value + 25
		mu_label = tk.Label(form_frame, text="Musculoskeletal:", font=self.label_font_2, fg="#636363")
		mu_label.place(x=25, y=y_value)

		self.mu_var = []
		self.mu_cb = []
		self.mu_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.mu_var[0])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)
		y_value = y_value + 25

		self.mu_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.mu_var[1])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)

		self.mu_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.mu_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.mu_cb[0].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 0, 2))
		self.mu_cb[1].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 1, 2))

		y_value = y_value + 25
		he_label = tk.Label(form_frame, text="HEENT:", font=self.label_font_2, fg="#636363")
		he_label.place(x=25, y=y_value)

		self.he_var = []
		self.he_cb = []
		self.he_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.he_var[0])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)
		y_value = y_value + 25

		self.he_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.he_var[1])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)

		self.he_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.he_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.he_cb[0].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 0, 3))
		self.he_cb[1].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 1, 3))

		y_value = y_value + 25
		re_label = tk.Label(form_frame, text="Respiratory:", font=self.label_font_2, fg="#636363")
		re_label.place(x=25, y=y_value)

		self.re_var = []
		self.re_cb = []
		self.re_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.re_var[0])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)
		y_value = y_value + 25

		self.re_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.re_var[1])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)

		self.re_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.re_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.re_cb[0].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 0, 4))
		self.re_cb[1].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 1, 4))

		y_value = y_value + 25
		ca_label = tk.Label(form_frame, text="Cardiovascular:", font=self.label_font_2, fg="#636363")
		ca_label.place(x=25, y=y_value)

		self.ca_var = []
		self.ca_cb = []
		self.ca_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ca_var[0])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)
		y_value = y_value + 25

		self.ca_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ca_var[1])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)

		self.ca_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ca_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.ca_cb[0].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 0, 5))
		self.ca_cb[1].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 1, 5))

		y_value = y_value + 25
		ga_label = tk.Label(form_frame, text="Gastrointestinal:", font=self.label_font_2, fg="#636363")
		ga_label.place(x=25, y=y_value)

		self.ga_var = []
		self.ga_cb = []
		self.ga_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ga_var[0])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)
		y_value = y_value + 25

		self.ga_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ga_var[1])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)

		self.ga_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ga_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.ga_cb[0].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 0, 6))
		self.ga_cb[1].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 1, 6))

		y_value = y_value + 25
		gn_label = tk.Label(form_frame, text="Genitourinary:", font=self.label_font_2, fg="#636363")
		gn_label.place(x=25, y=y_value)

		self.gn_var = []
		self.gn_cb = []
		self.gn_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.gn_var[0])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)
		y_value = y_value + 25

		self.gn_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.gn_var[1])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)

		self.gn_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.gn_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.gn_cb[0].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 0, 7))
		self.gn_cb[1].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 1, 7))

		y_value = y_value + 25
		ie_label = tk.Label(form_frame, text="IE:", font=self.label_font_2, fg="#636363")
		ie_label.place(x=25, y=y_value)

		self.ie_var = []
		self.ie_cb = []
		self.ie_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ie_var[0])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)
		y_value = y_value + 25

		self.ie_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ie_var[1])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)

		self.ie_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ie_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.ie_cb[0].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 0, 8))
		self.ie_cb[1].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 1, 8))

		y_value = y_value + 25
		dre_label = tk.Label(form_frame, text="DRE:", font=self.label_font_2, fg="#636363")
		dre_label.place(x=25, y=y_value)

		self.dre_var = []
		self.dre_cb = []
		self.dre_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.dre_var[0])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)
		y_value = y_value + 25

		self.dre_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.dre_var[1])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)

		self.dre_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.dre_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.dre_cb[0].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 0, 9))
		self.dre_cb[1].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 1, 9))

		y_value = y_value + 25
		ne_label = tk.Label(form_frame, text="Neuropsych:", font=self.label_font_2, fg="#636363")
		ne_label.place(x=25, y=y_value)

		self.ne_var = []
		self.ne_cb = []
		self.ne_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ne_var[0])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)
		y_value = y_value + 25

		self.ne_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ne_var[1])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)

		self.ne_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ne_find.place(x=225, y=y_value)

		self.listvar.append(0)

		self.ne_cb[0].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 0, 10))
		self.ne_cb[1].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 1, 10))

		y_value = y_value + 25

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("assessment_table"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

		tk.Label(form_frame, text="*BMI weight in kg height in meters squared or weight in lbs x 705 inches", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=200)
		tk.Label(form_frame, text="**IBW quick estimate:", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=280)
		tk.Label(form_frame, text="for females 105 lbs for first 5 feet+ 5 lbs for every inch above five feet, for males 106 lbs for first 5 feet and 5 lbs for every inch above five feet", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=325)

	def check_cb(self, cb_arr, cb_var_arr, textfield, i, index):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				cb_arr[i+1].config(state="disabled")
				textfield.config(state="disabled", bg = "#e8e8e8")
			else:
				cb_arr[i+1].config(state="normal")
				textfield.config(state="normal", bg = "#ffffff")
			self.listvar[index] = 0
		else:
			if cb_var_arr[i].get() == 1:
				cb_arr[i-1].config(state="disabled")
				textfield.config(state="normal", bg = "#ffffff")
			else:
				cb_arr[i-1].config(state="normal")
				textfield.config(state="disabled", bg = "#e8e8e8")
			self.listvar[index] = 1

	def add_details(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT log_id FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (hr, bp, rr, temp, height, bmi, ibw, hip_circ, waist_circ, head_circ, abw, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			val = (self.hr.get("1.0",'end-1c'),self.bp.get("1.0",'end-1c'), self.rr.get("1.0",'end-1c'), self.temp.get("1.0",'end-1c'), self.height.get("1.0",'end-1c'), self.bmi.get("1.0",'end-1c'), self.ibw.get("1.0",'end-1c'), self.hipcirc.get("1.0",'end-1c'), self.waistcirc.get("1.0",'end-1c'), self.headcirc.get("1.0",'end-1c'), self.abw.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET hr = %s, bp = %s, rr = %s, temp = %s, height = %s, bmi = %s, ibw = %s, hip_circ = %s, waist_circ = %s, head_circ = %s, abw = %s WHERE patient_id = %s"
			val = (self.hr.get("1.0",'end-1c'),self.bp.get("1.0",'end-1c'), self.rr.get("1.0",'end-1c'), self.temp.get("1.0",'end-1c'), self.height.get("1.0",'end-1c'), self.bmi.get("1.0",'end-1c'), self.ibw.get("1.0",'end-1c'), self.hipcirc.get("1.0",'end-1c'), self.waistcirc.get("1.0",'end-1c'), self.headcirc.get("1.0",'end-1c'), self.abw.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		cur.execute(("SELECT ge_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (ge_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[0], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET ge_1 = %s WHERE patient_id = %s"
			val = (self.listvar[0], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.ge_var[1].get() == 1:
			cur.execute(("SELECT ge_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (ge_others, patient_id) VALUES (%s, %s)"), (self.ge_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET ge_others = %s WHERE patient_id = %s"), (self.ge_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT ge_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (ge_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET ge_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT skin_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (skin_1 patient_id) VALUES (%s, %s)"
			val = (self.listvar[1], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET skin_1 = %s WHERE patient_id = %s"
			val = (self.listvar[1], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.sk_var[1].get() == 1:
			cur.execute(("SELECT skin_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (skin_others, patient_id) VALUES (%s, %s)"), (self.sk_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET skin_others = %s WHERE patient_id = %s"), (self.sk_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT skin_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (skin_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET skin_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT musculo_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (musculo_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[2], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET musculo_1 = %s WHERE patient_id = %s"
			val = (self.listvar[2], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.mu_var[1].get() == 1:
			cur.execute(("SELECT musculo_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (musculo_others, patient_id) VALUES (%s, %s)"), (self.mu_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET musculo_others = %s WHERE patient_id = %s"), (self.mu_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT musculo_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (musculo_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET musculo_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT heent_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (heent_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[3], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET heent_1 = %s WHERE patient_id = %s"
			val = (self.listvar[3], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.he_var[1].get() == 1:
			cur.execute(("SELECT heent_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (heent_others, patient_id) VALUES (%s, %s)"), (self.he_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET heent_others = %s WHERE patient_id = %s"), (self.he_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT heent_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (heent_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET heent_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT respi_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (respi_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[4], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET respi_1 = %s WHERE patient_id = %s"
			val = (self.listvar[4], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.re_var[1].get() == 1:
			cur.execute(("SELECT respi_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (respi_others, patient_id) VALUES (%s, %s)"), (self.re_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET respi_others = %s WHERE patient_id = %s"), (self.re_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT respi_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (respi_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET respi_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT cardio_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (cardio_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[5], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET cardio_1 = %s WHERE patient_id = %s"
			val = (self.listvar[5], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.ca_var[1].get() == 1:
			cur.execute(("SELECT cardio_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (cardio_others, patient_id) VALUES (%s, %s)"), (self.ca_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET cardio_others = %s WHERE patient_id = %s"), (self.ca_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT cardio_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (cardio_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET cardio_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT gastro_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (gastro_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[6], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET gastro_1 = %s WHERE patient_id = %s"
			val = (self.listvar[6], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.ga_var[1].get() == 1:
			cur.execute(("SELECT gastro_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (gastro_others, patient_id) VALUES (%s, %s)"), (self.ga_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET gastro_others = %s WHERE patient_id = %s"), (self.ga_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT gastro_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (gastro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET gastro_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT genito_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (genito_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[7], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET genito_1 = %s WHERE patient_id = %s"
			val = (self.listvar[7], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.gn_var[1].get() == 1:
			cur.execute(("SELECT genito_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (genito_others, patient_id) VALUES (%s, %s)"), (self.gn_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET genito_others = %s WHERE patient_id = %s"), (self.gn_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT genito_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (genito_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET genito_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT ie_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (ie_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[8], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET ie_1 = %s WHERE patient_id = %s"
			val = (self.listvar[8], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.ie_var[1].get() == 1:
			cur.execute(("SELECT ie_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (ie_others, patient_id) VALUES (%s, %s)"), (self.ie_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET ie_others = %s WHERE patient_id = %s"), (self.ie_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT ie_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (ie_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET ie_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT dre_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (dre_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[9], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET dre_1 = %s WHERE patient_id = %s"
			val = (self.listvar[9], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.dre_var[1].get() == 1:
			cur.execute(("SELECT dre_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (dre_others, patient_id) VALUES (%s, %s)"), (self.dre_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET dre_others = %s WHERE patient_id = %s"), (self.dre_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT dre_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (dre_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET dre_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		cur.execute(("SELECT neuro_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (neuro_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[10], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET neuro_1 = %s WHERE patient_id = %s"
			val = (self.listvar[10], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.ne_var[1].get() == 1:
			cur.execute(("SELECT neuro_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (neuro_others, patient_id) VALUES (%s, %s)"), (self.ne_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET neuro_others = %s WHERE patient_id = %s"), (self.ne_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT neuro_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (neuro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET neuro_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()


		self.ge_find.delete('1.0', 'end') 
		self.sk_find.delete('1.0', 'end') 
		self.mu_find.delete('1.0', 'end') 
		self.he_find.delete('1.0', 'end') 
		self.re_find.delete('1.0', 'end') 
		self.ca_find.delete('1.0', 'end') 
		self.ga_find.delete('1.0', 'end') 
		self.gn_find.delete('1.0', 'end') 
		self.ie_find.delete('1.0', 'end') 
		self.dre_find.delete('1.0', 'end') 
		self.ne_find.delete('1.0', 'end') 

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.hr.delete('1.0', 'end')
		self.bp.delete('1.0', 'end')
		self.rr.delete('1.0', 'end')
		self.temp.delete('1.0', 'end')
		self.height.delete('1.0', 'end')
		self.bmi.delete('1.0', 'end')
		self.ibw.delete('1.0', 'end')
		self.hipcirc.delete('1.0', 'end')
		self.waistcirc.delete('1.0', 'end')
		self.headcirc.delete('1.0', 'end')
		self.abw.delete('1.0', 'end')
		
		cur.execute(("SELECT hr, bp, rr, temp, height, bmi, ibw, hip_circ, waist_circ, head_circ, abw FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is not None:
			if res[0] is not None:
				self.hr.insert('1.0', res[0])
			if res[1] is not None:
				self.bp.insert('1.0', res[1])
			if res[2] is not None:
				self.rr.insert('1.0', res[2])
			if res[3] is not None:
				self.temp.insert('1.0', res[3])
			if res[4] is not None:
				self.height.insert('1.0', res[4])
			if res[5] is not None:
				self.bmi.insert('1.0', res[5])
			if res[6] is not None:
				self.ibw.insert('1.0', res[6])
			if res[7] is not None:
				self.hipcirc.insert('1.0', res[7])
			if res[8] is not None:
				self.waistcirc.insert('1.0', res[8])
			if res[9] is not None:
				self.headcirc.insert('1.0', res[9])
			if res[10] is not None:
				self.abw.insert('1.0', res[10])

			self.hr.config(state="disabled", bg = "#e8e8e8")
			self.bp.config(state="disabled", bg = "#e8e8e8")
			self.rr.config(state="disabled", bg = "#e8e8e8")
			self.temp.config(state="disabled", bg = "#e8e8e8")
			self.height.config(state="disabled", bg = "#e8e8e8")
			self.bmi.config(state="disabled", bg = "#e8e8e8")
			self.ibw.config(state="disabled", bg = "#e8e8e8")
			self.hipcirc.config(state="disabled", bg = "#e8e8e8")
			self.waistcirc.config(state="disabled", bg = "#e8e8e8")
			self.headcirc.config(state="disabled", bg = "#e8e8e8")
			self.abw.config(state="disabled", bg = "#e8e8e8")
		else:
			self.hr.delete('1.0', 'end')
			self.bp.delete('1.0', 'end')
			self.rr.delete('1.0', 'end')
			self.temp.delete('1.0', 'end')
			self.height.delete('1.0', 'end')
			self.bmi.delete('1.0', 'end')
			self.ibw.delete('1.0', 'end')
			self.hipcirc.delete('1.0', 'end')
			self.waistcirc.delete('1.0', 'end')
			self.headcirc.delete('1.0', 'end')
			self.abw.delete('1.0', 'end')

			self.hr.config(state="normal", bg = "#ffffff")
			self.bp.config(state="normal", bg = "#ffffff")
			self.rr.config(state="normal", bg = "#ffffff")
			self.temp.config(state="normal", bg = "#ffffff")
			self.height.config(state="normal", bg = "#ffffff")
			self.bmi.config(state="normal", bg = "#ffffff")
			self.ibw.config(state="normal", bg = "#ffffff")
			self.hipcirc.config(state="normal", bg = "#ffffff")
			self.waistcirc.config(state="normal", bg = "#ffffff")
			self.headcirc.config(state="normal", bg = "#ffffff")
			self.abw.config(state="normal", bg = "#ffffff")

		cur.execute(("SELECT ge_1, skin_1, musculo_1, heent_1, respi_1, cardio_1, gastro_1, genito_1, ie_1, dre_1, neuro_1 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] == 0:
				self.ge_var[0].set(1)
				self.ge_var[1].set(0)
			elif res[0] == 1:
				self.ge_var[0].set(0)
				self.ge_var[1].set(1)
			else:
				self.ge_var[0].set(0)
				self.ge_var[1].set(0)

			if res[1] == 0:
				self.sk_var[0].set(1)
				self.sk_var[1].set(0)
			elif res[1] == 1:
				self.sk_var[0].set(0)
				self.sk_var[1].set(1)
			else:
				self.sk_var[0].set(0)
				self.sk_var[1].set(0)

			if res[2] == 0:
				self.mu_var[0].set(1)
				self.mu_var[1].set(0)
			elif res[2] == 1:
				self.mu_var[0].set(0)
				self.mu_var[1].set(1)
			else:
				self.mu_var[0].set(0)
				self.mu_var[1].set(0)

			if res[3] == 0:
				self.he_var[0].set(1)
				self.he_var[1].set(0)
			elif res[3] == 1:
				self.he_var[0].set(0)
				self.he_var[1].set(1)
			else:
				self.he_var[0].set(0)
				self.he_var[1].set(0)

			if res[4] == 0:
				self.re_var[0].set(1)
				self.re_var[1].set(0)
			elif res[4] == 1:
				self.re_var[0].set(0)
				self.re_var[1].set(1)
			else:
				self.re_var[0].set(0)
				self.re_var[1].set(0)

			if res[5] == 0:
				self.ca_var[0].set(1)
				self.ca_var[1].set(0)
			elif res[5] == 1:
				self.ca_var[0].set(0)
				self.ca_var[1].set(1)
			else:
				self.ca_var[0].set(0)
				self.ca_var[1].set(0)

			if res[6] == 0:
				self.ga_var[0].set(1)
				self.ga_var[1].set(0)
			elif res[6] == 1:
				self.ga_var[0].set(0)
				self.ga_var[1].set(1)
			else:
				self.ga_var[0].set(0)
				self.ga_var[1].set(0)

			if res[7] == 0:
				self.gn_var[0].set(1)
				self.gn_var[1].set(0)
			elif res[7] == 1:
				self.gn_var[0].set(0)
				self.gn_var[1].set(1)
			else:
				self.gn_var[0].set(0)
				self.gn_var[1].set(0)

			if res[8] == 0:
				self.ie_var[0].set(1)
				self.ie_var[1].set(0)
			elif res[8] == 1:
				self.ie_var[0].set(0)
				self.ie_var[1].set(1)
			else:
				self.ie_var[0].set(0)
				self.ie_var[1].set(0)

			if res[9] == 0:
				self.dre_var[0].set(1)
				self.dre_var[1].set(0)
			elif res[9] == 1:
				self.dre_var[0].set(0)
				self.dre_var[1].set(1)
			else:
				self.dre_var[0].set(0)
				self.dre_var[1].set(0)

			if res[10] == 0:
				self.ne_var[0].set(1)
				self.ne_var[1].set(0)
			elif res[10] == 1:
				self.ne_var[0].set(0)
				self.ne_var[1].set(1)
			else:
				self.ne_var[0].set(0)
				self.ne_var[1].set(0)

		else:
			for i in range(2):
				self.ge_var[i].set(0)
				self.sk_var[i].set(0)
				self.mu_var[i].set(0)
				self.he_var[i].set(0)
				self.re_var[i].set(0)
				self.ca_var[i].set(0)
				self.ga_var[i].set(0)
				self.gn_var[i].set(0)
				self.ie_var[i].set(0)
				self.dre_var[i].set(0)
				self.ne_var[i].set(0)

			for i in range(11):
				self.listvar[i] = 0

		self.ge_find.delete('1.0', 'end') 
		self.sk_find.delete('1.0', 'end') 
		self.mu_find.delete('1.0', 'end') 
		self.he_find.delete('1.0', 'end') 
		self.re_find.delete('1.0', 'end') 
		self.ca_find.delete('1.0', 'end') 
		self.ga_find.delete('1.0', 'end') 
		self.gn_find.delete('1.0', 'end') 
		self.ie_find.delete('1.0', 'end') 
		self.dre_find.delete('1.0', 'end') 
		self.ne_find.delete('1.0', 'end') 

		cur.execute(("SELECT ge_others, skin_others, musculo_others, heent_others, respi_others, cardio_others, gastro_others, genito_others, ie_others, dre_others, neuro_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				self.ge_find.insert('1.0', res[0])
			if res[1] is not None:
				self.sk_find.insert('1.0', res[1])
			if res[2] is not None:
				self.mu_find.insert('1.0', res[2])
			if res[3] is not None:
				self.he_find.insert('1.0', res[3])
			if res[4] is not None:
				self.re_find.insert('1.0', res[4])
			if res[5] is not None:
				self.ca_find.insert('1.0', res[5])
			if res[6] is not None:
				self.ga_find.insert('1.0', res[6])
			if res[7] is not None:
				self.gn_find.insert('1.0', res[7])
			if res[8] is not None:
				self.ie_find.insert('1.0', res[8])
			if res[9] is not None:
				self.dre_find.insert('1.0', res[9])
			if res[10] is not None:
				self.ne_find.insert('1.0', res[10])

			self.ge_find.config(state = "disabled", bg = "#e8e8e8")
			self.sk_find.config(state = "disabled", bg = "#e8e8e8")
			self.mu_find.config(state = "disabled", bg = "#e8e8e8")
			self.he_find.config(state = "disabled", bg = "#e8e8e8")
			self.re_find.config(state = "disabled", bg = "#e8e8e8")
			self.ca_find.config(state = "disabled", bg = "#e8e8e8")
			self.ga_find.config(state = "disabled", bg = "#e8e8e8")
			self.gn_find.config(state = "disabled", bg = "#e8e8e8")
			self.ie_find.config(state = "disabled", bg = "#e8e8e8")
			self.dre_find.config(state = "disabled", bg = "#e8e8e8")
			self.ne_find.config(state = "disabled", bg = "#e8e8e8")
			for i in range(2):
				self.ge_cb[i].config(state = "disabled")
				self.sk_cb[i].config(state = "disabled")
				self.mu_cb[i].config(state = "disabled")
				self.he_cb[i].config(state = "disabled")
				self.re_cb[i].config(state = "disabled")
				self.ca_cb[i].config(state = "disabled")
				self.ga_cb[i].config(state = "disabled")
				self.gn_cb[i].config(state = "disabled")
				self.ie_cb[i].config(state = "disabled")
				self.dre_cb[i].config(state = "disabled")
				self.ne_cb[i].config(state = "disabled")
		else:
			self.ge_find.delete('1.0', 'end') 
			self.sk_find.delete('1.0', 'end') 
			self.mu_find.delete('1.0', 'end') 
			self.he_find.delete('1.0', 'end') 
			self.re_find.delete('1.0', 'end') 
			self.ca_find.delete('1.0', 'end') 
			self.ga_find.delete('1.0', 'end') 
			self.gn_find.delete('1.0', 'end') 
			self.ie_find.delete('1.0', 'end') 
			self.dre_find.delete('1.0', 'end') 
			self.ne_find.delete('1.0', 'end') 

			self.ge_find.config(state = "normal", bg = "#ffffff")
			self.sk_find.config(state = "normal", bg = "#ffffff")
			self.mu_find.config(state = "normal", bg = "#ffffff")
			self.he_find.config(state = "normal", bg = "#ffffff")
			self.re_find.config(state = "normal", bg = "#ffffff")
			self.ca_find.config(state = "normal", bg = "#ffffff")
			self.ga_find.config(state = "normal", bg = "#ffffff")
			self.gn_find.config(state = "normal", bg = "#ffffff")
			self.ie_find.config(state = "normal", bg = "#ffffff")
			self.dre_find.config(state = "normal", bg = "#ffffff")
			self.ne_find.config(state = "normal", bg = "#ffffff")

			for i in range(2):
				self.ge_cb[i].config(state = "normal")
				self.sk_cb[i].config(state = "normal")
				self.mu_cb[i].config(state = "normal")
				self.he_cb[i].config(state = "normal")
				self.re_cb[i].config(state = "normal")
				self.ca_cb[i].config(state = "normal")
				self.ga_cb[i].config(state = "normal")
				self.gn_cb[i].config(state = "normal")
				self.ie_cb[i].config(state = "normal")
				self.dre_cb[i].config(state = "normal")
				self.ne_cb[i].config(state = "normal")

class assessment_table(tk.Frame): # Form containing the remaining parts of the First Consultation Record

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_1(self, self.controller, 2)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		assess_label = tk.Label(form_frame, text="Assessment", font=self.label_font, fg="#636363")
		assess_label.place(x=65, y=25)
		self.assess = tk.Text(form_frame, height = 4, width = 34, wrap="word")
		self.assess.place(x=25, y=50)

		icd_code_label = tk.Label(form_frame, text="ICD Code", font=self.label_font, fg="#636363")
		icd_code_label.place(x=343, y=25)
		self.icd_code = tk.Text(form_frame, height = 4, width = 34, wrap="word")
		self.icd_code.place(x=303, y=50)

		dpra_label = tk.Label(form_frame, text="Diagnostic/Prognostic Risk Assessments", font=self.label_font, fg="#636363")
		dpra_label.place(x=622, y=25)
		self.dpra = tk.Text(form_frame, height = 4, width = 34, wrap="word")
		self.dpra.place(x=582, y=50)

		tk.Button(form_frame, text="Add to List", command=lambda: self.add_to_table(self.assess.get("1.0",'end-1c'), self.icd_code.get("1.0",'end-1c'), self.dpra.get("1.0",'end-1c')), height = 2, width = 18, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=370, y=130)

		self.tree = ttk.Treeview(form_frame, height = 20)
		self.tree.heading("#0", text="List of Assessments")
		self.tree.column("#0", minwidth=200, width=300, stretch="no") 
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=25, y=190)

		therapeutic_label = tk.Label(form_frame, text="Therapeutic Intervention", font=self.label_font_2)
		therapeutic_label.place(x=375, y=190)

		drugs_label = tk.Label(form_frame, text="Drugs:", font=self.label_font, fg="#636363")
		drugs_label.place(x=375, y=215)
		self.drugs = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.drugs.place(x=375, y=240)

		diet_label = tk.Label(form_frame, text="Dietary advice:", font=self.label_font, fg="#636363")
		diet_label.place(x=375, y=280)
		self.diet = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.diet.place(x=375, y=305)

		lifestyle_label = tk.Label(form_frame, text="Lifestyle change:", font=self.label_font, fg="#636363")
		lifestyle_label.place(x=375, y=355)
		self.lifestyle = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.lifestyle.place(x=375, y=380)

		exer_label = tk.Label(form_frame, text="Exercises (type/duration)", font=self.label_font, fg="#636363")
		exer_label.place(x=375, y=430)
		self.exer = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.exer.place(x=375, y=455)

		referral_label = tk.Label(form_frame, text="Referral:", font=self.label_font)
		referral_label.place(x=375, y=505)
		self.referral = tk.Text(form_frame, height = 1, width = 29, wrap="word")
		self.referral.place(x=425, y=505)

		follow_up_label = tk.Label(form_frame, text="Follow-up:", font=self.label_font)
		follow_up_label.place(x=375, y=535)
		self.follow_up = tk.Text(form_frame, height = 1, width = 28, wrap="word")
		self.follow_up.place(x=435, y=535)

		self.strat_var = []

		healthstrat_label = tk.Label(form_frame, text="Health Education/Strategy:", font=self.label_font_2, fg="#636363")
		healthstrat_label.place(x=675, y=190)

		self.strat_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Advice", variable=self.strat_var[0])
		cb.place(x=695, y=205)

		self.strat_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Flyers/pamphlets", variable=self.strat_var[1])
		cb.place(x=695, y=225)

		self.strat_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="Others:", variable=self.strat_var[2])
		cb.place(x=695, y=245)

		self.health_strat_others = tk.Text(form_frame, height = 1, width = 23, wrap="word")
		self.health_strat_others.place(x=765, y=250)

		drugs_label = tk.Label(form_frame, text="Family Assessment/ Interventions (as needed):", font=self.label_font, fg="#636363")
		drugs_label.place(x=675, y=280)
		self.drugs = tk.Text(form_frame, height = 4, width = 35, wrap="word")
		self.drugs.place(x=675, y=305)

		tk.Button(form_frame, text="Add Assessment/Intervention", command=lambda: self.add_assessment(), height = 3, width = 20, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007", wraplength = 150).place(x=750, y=420)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("physical_examination_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def add_assessment(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.controller.get_page("physical_examination_form").add_details()

		cur.execute(("SELECT log_id FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (ti_drugs, ti_diet, ti_lifestyle, ti_exer, ti_ref, ti_follow, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			val = (self.drugs.get("1.0",'end-1c'), self.diet.get("1.0",'end-1c'), self.lifestyle.get("1.0",'end-1c'), self.exer.get("1.0",'end-1c'), self.referral.get("1.0",'end-1c'), self.follow_up.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET ti_drugs = %s, ti_diet = %s, ti_lifestyle = %s, ti_exer = %s, ti_ref = %s, ti_follow = %s WHERE patient_id = %s"
			val = (self.drugs.get("1.0",'end-1c'), self.diet.get("1.0",'end-1c'), self.lifestyle.get("1.0",'end-1c'), self.exer.get("1.0",'end-1c'), self.referral.get("1.0",'end-1c'), self.follow_up.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		self.drugs.delete('1.0', 'end') 
		self.diet.delete('1.0', 'end') 
		self.lifestyle.delete('1.0', 'end') 
		self.exer.delete('1.0', 'end') 
		self.referral.delete('1.0', 'end') 
		self.follow_up.delete('1.0', 'end') 

		cur.execute(("SELECT log_id FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientassessment (strat_1, strat_2, strat_3, patient_id) VALUES (%s, %s, %s)"
			val = (self.strat_var[0].get(), self.strat_var[1].get(), self.strat_var[2].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientassessment SET strat_1 = %s, strat_2 = %s, strat_3 = %s WHERE patient_id = %s"
			val = (self.strat_var[0].get(), self.strat_var[1].get(), self.strat_var[2].get(), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()

		if self.strat_var[2].get() == 1:
			cur.execute(("SELECT strat_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (strat_others, patient_id) VALUES (%s, %s)"), (self.health_strat_others.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET strat_others = %s WHERE patient_id = %s"), (self.health_strat_others.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
		else:
			cur.execute(("SELECT strat_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientassessment (strat_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientassessment SET strat_others = %s WHERE patient_id = %s"), (" ", self.controller.patient_id.get()))
				mydb.commit()

		self.health_strat_others.delete('1.0', 'end')

		self.controller.show_frame("physical_examination_form")

	def add_to_table(self, assessment, icd, dpra):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		sql = "INSERT INTO patientassessmenttree (assessment, icd_code, dpra, patient_id) VALUES (%s, %s, %s, %s)"
		val = (assessment, icd, dpra, self.controller.patient_id.get())
		cur.execute(sql, val)
		mydb.commit()

		id = self.tree.insert('', 'end', text="Assessment: " + assessment)
		sub_id_1 = self.tree.insert(id, 'end', text="ICD Code")
		self.tree.insert(sub_id_1, 'end', text=icd)
		sub_id_2 = self.tree.insert(id, 'end', text="Diagnostic/Prognostic Risk Assessments")
		self.tree.insert(sub_id_2, 'end', text=dpra)

		self.assess.delete('1.0', 'end')
		self.icd_code.delete('1.0', 'end')
		self.dpra.delete('1.0', 'end')

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.assess.delete('1.0', 'end')
		self.icd_code.delete('1.0', 'end')
		self.dpra.delete('1.0', 'end')
		self.drugs.delete('1.0', 'end')
		self.diet.delete('1.0', 'end')
		self.lifestyle.delete('1.0', 'end')
		self.exer.delete('1.0', 'end')
		self.referral.delete('1.0', 'end')
		self.follow_up.delete('1.0', 'end')

		cur.execute(("SELECT ti_drugs, ti_diet, ti_lifestyle, ti_exer, ti_ref, ti_follow FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				self.drugs.insert('1.0', res[0])
			if res[1] is not None:
				self.diet.insert('1.0', res[1])
			if res[2] is not None:
				self.lifestyle.insert('1.0', res[2])
			if res[3] is not None:
				self.exer.insert('1.0', res[3])
			if res[4] is not None:
				self.referral.insert('1.0', res[4])
			if res[5] is not None:
				self.follow_up.insert('1.0', res[5])
			self.drugs.config(state="disabled", bg = "#e8e8e8")
			self.diet.config(state="disabled", bg = "#e8e8e8")
			self.lifestyle.config(state="disabled", bg = "#e8e8e8")
			self.exer.config(state="disabled", bg = "#e8e8e8")
			self.referral.config(state="disabled", bg = "#e8e8e8")
			self.follow_up.config(state="disabled", bg = "#e8e8e8")
		else:
			self.drugs.delete('1.0', 'end')
			self.diet.delete('1.0', 'end')
			self.lifestyle.delete('1.0', 'end')
			self.exer.delete('1.0', 'end')
			self.referral.delete('1.0', 'end')
			self.follow_up.delete('1.0', 'end')
			self.drugs.config(state="normal", bg = "#ffffff")
			self.diet.config(state="normal", bg = "#ffffff")
			self.lifestyle.config(state="normal", bg = "#ffffff")
			self.exer.config(state="normal", bg = "#ffffff")
			self.referral.config(state="normal", bg = "#ffffff")
			self.follow_up.config(state="normal", bg = "#ffffff")

		cur.execute(("SELECT assessment, icd_code, dpra FROM patientassessmenttree WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree.delete(*self.tree.get_children())

		for i in range(len(res)):
			id = self.tree.insert('', 'end', text="Assessment: " + str(res[i][0]))
			sub_id_1 = self.tree.insert(id, 'end', text="ICD Code")
			self.tree.insert(sub_id_1, 'end', text=res[i][1])
			sub_id_2 = self.tree.insert(id, 'end', text="Diagnostic/Prognostic Risk Assessments")
			self.tree.insert(sub_id_2, 'end', text=res[i][2])

		cur.execute(("SELECT strat_1, strat_2, strat_3 FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(3):
				if res[i] is not None:
					self.strat_var[i].set(res[i])
		else:
			for i in range(3):
				self.strat_var[i].set(0)

		self.health_strat_others.delete('1.0', 'end')

		cur.execute(("SELECT strat_others FROM patientassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.health_strat_others.insert('1.0', res[0])
		else:
			self.health_strat_others.delete('1.0', 'end')
