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

def submenu_buttons_3(self, controller, num):
	side_menu_frame = tk.Frame(self, height = 720, width = 200)
	side_menu_frame.pack(side="left")

	b1 = tk.Button(side_menu_frame, text="Follow-up Patient Record", command=lambda: controller.show_frame("followup_patient_form"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b1.place(x=25, y=160)
	b2 = tk.Button(side_menu_frame, text="Patient's Records", command=lambda: controller.show_frame("followup_patient_form_res"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b2.place(x=25, y=220)
	b3 = tk.Button(side_menu_frame, text="Referral Form and Clinical Summary", command=lambda: controller.show_frame("ReferralForm"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b3.place(x=25, y=280)

	if(num == 1):
		b1.config(bg = "#2553a8")
	elif(num == 2):
		b2.config(bg = "#2553a8")
	else:
		b3.config(bg = "#2553a8")

class followup_patient_form(tk.Frame): # Form containing the additional form for follow-up record of patient up to present medication

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 5)
		submenu_buttons_3(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.label_font_3 = tkfont.Font(family='Helvetica', size = 8)

		page_title = tk.Label(form_frame, text="Follow-up Patient Record", font=self.title_font)
		page_title.place(x=375, y=15)

		p_name_label = tk.Label(form_frame, text="Name:", font=self.label_font_2)
		p_name_label.place(x=90, y=50)

		self.p_name = tk.Label(form_frame, text="")
		self.p_name.place(x=140, y=50)

		p_gender_label = tk.Label(form_frame, text="Gender:", font=self.label_font_2)
		p_gender_label.place(x=590, y=50)

		self.p_gender = tk.Label(form_frame, text="")
		self.p_gender.place(x=640, y=50)

		f_date_label = tk.Label(form_frame, text="Date of Follow-up: ", font=self.label_font_2)
		f_date_label.place(x=90, y=80)

		self.f_date_input = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd")
		self.f_date_input.place(x=200, y=80)

		f_reasons_label = tk.Label(form_frame, text="Reasons for Follow-up: ", font=self.label_font_2)
		f_reasons_label.place(x=90, y=110)

		self.reason = 0
		self.r_var = []
		self.r_cb_arr = []
		self.r_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="continuing care from previous visit", variable=self.r_var[0])
		cb.place(x=230, y=110)
		self.r_cb_arr.append(cb)

		self.r_var.append(tk.IntVar(self))
		cb = tk.Checkbutton(form_frame, text="new complaint", variable=self.r_var[1])
		cb.place(x=230, y=130)
		self.r_cb_arr.append(cb)

		self.r_cb_arr[0].config(command=partial(self.check_cb, self.r_cb_arr, self.r_var, 0))
		self.r_cb_arr[1].config(command=partial(self.check_cb, self.r_cb_arr, self.r_var, 1))

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=160)

		f_s_label = tk.Label(form_frame, text="S:", font=self.label_font_2)
		f_s_label.place(x=90, y=180)

		self.f_s = tk.Text(form_frame, height = 8, width = 102, wrap="word")
		self.f_s.place(x=90, y=200)

		f_medication_label = tk.Label(form_frame, text="Present Medications:", font=self.label_font_2)
		f_medication_label.place(x=90, y=350)

		self.f_medication = tk.Text(form_frame, height = 4, width = 102, wrap="word")
		self.f_medication.place(x=90, y=370)

		tk.Label(form_frame, text="*include symptom progression or improvement and medications on board and lab results for chronic illness", font=self.label_font, fg="#636363").place(x=110, y=450)
		tk.Label(form_frame, text="**put symptoms and interventions done for new complaints", font=self.label_font, fg="#636363").place(x=110, y=480)

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=500)

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("followup_patient_form_2"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def check_cb(self, cb_arr, cb_var_arr, i):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				cb_arr[i+1].config(state="disabled")
				self.reason = 0
			else:
				cb_arr[i+1].config(state="normal")
				self.reason = 2
		else:
			if cb_var_arr[i].get() == 1:
				cb_arr[i-1].config(state="disabled")
				self.reason = 1
			else:
				cb_arr[i-1].config(state="normal")
				self.reason = 2

	def add_details(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT followup_date FROM patientfollowup WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			cur.execute(("INSERT INTO patientfollowup (followup_date, reason, followup_s, followup_med, patient_id) VALUES (%s, %s, %s, %s, %s)"), (self.f_date_input.get_date().strftime('%Y-%m-%d'), self.reason, self.f_s.get("1.0",'end-1c'), self.f_medication.get("1.0",'end-1c'), self.controller.patient_id.get()))
			mydb.commit()
		else:
			cur.execute(("UPDATE patientfollowup SET followup_date = %s, reason = %s, followup_s = %s, followup_med = %s WHERE patient_id = %s"), (self.f_date_input.get_date().strftime('%Y-%m-%d'), self.reason, self.f_s.get("1.0",'end-1c'), self.f_medication.get("1.0",'end-1c'), self.controller.patient_id.get()))
			mydb.commit()

		self.f_s.delete('1.0', 'end')
		self.f_medication.delete('1.0', 'end')

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT last_name, first_name, middle_name, gender FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.p_name['text'] = res[0] + ", " + res[1] + " " + res[2]
			self.p_gender['text'] = res[3]
		else:
			self.p_name['text'] = ""
			self.p_gender['text'] = ""

		self.f_date_input.set_date(dt.datetime.today())
		for i in range(2):
			self.r_var[i].set(0)
			self.r_cb_arr[i].config(state="normal")
		self.reason = 2
		self.f_s.delete('1.0', 'end')
		self.f_medication.delete('1.0', 'end')

class followup_patient_form_2(tk.Frame): # Form containing the additional form for follow-up record of patient before the assessment table

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 5)
		submenu_buttons_3(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		y_value = 25

		self.followup_date = self.controller.get_page("followup_patient_form").f_date_input.get_date().strftime('%Y-%m-%d')

		pe_label = tk.Label(form_frame, text="O:", font=self.label_font_2, fg="#636363")
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

		weight_label = tk.Label(form_frame, text="Weight:", font=self.label_font, fg="#636363")
		weight_label.place(x=490, y=y_value)

		self.weight = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.weight.place(x=530, y=y_value)

		y_value = y_value + 30
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

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("followup_assessment_table"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=65)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("followup_patient_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

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
		
		self.controller.get_page("followup_patient_form").add_details()

		cur.execute(("SELECT followup_date FROM patientfollowup WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (followup_date, hr, bp, rr, temp, weight, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			val = (self.followup_date, self.hr.get("1.0",'end-1c'),self.bp.get("1.0",'end-1c'), self.rr.get("1.0",'end-1c'), self.temp.get("1.0",'end-1c'), self.weight.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET hr = %s, bp = %s, rr = %s, temp = %s, weight = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.hr.get("1.0",'end-1c'),self.bp.get("1.0",'end-1c'), self.rr.get("1.0",'end-1c'), self.temp.get("1.0",'end-1c'), self.weight.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		cur.execute(("SELECT ge_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (ge_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[0], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET ge_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[0], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.ge_var[1].get() == 1:
			cur.execute(("SELECT ge_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (ge_others, patient_id) VALUES (%s, %s)"), (self.ge_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET ge_others = %s WHERE patient_id = %s and followup_date = %s"), (self.ge_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT ge_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (ge_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET ge_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT skin_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (skin_1 patient_id) VALUES (%s, %s)"
			val = (self.listvar[1], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET skin_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[1], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.sk_var[1].get() == 1:
			cur.execute(("SELECT skin_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (skin_others, patient_id) VALUES (%s, %s)"), (self.sk_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET skin_others = %s WHERE patient_id = %s and followup_date = %s"), (self.sk_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT skin_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (skin_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET skin_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT musculo_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (musculo_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[2], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET musculo_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[2], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.mu_var[1].get() == 1:
			cur.execute(("SELECT musculo_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(),))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (musculo_others, patient_id) VALUES (%s, %s)"), (self.mu_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET musculo_others = %s WHERE patient_id = %s and followup_date = %s"), (self.mu_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT musculo_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (musculo_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET musculo_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT heent_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (heent_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[3], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET heent_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[3], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.he_var[1].get() == 1:
			cur.execute(("SELECT heent_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (heent_others, patient_id) VALUES (%s, %s)"), (self.he_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET heent_others = %s WHERE patient_id = %s and followup_date = %s"), (self.he_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT heent_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (heent_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET heent_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT respi_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (respi_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[4], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET respi_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[4], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.re_var[1].get() == 1:
			cur.execute(("SELECT respi_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (respi_others, patient_id) VALUES (%s, %s)"), (self.re_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET respi_others = %s WHERE patient_id = %s and followup_date = %s"), (self.re_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT respi_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (respi_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET respi_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT cardio_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (cardio_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[5], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET cardio_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[5], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.ca_var[1].get() == 1:
			cur.execute(("SELECT cardio_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (cardio_others, patient_id) VALUES (%s, %s)"), (self.ca_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET cardio_others = %s WHERE patient_id = %s and followup_date = %s"), (self.ca_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT cardio_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (cardio_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET cardio_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT gastro_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (gastro_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[6], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET gastro_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[6], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.ga_var[1].get() == 1:
			cur.execute(("SELECT gastro_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (gastro_others, patient_id) VALUES (%s, %s)"), (self.ga_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET gastro_others = %s WHERE patient_id = %s and followup_date = %s"), (self.ga_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT gastro_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (gastro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET gastro_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT genito_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (genito_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[7], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET genito_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[7], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.gn_var[1].get() == 1:
			cur.execute(("SELECT genito_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (genito_others, patient_id) VALUES (%s, %s)"), (self.gn_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET genito_others = %s WHERE patient_id = %s and followup_date = %s"), (self.gn_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT genito_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (genito_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET genito_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT ie_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (ie_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[8], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET ie_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[8], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.ie_var[1].get() == 1:
			cur.execute(("SELECT ie_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (ie_others, patient_id) VALUES (%s, %s)"), (self.ie_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET ie_others = %s WHERE patient_id = %s and followup_date = %s"), (self.ie_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT ie_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (ie_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET ie_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT dre_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (dre_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[9], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET dre_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[9], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.dre_var[1].get() == 1:
			cur.execute(("SELECT dre_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (dre_others, patient_id) VALUES (%s, %s)"), (self.dre_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET dre_others = %s WHERE patient_id = %s and followup_date = %s"), (self.dre_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT dre_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (dre_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET dre_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
				mydb.commit()

		cur.execute(("SELECT neuro_1 FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (neuro_1, patient_id) VALUES (%s, %s)"
			val = (self.listvar[10], self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET neuro_1 = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.listvar[10], self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		if self.ne_var[1].get() == 1:
			cur.execute(("SELECT neuro_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (neuro_others, patient_id) VALUES (%s, %s)"), (self.ne_find.get("1.0",'end-1c'), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET neuro_others = %s WHERE patient_id = %s and followup_date = %s"), (self.ne_find.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date))
				mydb.commit()
		else:
			cur.execute(("SELECT neuro_others FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfollowup (neuro_others, patient_id) VALUES (%s, %s)"), (" ", self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfollowup SET neuro_others = %s WHERE patient_id = %s and followup_date = %s"), (" ", self.controller.patient_id.get(), self.followup_date))
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
		self.followup_date = self.controller.get_page("followup_patient_form").f_date_input.get_date().strftime('%Y-%m-%d')

		self.hr.delete('1.0', 'end')
		self.bp.delete('1.0', 'end')
		self.rr.delete('1.0', 'end')
		self.temp.delete('1.0', 'end')
		self.weight.delete('1.0', 'end')

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

class followup_patient_form_res(tk.Frame): # Form for viewing follow-up records only

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_3(self, self.controller, 2)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		self.tree = ttk.Treeview(form_frame, height = 16)
		self.tree.heading("#0", text="Follow-up Records")
		self.tree.column("#0", minwidth=150, width=850, stretch="no")
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=65, y=25)

		self.tree_2 = ttk.Treeview(form_frame, height = 9)
		self.tree_2.heading("#0", text="Assessment Records")
		self.tree_2.column("#0", minwidth=150, width=850, stretch="no")
		vsb_2 = ttk.Scrollbar(orient="vertical", command=self.tree_2.yview)
		self.tree_2.configure(yscrollcommand=vsb_2.set)
		self.tree_2.place(x=65, y=400)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT followup_date, reason, followup_s, followup_med, hr, bp, rr, temp, weight, ge_1, ge_others, skin_1, skin_others, musculo_1, musculo_others, heent_1, heent_others, respi_1, respi_others, cardio_1, cardio_others, gastro_1, gastro_others, genito_1, genito_others, ie_1, ie_others, dre_1, dre_others, neuro_1, neuro_others, ti_drugs, ti_diet, ti_lifestyle, ti_exer FROM patientfollowup WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree.delete(*self.tree.get_children())

		for i in range(len(res)):
			if res[i][0] is not None:
				id = self.tree.insert('', 'end', text=res[i][0])
				sub_id_1 = self.tree.insert(id, 'end', text="Reasons for follow-up")
				if res[i][1] == 0:
					self.tree.insert(sub_id_1, 'end', text="continuing care from previous visit")
				elif res[i][1] == 1:
					self.tree.insert(sub_id_1, 'end', text="new complaint")
				else:
					self.tree.insert(sub_id_1, 'end', text="")
				sub_id_2 = self.tree.insert(id, 'end', text="S")
				self.tree.insert(sub_id_2, 'end', text=res[i][2])
				sub_id_3 = self.tree.insert(id, 'end', text="Present Medications")
				self.tree.insert(sub_id_3, 'end', text=res[i][3])
				sub_id_4 = self.tree.insert(id, 'end', text="HR")
				self.tree.insert(sub_id_4, 'end', text=res[i][4])
				sub_id_5 = self.tree.insert(id, 'end', text="BP")
				self.tree.insert(sub_id_5, 'end', text=res[i][5])
				sub_id_6 = self.tree.insert(id, 'end', text="RR")
				self.tree.insert(sub_id_6, 'end', text=res[i][6])
				sub_id_7 = self.tree.insert(id, 'end', text="Temperature")
				self.tree.insert(sub_id_7, 'end', text=res[i][7])
				sub_id_8 = self.tree.insert(id, 'end', text="Weight")
				self.tree.insert(sub_id_8, 'end', text=res[i][8])

				sub_id_9 = self.tree.insert(id, 'end', text="General Survey")
				if res[i][9] == 0:
					self.tree.insert(sub_id_9, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_9, 'end', text=res[i][10])

				sub_id_10 = self.tree.insert(id, 'end', text="Skin/Integument")
				if res[i][11] == 0:
					self.tree.insert(sub_id_10, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_10, 'end', text=res[i][12])

				sub_id_11 = self.tree.insert(id, 'end', text="Musculoskeletal")
				if res[i][13] == 0:
					self.tree.insert(sub_id_11, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_11, 'end', text=res[i][14])

				sub_id_12 = self.tree.insert(id, 'end', text="HEENT")
				if res[i][15] == 0:
					self.tree.insert(sub_id_12, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_12, 'end', text=res[i][16])

				sub_id_13 = self.tree.insert(id, 'end', text="Respiratory")
				if res[i][17] == 0:
					self.tree.insert(sub_id_13, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_13, 'end', text=res[i][18])

				sub_id_14 = self.tree.insert(id, 'end', text="Cardiovascular")
				if res[i][19] == 0:
					self.tree.insert(sub_id_14, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_14, 'end', text=res[i][20])

				sub_id_15 = self.tree.insert(id, 'end', text="Gastrointestinal")
				if res[i][21] == 0:
					self.tree.insert(sub_id_15, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_15, 'end', text=res[i][22])

				sub_id_16 = self.tree.insert(id, 'end', text="Genitourinary")
				if res[i][23] == 0:
					self.tree.insert(sub_id_16, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_16, 'end', text=res[i][24])

				sub_id_17 = self.tree.insert(id, 'end', text="IE")
				if res[i][25] == 0:
					self.tree.insert(sub_id_17, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_17, 'end', text=res[i][26])

				sub_id_18 = self.tree.insert(id, 'end', text="DRE")
				if res[i][27] == 0:
					self.tree.insert(sub_id_18, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_18, 'end', text=res[i][28])

				sub_id_19 = self.tree.insert(id, 'end', text="Neurolopsych")
				if res[i][29] == 0:
					self.tree.insert(sub_id_19, 'end', text="No significant findings")
				else:
					self.tree.insert(sub_id_19, 'end', text=res[i][30])

				sub_id_20 = self.tree.insert(id, 'end', text="Therapeutic Intervention - Drugs")
				self.tree.insert(sub_id_20, 'end', text=res[i][31])

				sub_id_21 = self.tree.insert(id, 'end', text="Therapeutic Intervention - Diet")
				self.tree.insert(sub_id_21, 'end', text=res[i][32])

				sub_id_22 = self.tree.insert(id, 'end', text="Therapeutic Intervention - Lifestyle")
				self.tree.insert(sub_id_22, 'end', text=res[i][33])

				sub_id_23 = self.tree.insert(id, 'end', text="Therapeutic Intervention - Exercise")
				self.tree.insert(sub_id_23, 'end', text=res[i][34])

		cur.execute(("SELECT followup_date, assessment, icd_code, dpra FROM patientfollowuptree WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree_2.delete(*self.tree_2.get_children())

		for i in range(len(res)):
			id = self.tree.insert('', 'end', text=res[i][0])
			sub_id_2 = self.tree.insert(id, 'end', text="Assessment")
			self.tree.insert(sub_id_1, 'end', text=res[i][1])
			sub_id_2 = self.tree.insert(id, 'end', text="ICD Code")
			self.tree.insert(sub_id_1, 'end', text=res[i][2])
			sub_id_3 = self.tree.insert(id, 'end', text="Diagnostic/Prognostic Risk Assessments")
			self.tree.insert(sub_id_2, 'end', text=res[i][3])

class followup_assessment_table(tk.Frame): # Form containing the remaining additional form for follow-up record of patient (assessment table)

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 5)
		submenu_buttons_3(self, self.controller, 1)
		
		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		self.followup_date = self.controller.get_page("followup_patient_form").f_date_input.get_date().strftime('%Y-%m-%d')

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
		self.tree.column("#0", minwidth=200, width=500, stretch="no") 
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=25, y=190)

		therapeutic_label = tk.Label(form_frame, text="Therapeutic Intervention", font=self.label_font_2)
		therapeutic_label.place(x=575, y=190)

		drugs_label = tk.Label(form_frame, text="Drugs:", font=self.label_font, fg="#636363")
		drugs_label.place(x=575, y=215)
		self.drugs = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.drugs.place(x=575, y=240)

		diet_label = tk.Label(form_frame, text="Dietary advice:", font=self.label_font, fg="#636363")
		diet_label.place(x=575, y=280)
		self.diet = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.diet.place(x=575, y=305)

		lifestyle_label = tk.Label(form_frame, text="Lifestyle change:", font=self.label_font, fg="#636363")
		lifestyle_label.place(x=575, y=355)
		self.lifestyle = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.lifestyle.place(x=575, y=380)

		exer_label = tk.Label(form_frame, text="Exercises (type/duration)", font=self.label_font, fg="#636363")
		exer_label.place(x=575, y=430)
		self.exer = tk.Text(form_frame, height = 2, width = 35, wrap="word")
		self.exer.place(x=575, y=455)


		tk.Button(form_frame, text="Add Follow-up record", command=lambda: self.add_follow_up(), height = 3, width = 20, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007", wraplength = 150).place(x=650, y=530)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("followup_patient_form_2"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def load_data(self):
		self.followup_date = self.controller.get_page("followup_patient_form").f_date_input.get_date().strftime('%Y-%m-%d')

		self.assess.delete('1.0', 'end')
		self.icd_code.delete('1.0', 'end')
		self.dpra.delete('1.0', 'end')
		self.drugs.delete('1.0', 'end')
		self.diet.delete('1.0', 'end')
		self.lifestyle.delete('1.0', 'end')
		self.exer.delete('1.0', 'end')

	def add_follow_up(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.controller.get_page("followup_patient_form_2").add_details()

		cur.execute(("SELECT log_id FROM patientfollowup WHERE patient_id = %s and followup_date = %s"), (self.controller.patient_id.get(), self.followup_date))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientfollowup (ti_drugs, ti_diet, ti_lifestyle, ti_exer, patient_id) VALUES (%s, %s, %s, %s, %s)"
			val = (self.drugs.get("1.0",'end-1c'), self.diet.get("1.0",'end-1c'), self.lifestyle.get("1.0",'end-1c'), self.exer.get("1.0",'end-1c'), self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientfollowup SET ti_drugs = %s, ti_diet = %s, ti_lifestyle = %s, ti_exer = %s WHERE patient_id = %s and followup_date = %s"
			val = (self.drugs.get("1.0",'end-1c'), self.diet.get("1.0",'end-1c'), self.lifestyle.get("1.0",'end-1c'), self.exer.get("1.0",'end-1c'), self.controller.patient_id.get(), self.followup_date)
			cur.execute(sql, val)
			mydb.commit()

		self.drugs.delete('1.0', 'end') 
		self.diet.delete('1.0', 'end') 
		self.lifestyle.delete('1.0', 'end') 
		self.exer.delete('1.0', 'end') 

		self.controller.show_frame("followup_patient_form")

	def add_to_table(self, assessment, icd, dpra):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		sql = "INSERT INTO patientfollowuptree (followup_date, assessment, icd_code, dpra, patient_id) VALUES (%s, %s, %s, %s, %s)"
		val = (self.followup_date, assessment, icd, dpra, self.controller.patient_id.get())
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

class ReferralForm(tk.Frame): # Form containing the additional form for referrals and clinical summary

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 5)
		submenu_buttons_3(self, self.controller, 3)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=15)

		page_subtitle_1 = tk.Label(form_frame, text="Details of Referral", font=self.title_font)
		page_subtitle_1.place(x=400, y=20)

		r_date_label = tk.Label(form_frame, text="Date of Follow-up: ", font=self.label_font_2)
		r_date_label.place(x=90, y=55)

		self.r_date_input = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd")
		self.r_date_input.place(x=200, y=55)

		self.referring_phys = tk.Text(form_frame, height = 1, width = 65, wrap="word")
		self.referring_phys.place(x=220, y=85)
		referring_phys_label = tk.Label(form_frame, text="Referring Physicians:", font=self.label_font_2)
		referring_phys_label.place(x=90, y=85)

		self.phys_referred = tk.Text(form_frame, height = 1, width = 65, wrap="word")
		self.phys_referred.place(x=220, y=115)
		phys_referred_label = tk.Label(form_frame, text="Physician Referred to:", font=self.label_font_2)
		phys_referred_label.place(x=90, y=115)

		self.r_referral = tk.Text(form_frame, height = 4, width = 65, wrap="word")
		self.r_referral.place(x=220, y=145)
		r_referral_label = tk.Label(form_frame, text="Reason for Referral:", font=self.label_font_2)
		r_referral_label.place(x=90, y=145)

		tk.Button(form_frame, text="Add Referral", command=lambda: self.add_referral(self.r_date_input.get_date().strftime('%Y-%m-%d'), self.referring_phys.get("1.0",'end-1c'), self.phys_referred.get("1.0",'end-1c'), self.r_referral.get("1.0",'end-1c')), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=770, y=100)
		tk.Button(form_frame, text="Show Referrals", command=lambda: self.show_referral(), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=770, y=140)
		
		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=220)

		page_subtitle_2 = tk.Label(form_frame, text="Clinical Summary", font=self.title_font)
		page_subtitle_2.place(x=400, y=225)

		p_name_label = tk.Label(form_frame, text="Name of Patient:", font=self.label_font_2)
		p_name_label.place(x=90, y=255)
		self.p_name = tk.Label(form_frame, text="", font=self.label_font)
		self.p_name.place(x=200, y=255)

		p_agegender_label = tk.Label(form_frame, text="Age/Gender:", font=self.label_font_2)
		p_agegender_label.place(x=90, y=275)
		self.p_agegender = tk.Label(form_frame, text="", font=self.label_font)
		self.p_agegender.place(x=200, y=275)

		p_working_impre_label = tk.Label(form_frame, text="Working Impression:", font=self.label_font_2)
		p_working_impre_label.place(x=90, y=305)
		self.p_working_impre = tk.Text(form_frame, height = 1, width = 65, wrap="word")
		self.p_working_impre.place(x=230, y=305)

		p_brief_hist_label = tk.Label(form_frame, text="Brief History and PE:", font=self.label_font_2)
		p_brief_hist_label.place(x=90, y=335)
		self.p_brief_hist = tk.Text(form_frame, height = 4, width = 65, wrap="word")
		self.p_brief_hist.place(x=230, y=335)

		p_summ_lab_label = tk.Label(form_frame, text="Summary of Lab Results if applicable:", font=self.label_font_2)
		p_summ_lab_label.place(x=90, y=415)
		self.p_summ_lab = tk.Text(form_frame, height = 4, width = 82, wrap="word")
		self.p_summ_lab.place(x=92, y=435)

		p_summ_med_label = tk.Label(form_frame, text="Summary of Medications if applicable:", font=self.label_font_2)
		p_summ_med_label.place(x=90, y=515)
		self.p_summ_med = tk.Text(form_frame, height = 4, width = 82, wrap="word")
		self.p_summ_med.place(x=92, y=535)

		tk.Button(form_frame, text="Edit Summary", command=lambda: self.edit_summary(), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=790, y=455)
		tk.Button(form_frame, text="Add Summary", command=lambda: self.add_summary(self.p_name['text'], self.p_agegender['text'], self.p_working_impre.get("1.0",'end-1c'), self.p_brief_hist.get("1.0",'end-1c'), self.p_summ_lab.get("1.0",'end-1c'), self.p_summ_med.get("1.0",'end-1c')), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=790, y=415)

	def add_referral(self, date, referring_phys, phys_referred, reason):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		sql = "INSERT INTO patientreferral (date_of_followup, referring_phys, phys_referred_to, reasons, patient_id) VALUES (%s, %s, %s, %s, %s)"
		val = (date, referring_phys, phys_referred, reason, self.controller.patient_id.get())
		cur.execute(sql, val)
		mydb.commit()

		self.r_date_input.set_date(dt.datetime.today())
		self.referring_phys.delete('1.0', 'end')
		self.phys_referred.delete('1.0', 'end')
		self.r_referral.delete('1.0', 'end')

	def show_referral(self):
		self.controller.show_frame("ReferralForm_res")

	def add_summary(self, name, agegender, working_impre, brief_hist, summ_lab, summ_med):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT log_id FROM patientsummary WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			sql = "INSERT INTO patientsummary (impression, brief_history, summ_lab, summ_meds, patient_id) VALUES (%s, %s, %s, %s, %s)"
			val = (working_impre, brief_hist, summ_lab, summ_med, self.controller.patient_id.get())
			cur.execute(sql, val)
			mydb.commit()
		else:
			sql = "UPDATE patientsummary SET impression = %s, brief_history = %s, summ_lab = %s, summ_meds = %s WHERE patient_id = %s"
			val = (working_impre, brief_hist, summ_lab, summ_med, self.controller.patient_id.get())
			mydb.commit()

		self.p_working_impre.config(state="disabled", bg = "#e8e8e8")
		self.p_brief_hist.config(state="disabled", bg = "#e8e8e8")
		self.p_summ_lab.config(state="disabled", bg = "#e8e8e8")
		self.p_summ_med.config(state="disabled", bg = "#e8e8e8")

	def edit_summary(self):
		self.p_working_impre.config(state="normal", bg = "#ffffff")
		self.p_brief_hist.config(state="normal", bg = "#ffffff")
		self.p_summ_lab.config(state="normal", bg = "#ffffff")
		self.p_summ_med.config(state="normal", bg = "#ffffff")

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.p_working_impre.delete('1.0', 'end')
		self.p_brief_hist.delete('1.0', 'end')
		self.p_summ_lab.delete('1.0', 'end')
		self.p_summ_med.delete('1.0', 'end')

		cur.execute(("SELECT last_name, first_name, middle_name, age, gender FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.p_name['text'] = res[0] + ", " + res[1] + " " + res[2]
			self.p_agegender['text'] =  str(res[3]) + " / " + res[4]
		else:
			self.p_name['text'] = ""
			self.p_agegender['text'] = ""

		cur.execute(("SELECT log_id, impression, brief_history, summ_lab, summ_meds FROM patientsummary WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is not None:
			self.p_working_impre.insert('1.0', res[1])
			self.p_brief_hist.insert('1.0', res[2])
			self.p_summ_lab.insert('1.0', res[3])
			self.p_summ_med.insert('1.0', res[4])
			self.p_working_impre.config(state="disabled", bg = "#e8e8e8")
			self.p_brief_hist.config(state="disabled", bg = "#e8e8e8")
			self.p_summ_lab.config(state="disabled", bg = "#e8e8e8")
			self.p_summ_med.config(state="disabled", bg = "#e8e8e8")
		else:
			self.p_working_impre.delete('1.0', 'end')
			self.p_brief_hist.delete('1.0', 'end')
			self.p_summ_lab.delete('1.0', 'end')
			self.p_summ_med.delete('1.0', 'end')
			self.p_working_impre.config(state="normal", bg = "#ffffff")
			self.p_brief_hist.config(state="normal", bg = "#ffffff")
			self.p_summ_lab.config(state="normal", bg = "#ffffff")
			self.p_summ_med.config(state="normal", bg = "#ffffff")

class ReferralForm_res(tk.Frame): # Form for viewing records of referrals

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 3)
		submenu_buttons_3(self, self.controller, 3)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		self.tree = ttk.Treeview(form_frame, height = 25)
		self.tree.heading("#0", text="Referral Records")
		self.tree.column("#0", minwidth=150, width=850, stretch="no")
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=65, y=25)

		self.res_bttn = tk.Button(self, text="Go Back", command=lambda: controller.show_frame("ReferralForm"), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.res_bttn.place(x=950, y=635)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT date_of_followup, referring_phys, phys_referred_to, reasons FROM patientreferral WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree.delete(*self.tree.get_children())

		for i in range(len(res)):
			if res[i][0] is not None:
				id = self.tree.insert('', 'end', text=str(res[i][0]) + " - Referring Physicians: " + res[i][1])
				sub_id_1 = self.tree.insert(id, 'end', text="Physician Referred to")
				self.tree.insert(sub_id_1, 'end', text=res[i][2])
				sub_id_2 = self.tree.insert(id, 'end', text="Reason for Referral")
				self.tree.insert(sub_id_2, 'end', text=res[i][3])
