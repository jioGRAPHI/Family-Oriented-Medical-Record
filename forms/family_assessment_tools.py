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

def submenu_buttons_2(self, controller, num):
	side_menu_frame = tk.Frame(self, height = 720, width = 200)
	side_menu_frame.pack(side="left")

	b1 = tk.Button(side_menu_frame, text="Family Assessment Tools", command=lambda: controller.show_frame("FamAssessForm"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b1.place(x=25, y=160)
	b2 = tk.Button(side_menu_frame, text="Family APGAR", command=lambda: controller.show_frame("family_apgar_form"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b2.place(x=25, y=220)

	if(num == 1):
		b1.config(bg = "#2553a8")
	else:
		b2.config(bg = "#2553a8")

class FamAssessForm(tk.Frame): # Form contaning the Genogram, Family Map, ECOMAP, and Family Wellness Plan

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 4)
		submenu_buttons_2(self, self.controller, 1)

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		self.title_font = tkfont.Font(family='Times New Roman', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size = 8)
		self.label_font_2 = tkfont.Font(family='Helvetica', size = 8, weight="bold")
		self.notes_font = tkfont.Font(family='Helvetica', size = 8, slant="italic")

		label = tk.Label(form_frame, text="FAMILY ASSESSMENT TOOLS", font=self.title_font)
		label.place(x=375, y=15)

		self.genogram = tk.Text(form_frame, height = 8, width = 30, wrap="word")
		self.genogram.place(x=90, y=80)
		genogram_label = tk.Label(form_frame, text="A. Genogram", font=self.label_font, fg="#636363")
		genogram_label.place(x=90, y=60)

		self.fammap = tk.Text(form_frame, height = 8, width = 30, wrap="word")
		self.fammap.place(x=375, y=80)
		fammap_label = tk.Label(form_frame, text="B. Family Map", font=self.label_font, fg="#636363")
		fammap_label.place(x=375, y=60)

		self.ecomap = tk.Text(form_frame, height = 8, width = 30, wrap="word")
		self.ecomap.place(x=660, y=80)
		ecomap_label = tk.Label(form_frame, text="C. ECOMAP", font=self.label_font, fg="#636363")
		ecomap_label.place(x=660, y=60)

		tk.Button(form_frame, text="Add Details", command=lambda: self.add_details_map(self.genogram.get('1.0', 'end-1c'), self.fammap.get('1.0', 'end-1c'), self.ecomap.get('1.0', 'end-1c')), height = 2, width = 15, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=335, y=230)
		self.edit_bttn = tk.Button(form_frame, text="Edit", command=lambda: self.edit(), height = 2, width = 15, bd = 0, bg = "#183873", fg = "#ffffff", activebackground = "#cf0007")
		self.edit_bttn.place(x=525, y=230)
		self.edit_bttn.config(state = "disabled")

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=605, y=275)

		fam_wellness_label = tk.Label(form_frame, text="Family Wellness Plan", font=self.label_font_2)
		fam_wellness_label.place(x=90, y=280)
		fam_wellness_dir_label = tk.Label(form_frame, text="List down wellness plan and put a check mark after when completed.", font=self.notes_font, fg="#636363")
		fam_wellness_dir_label.place(x=90, y=295)

		fam_member_label = tk.Label(form_frame, text="Family Member", font=self.label_font, fg="#636363")
		fam_member_label.place(x=110, y=320)
		self.fam_member = tk.Text(form_frame, height = 1, width = 35, wrap="word")
		self.fam_member.place(x=110, y=340)

		scrnning_label = tk.Label(form_frame, text="Screening Test", font=self.label_font, fg="#636363")
		scrnning_label.place(x=430, y=320)

		immno_label = tk.Label(form_frame, text="Immunization", font=self.label_font, fg="#636363")
		immno_label.place(x=530, y=320)

		lfstyle_label = tk.Label(form_frame, text="Lifestyle Changes", font=self.label_font, fg="#636363")
		lfstyle_label.place(x=630, y=320)

		cnsling_label = tk.Label(form_frame, text="Counseling needs", font=self.label_font, fg="#636363")
		cnsling_label.place(x=730, y=320)

		self.lob = []
		self.b_var = []

		self.screening_var = 0
		self.immunization_var = 0
		self.lifestyle_var = 0
		self.counseling_var = 0

		x_value = 440

		for i in range(4):
			self.b_var.append(0)
			b = tk.Button(form_frame, text="✓", command=partial(self.set_var, i), height = 1, width = 5, bd = 1, fg = "#000000", bg = "#e3e3e3")
			b.place(x=x_value, y=340)
			self.lob.append(b)
			x_value = x_value + 100

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=370)

		self.tree = ttk.Treeview(form_frame, height = 8, columns=("A", "B", "C", "D"))
		self.tree.heading("#0", text="Family Member")
		self.tree.heading("A", text="Screening Test")
		self.tree.heading("B", text="Immunization")
		self.tree.heading("C", text="Lifestyle Changes")
		self.tree.heading("D", text="Counseling needs")
		self.tree.column("#0", minwidth=0, width=300, stretch="no")
		self.tree.column("A", minwidth=0, width=120, stretch="no") 
		self.tree.column("B", minwidth=0, width=120, stretch="no") 
		self.tree.column("C", minwidth=0, width=120, stretch="no") 
		self.tree.column("D", minwidth=0, width=120, stretch="no") 
		vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=vsb.set)
		self.tree.place(x=110, y=410)

		tk.Button(form_frame, text="Add", command=lambda: self.add_details(self.fam_member.get('1.0', 'end-1c'), self.screening_var, self.immunization_var, self.lifestyle_var, self.counseling_var), height = 2, width = 5, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=850, y=320)

	def edit(self):
		self.genogram.config(state = "normal", bg = "#ffffff")
		self.fammap.config(state = "normal", bg = "#ffffff")
		self.ecomap.config(state = "normal", bg = "#ffffff")

	def set_var(self, i):
		if self.b_var[i] == 0:
			self.b_var[i] = 1
			vote = self.b_var[i]
		else:
			self.b_var[i] = 0
			vote = self.b_var[i]


		if i == 0:
			if vote == 1:
				self.screening_var = 1
				(self.lob[i]).config(bg = "#0060ba", fg = "#ffffff")
			else:
				self.screening_var = 0
				(self.lob[i]).config(fg = "#000000", bg = "#e3e3e3")
		elif i == 1:
			if vote == 1:
				self.immunization_var = 1
				(self.lob[i]).config(bg = "#0060ba", fg = "#ffffff")
			else:
				self.immunization_var = 0
				(self.lob[i]).config(fg = "#000000", bg = "#e3e3e3")
		elif i == 2:
			if vote == 1:
				self.lifestyle_var = 1
				(self.lob[i]).config(bg = "#0060ba", fg = "#ffffff")
			else:
				self.lifestyle_var = 0
				(self.lob[i]).config(fg = "#000000", bg = "#e3e3e3")
		else:
			if vote == 1:
				self.counseling_var = 1
				(self.lob[i]).config(bg = "#0060ba", fg = "#ffffff")
			else:
				self.counseling_var = 0
				(self.lob[i]).config(fg = "#000000", bg = "#e3e3e3")

	def add_details_map(self, genogram, fammap, ecomap):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT patient_id FROM patientfamassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			cur.execute(("INSERT INTO patientfamassessment (genogram, family_map, ecomap, patient_id) VALUES (%s, %s, %s, %s)"), (genogram, fammap, ecomap, self.controller.patient_id.get()))
			mydb.commit()
		else:
			cur.execute(("UPDATE patientfamassessment SET genogram = %s, family_map = %s, ecomap = %s WHERE patient_id = %s"), (genogram, fammap, ecomap, self.controller.patient_id.get()))
			mydb.commit()

		self.genogram.config(state = "disabled", bg = "#c4c4c4")
		self.fammap.config(state = "disabled", bg = "#c4c4c4")
		self.ecomap.config(state = "disabled", bg = "#c4c4c4")
		self.edit_bttn.config(state = "normal")

	def add_details(self, name, scr_in, if_in, lf_in, c_in):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		if name == "":
			messagebox.showwarning("Warning", "Please input a family member")
		else:
			cur.execute(("SELECT member_name FROM patientfammember WHERE patient_id = %s and member_name = %s"), (self.controller.patient_id.get(), name))
			res = cur.fetchone()
			if res is None:
				cur.execute(("INSERT INTO patientfammember (member_name, screening, immunization, lifestyle_changes, counseling_needs, patient_id) VALUES (%s, %s, %s, %s, %s, %s)"), (name, int(scr_in), int(if_in), int(lf_in), int(c_in), self.controller.patient_id.get()))
				mydb.commit()
			else:
				cur.execute(("UPDATE patientfammember SET member_name = %s, screening = %s, immunization = %s, lifestyle_changes = %s, counseling_needs = %s WHERE patient_id = %s and member_name = %s"), (name, int(scr_in), int(if_in), int(lf_in), int(c_in), self.controller.patient_id.get(), name))
				mydb.commit()

			id = self.tree.insert('', 'end', text=name)
			if scr_in == 1:
				self.tree.set(id, 'A', "Yes")
			else:
				self.tree.set(id, 'A', "No")

			if if_in == 1:
				self.tree.set(id, 'B', "Yes")
			else:
				self.tree.set(id, 'B', "No")

			if lf_in == 1:
				self.tree.set(id, 'C', "Yes")
			else:
				self.tree.set(id, 'C', "No")

			if c_in == 1:
				self.tree.set(id, 'D', "Yes")
			else:
				self.tree.set(id, 'D', "No")

			self.fam_member.delete('1.0', 'end')

			self.screening_var = 0
			self.immunization_var = 0
			self.lifestyle_var = 0
			self.counseling_var = 0
			
			for i in range(4):
				(self.lob[i]).config(fg = "#000000", bg = "#e3e3e3")

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.genogram.delete('1.0', 'end')
		self.fammap.delete('1.0', 'end')
		self.ecomap.delete('1.0', 'end')
		
		cur.execute(("SELECT genogram, family_map, ecomap FROM patientfamassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				self.genogram.insert('1.0', res[0])
			if res[1] is not None:
				self.fammap.insert('1.0', res[1])
			if res[2] is not None:
				self.ecomap.insert('1.0', res[2])
			self.genogram.config(state = "disabled", bg = "#e8e8e8")
			self.fammap.config(state = "disabled", bg = "#e8e8e8")
			self.ecomap.config(state = "disabled", bg = "#e8e8e8")
			self.edit_bttn.config(state = "normal")
		else:
			self.genogram.delete('1.0', 'end')
			self.fammap.delete('1.0', 'end')
			self.ecomap.delete('1.0', 'end')

		self.fam_member.delete('1.0', 'end')

		cur.execute(("SELECT member_name, screening, immunization, lifestyle_changes, counseling_needs FROM patientfammember WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchall()

		self.tree.delete(*self.tree.get_children())

		for i in range(len(res)):
			id = self.tree.insert('', 'end', text=res[i][0])
			if res[i][1] == 1:
				self.tree.set(id, 'A', "Yes")
			else:
				self.tree.set(id, 'A', "No")

			if res[i][2] == 1:
				self.tree.set(id, 'B', "Yes")
			else:
				self.tree.set(id, 'B', "No")

			if res[i][3] == 1:
				self.tree.set(id, 'C', "Yes")
			else:
				self.tree.set(id, 'C', "No")

			if res[i][4] == 1:
				self.tree.set(id, 'D', "Yes")
			else:
				self.tree.set(id, 'D', "No")

class family_apgar_form(tk.Frame): # Form containing the Family APGAR form 

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 4)
		submenu_buttons_2(self, self.controller, 2)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.subtitle_font = tkfont.Font(family='Helvetica', size=9, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=8, slant="italic")
		self.label_font2 = tkfont.Font(family='Helvetica', size=8, weight="bold")
		self.label_font3 = tkfont.Font(family='Helvetica', size=10, weight="bold", slant="italic")

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		with open("./data/APGAR.txt", 'r') as f:
			apgar_questions = f.read().splitlines()
		f.close()

		question_label = tk.Label(form_frame, text="Areas of the APGAR", font=self.subtitle_font)
		question_label.place(x=110, y=25)

		y_value = 70

		fam_num_1_label = tk.Label(form_frame, text="Family Member 1", font=self.subtitle_font, wraplength=70)
		fam_num_1_label.place(x=505, y=25)

		fam_num_2_label = tk.Label(form_frame, text="Family Member 2", font=self.subtitle_font, wraplength=70)
		fam_num_2_label.place(x=645, y=25)

		average_label = tk.Label(form_frame, text="Average", font=self.subtitle_font, wraplength=70)
		average_label.place(x=780, y=25)

		self.apgar_var = []
		self.apgar_cb = []
		self.average = []
		self.vote_1_arr = []
		self.vote_2_arr = []
		self.avg_vote = []
		self.vote_1 = 0
		self.vote_2 = 0
		self.avg_value = 0

		for i in range(0, len(apgar_questions), 2):
			cLabelFrame = tk.Frame(form_frame)
			cLabelFrame.place(x=90, y=y_value)

			tk.Label(cLabelFrame, text=apgar_questions[i], font=self.label_font, wraplength=350, justify="left").grid(row=0, column=0, sticky="w")
			tk.Label(cLabelFrame, text=apgar_questions[i+1], font=self.label_font2, wraplength=350, justify="left").grid(row=1, column=0, sticky="w")

			var = []
			cb_arr = []
			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="0", variable=var[0])
			cb.place(x=480, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="1", variable=var[1])
			cb.place(x=520, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="2", variable=var[2])
			cb.place(x=560, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="0", variable=var[3])
			cb.place(x=620, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="1", variable=var[4])
			cb.place(x=660, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar(self))
			cb = tk.Checkbutton(form_frame, text="2", variable=var[5])
			cb.place(x=700, y=y_value)
			cb_arr.append(cb)

			cb_arr[0].config(command=partial(self.check_cb, cb_arr, var, 0, self.average, (i//2)))
			cb_arr[1].config(command=partial(self.check_cb, cb_arr, var, 1, self.average, (i//2)))
			cb_arr[2].config(command=partial(self.check_cb, cb_arr, var, 2, self.average, (i//2)))
			cb_arr[3].config(command=partial(self.check_cb, cb_arr, var, 3, self.average, (i//2)))
			cb_arr[4].config(command=partial(self.check_cb, cb_arr, var, 4, self.average, (i//2)))
			cb_arr[5].config(command=partial(self.check_cb, cb_arr, var, 5, self.average, (i//2)))

			self.apgar_var.append(var)
			self.apgar_cb.append(cb_arr)
			self.vote_1_arr.append(0)
			self.vote_2_arr.append(0)
			self.avg_vote.append(0)

			avg_txt = tk.Label(form_frame, text="", font=self.label_font3)
			avg_txt.place(x=795, y=y_value)

			self.average.append(avg_txt)

			y_value = y_value + 100

		overall_label = tk.Label(form_frame, text="Overall Assessment", font=self.subtitle_font)
		overall_label.place(x=110, y=y_value-30)

		self.overall_f1_txt = tk.Label(form_frame, text="", font=self.label_font, wraplength=120)
		self.overall_f1_txt.place(x=485, y=y_value-30)

		self.overall_f2_txt = tk.Label(form_frame, text="", font=self.label_font, wraplength=120)
		self.overall_f2_txt.place(x=625, y=y_value-30)

		self.overall_avg_txt = tk.Label(form_frame, text="", font=self.label_font, wraplength=120)
		self.overall_avg_txt.place(x=775, y=y_value-30)

		tk.Label(form_frame, text="*Score: 0-hardly ever (halos hindi), 1-some of the time (minsan), 2-almost always (palagi)", font=self.label_font, fg="#636363").place(x=110, y=y_value+ 10)
		tk.Label(form_frame, text="*Interpretation: 0-3 severely dysfunctional, 4-6 moderately dysfunctional, 7-10 highly functional", font=self.label_font, fg="#636363").place(x=110, y=y_value + 30)

		self.sub_bttn = tk.Button(form_frame, text="Submit", command=lambda: self.submit(), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.sub_bttn.place(x=660, y=y_value + 10)

		self.res_bttn = tk.Button(form_frame, text="Show Results", command=lambda: controller.show_frame("family_apgar_form_res"), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.res_bttn.place(x=820, y=y_value + 10)
		self.res_bttn.config(state = "disabled")

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT fam_1_apgar_score, fam_2_apgar_score, avg_apgar_score FROM patientfamassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			self.res_bttn.config(state = "disabled")
		else:
			self.res_bttn.config(state = "normal")

		for i in range(5):
			self.apgar_var[i][0].set(0)
			self.apgar_var[i][1].set(0)
			self.apgar_var[i][2].set(0)
			self.apgar_var[i][3].set(0)
			self.apgar_var[i][4].set(0)
			self.apgar_var[i][5].set(0)

			self.apgar_cb[i][0].config(state="normal")
			self.apgar_cb[i][1].config(state="normal")
			self.apgar_cb[i][2].config(state="normal")
			self.apgar_cb[i][3].config(state="normal")
			self.apgar_cb[i][4].config(state="normal")
			self.apgar_cb[i][5].config(state="normal")

			self.average[i]['text'] = ""

			self.vote_1_arr[i] = 0
			self.vote_2_arr[i] = 0
			self.avg_vote[i] = 0

		self.vote_1 = 0
		self.vote_2 = 0
		self.overall_f1_txt['text'] = ""
		self.overall_f2_txt['text'] = ""
		self.overall_avg_txt['text'] = "" 

	def check_cb(self, cb_arr, cb_var_arr, i, average, index):
		if i < 3:
			if i == 0:
				if cb_var_arr[i].get() == 1:
					cb_arr[i+1].config(state="disabled")
					cb_arr[i+2].config(state="disabled")
					self.vote_1_arr[index] = 0
				else:
					cb_arr[i+1].config(state="normal")
					cb_arr[i+2].config(state="normal")
					self.vote_1_arr[index] = 0
			elif i == 1:
				if cb_var_arr[i].get() == 1:
					cb_arr[i-1].config(state="disabled")
					cb_arr[i+1].config(state="disabled")
					self.vote_1 = self.vote_1 + 1
					self.vote_1_arr[index] = 1
				else:
					cb_arr[i-1].config(state="normal")
					cb_arr[i+1].config(state="normal")
					self.vote_1 = self.vote_1 - 1
					self.vote_1_arr[index] = 0
			else:
				if cb_var_arr[i].get() == 1:
					cb_arr[i-1].config(state="disabled")
					cb_arr[i-2].config(state="disabled")
					self.vote_1 = self.vote_1 + 2
					self.vote_1_arr[index] = 2
				else:
					cb_arr[i-1].config(state="normal")
					cb_arr[i-2].config(state="normal")
					self.vote_1 = self.vote_1 - 2
					self.vote_1_arr[index] = 0
		else:
			if i == 3:
				if cb_var_arr[i].get() == 1:
					cb_arr[i+1].config(state="disabled")
					cb_arr[i+2].config(state="disabled")
					self.vote_2_arr[index] = 0
				else:
					cb_arr[i+1].config(state="normal")
					cb_arr[i+2].config(state="normal")
					self.vote_2_arr[index] = 0
			elif i == 4:
				if cb_var_arr[i].get() == 1:
					cb_arr[i-1].config(state="disabled")
					cb_arr[i+1].config(state="disabled")
					self.vote_2 = self.vote_2 + 1
					self.vote_2_arr[index] = 1
				else:
					cb_arr[i-1].config(state="normal")
					cb_arr[i+1].config(state="normal")
					self.vote_2 = self.vote_2 - 1
					self.vote_2_arr[index] = 0
			else:
				if cb_var_arr[i].get() == 1:
					cb_arr[i-1].config(state="disabled")
					cb_arr[i-2].config(state="disabled")
					self.vote_2 = self.vote_2 + 2
					self.vote_2_arr[index] = 2
				else:
					cb_arr[i-1].config(state="normal")
					cb_arr[i-2].config(state="normal")
					self.vote_2 = self.vote_2 - 2
					self.vote_2_arr[index] = 0

		for i in range(5):
			temp_avg = (self.vote_1_arr[i] + self.vote_2_arr[i]) / 2
			self.average[i]['text'] = str(temp_avg)
			self.avg_vote[i] = temp_avg

		self.avg_value = 0
		for i in range(len(self.avg_vote)):
			self.avg_value = self.avg_value + self.avg_vote[i]

		if self.avg_value <= 3:
			self.overall_avg_txt['text'] = str(self.avg_value) +" - Severely dysfunctional" 
		elif self.avg_value <= 6:
			self.overall_avg_txt['text'] = str(self.avg_value) + " - Moderately dysfunctional" 
		else:
			self.overall_avg_txt['text'] = str(self.avg_value) + " - Highly functional"


		if self.vote_1 <= 3:
			self.overall_f1_txt['text'] = str(self.vote_1) +" - Severely dysfunctional" 
		elif self.vote_1 <= 6:
			self.overall_f1_txt['text'] = str(self.vote_1) + " - Moderately dysfunctional" 
		else:
			self.overall_f1_txt['text'] = str(self.vote_1) + " - Highly functional"

		if self.vote_2 <= 3:
			self.overall_f2_txt['text'] = str(self.vote_2) +" - Severely dysfunctional" 
		elif self.vote_2 <= 6:
			self.overall_f2_txt['text'] = str(self.vote_2) + " - Moderately dysfunctional" 
		else:
			self.overall_f2_txt['text'] = str(self.vote_2) + " - Highly functional"

	def submit(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT fam_1_apgar_score, fam_2_apgar_score, avg_apgar_score FROM patientfamassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			cur.execute(("INSERT INTO patientfamassessment (fam_1_apgar_score, fam_2_apgar_score, avg_apgar_score, patient_id) VALUES (%s, %s, %s, %s)"), (int(self.vote_1), int(self.vote_2), int(self.avg_value), self.controller.patient_id.get()))
			mydb.commit()
		else:
			cur.execute(("UPDATE patientfamassessment SET fam_1_apgar_score = %s, fam_2_apgar_score = %s, avg_apgar_score = %s WHERE patient_id = %s"), (int(self.vote_1), int(self.vote_2), int(self.avg_value), self.controller.patient_id.get()))
			mydb.commit()

		self.res_bttn.config(state = "normal")

class family_apgar_form_res(tk.Frame): # Form for viewing of previous Family APGAR results only

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 4)
		submenu_buttons_2(self, self.controller, 2)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.subtitle_font = tkfont.Font(family='Helvetica', size=12, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=8, slant="italic")
		self.label_font2 = tkfont.Font(family='Helvetica', size=8, weight="bold")
		self.label_font3 = tkfont.Font(family='Helvetica', size=10, weight="bold", slant="italic")

		form_frame = tk.Frame(self, height = 720, width = 1000)
		form_frame.pack(side="left")

		question_label = tk.Label(form_frame, text="Results of the Previous APGAR", font=self.subtitle_font)
		question_label.place(x=110, y=60)

		y_value = 70

		fam_num_1_label = tk.Label(form_frame, text="Family Member 1: ", font=self.label_font3, fg ="#636362")
		fam_num_1_label.place(x=110, y=100)

		fam_num_2_label = tk.Label(form_frame, text="Family Member 2: ", font=self.label_font3, fg ="#636362")
		fam_num_2_label.place(x=110, y=150)

		average_label = tk.Label(form_frame, text="Average: ", font=self.label_font3, fg ="#636362")
		average_label.place(x=110, y=200)

		self.fam_num_1_score = tk.Label(form_frame, text="", font=self.title_font)
		self.fam_num_1_score.place(x=280, y=100)

		self.fam_num_2_score = tk.Label(form_frame, text="", font=self.title_font)
		self.fam_num_2_score.place(x=280, y=150)

		self.average_score = tk.Label(form_frame, text="", font=self.title_font)
		self.average_score.place(x=280, y=200)

		self.res_bttn = tk.Button(form_frame, text="Return", command=lambda: controller.show_frame("family_apgar_form"), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.res_bttn.place(x=820, y=580)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		self.fam_num_1_score['text'] = ""
		self.fam_num_2_score['text'] = ""
		self.average_score['text'] = ""

		cur.execute(("SELECT fam_1_apgar_score, fam_2_apgar_score, avg_apgar_score FROM patientfamassessment WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			if res[0] is not None:
				if int(res[0]) <= 3:
					self.fam_num_1_score['text'] = str(res[0]) +" - Severely dysfunctional" 
				elif int(res[0]) <= 6:
					self.fam_num_1_score['text'] = str(res[0]) + " - Moderately dysfunctional" 
				else:
					self.fam_num_1_score['text'] = str(res[0]) + " - Highly functional"

			if res[1] is not None:
				if int(res[1]) <= 3:
					self.fam_num_2_score['text']  = str(res[1]) +" - Severely dysfunctional" 
				elif int(res[1]) <= 6:
					self.fam_num_2_score['text']  = str(res[1]) + " - Moderately dysfunctional" 
				else:
					self.fam_num_2_score['text']  = str(res[1]) + " - Highly functional"

			if res[2] is not None:
				if int(res[2]) <= 3:
					self.average_score['text'] = str(res[2]) +" - Severely dysfunctional" 
				elif int(res[2]) <= 6:
					self.average_score['text'] = str(res[2]) + " - Moderately dysfunctional" 
				else:
					self.average_score['text'] = str(res[2]) + " - Highly functional"	
		else:
			self.fam_num_1_score['text'] = ""
			self.fam_num_2_score['text'] = ""
			self.average_score['text'] = ""
