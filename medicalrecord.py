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


def menu_frame(self, controller, num):
	menu_frame = tk.Frame(self, height = 60, width = 1200, bg = "#b1c3e6")
	menu_frame.pack(side="top")

	tk.Button(menu_frame, text="Patient Consultation Form", command=lambda: controller.show_frame("PatientForm"), height = 3, width = 32, bd = 0, bg = "#dbdbdb").place(x=5, y=9)
	tk.Button(menu_frame, text="Geriatric Depression Scale – Short Form", command=lambda: controller.show_frame("GeriaticForm"), height = 3, width = 32, bd = 0, bg = "#dbdbdb").place(x=245, y=9)
	tk.Button(menu_frame, text="First Consultation Record", command=lambda: controller.show_frame("FirstConsForm"), height = 3, width = 32, bd = 0, bg = "#dbdbdb").place(x=485, y=9)
	tk.Button(menu_frame, text="Family Assessment Tools", command=lambda: controller.show_frame("FamAssessForm"), height = 3, width = 32, bd = 0, bg = "#dbdbdb").place(x=725, y=9)
	tk.Button(menu_frame, text="Additional Form", command=lambda: controller.show_frame("followup_patient_form"), height = 3, width = 32, bd = 0, bg = "#dbdbdb").place(x=965, y=9)

	if(num == 1):
		tk.Button(menu_frame, text="Patient Consultation Form", command=lambda: controller.show_frame("PatientForm"), height = 3, width = 32, bd = 0).place(x=5, y=9)
	elif(num == 2):
		tk.Button(menu_frame, text="Geriatric Depression Scale – Short Form", command=lambda: controller.show_frame("GeriaticForm"), height = 3, width = 32, bd = 0).place(x=245, y=9)
	elif(num == 3):
		tk.Button(menu_frame, text="First Consultation Record", command=lambda: controller.show_frame("FirstConsForm"), height = 3, width = 32, bd = 0).place(x=485, y=9)
	elif(num == 4):
		tk.Button(menu_frame, text="Family Assessment Tools", command=lambda: controller.show_frame("FamAssessForm"), height = 3, width = 32, bd = 0).place(x=725, y=9)
	else:
		tk.Button(menu_frame, text="Additional Form", command=lambda: controller.show_frame("followup_patient_form"), height = 3, width = 32, bd = 0).place(x=965, y=9)

def submenu_buttons_1(self, controller, num):
	side_menu_frame = tk.Frame(self, height = 720, width = 200) # , bg = "#cfedc5"
	side_menu_frame.pack(side="left")

	b1 = tk.Button(side_menu_frame, text="Consultation Record", command=lambda: controller.show_frame("FirstConsForm"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b1.place(x=25, y=160)
	b2 = tk.Button(side_menu_frame, text="Physical Examination and Assessment", command=lambda: controller.show_frame("physical_examination_form"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b2.place(x=25, y=220)

	if(num == 1):
		b1.config(bg = "#2553a8")
	else:
		b2.config(bg = "#2553a8")

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

def submenu_buttons_3(self, controller, num):
	side_menu_frame = tk.Frame(self, height = 720, width = 200) # , bg = "#cfedc5"
	side_menu_frame.pack(side="left")

	b1 = tk.Button(side_menu_frame, text="Follow-up Patient Record", command=lambda: controller.show_frame("followup_patient_form"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b1.place(x=25, y=160)
	b2 = tk.Button(side_menu_frame, text="Referral Form and Clinical Summary", command=lambda: controller.show_frame("ReferralForm"), height = 3, width = 25, bd = 0, bg = "#183873", fg = "#ffffff", wraplength = 150)
	b2.place(x=25, y=220)

	if(num == 1):
		b1.config(bg = "#2553a8")
	else:
		b2.config(bg = "#2553a8")

class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.title_font = tkfont.Font(family='Times New Roman', size=14, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=10)

		self.frames = {}
		for F in (PatientForm, GeriaticForm, FirstConsForm, FamAssessForm, ReferralForm, review_of_systems_form, review_of_systems_form_2, physical_examination_form, assessment_table, family_apgar_form, followup_patient_form, followup_patient_form_2,followup_assessment_table):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("PatientForm")

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

class PatientForm(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 1)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=8)

		page_title = tk.Label(self, text="PATIENT CONSULTATION FORM", font=self.title_font)
		page_title.place(x=480, y=75)

		patient_name_label = tk.Label(self, text="FAMILY NAME, First Name: ", font=self.label_font, fg="#636363")
		patient_name_label.place(x=305, y=120)

		patient_name = tk.Text(self, height = 1, width = 55)
		patient_name.place(x=440, y=120)

		date_label = tk.Label(self, text="Date", font=self.label_font, fg="#636363")
		date_label.place(x=50, y=200)
		date_input = DateEntry(self, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd") # working
		date_input.place(x=50, y=220)

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

		tk.Button(self, text="ADD", command=lambda: self.add_details(date_input.get_date(), self.diag_input.get('1.0', 'end-1c'), self.phys_input.get('1.0', 'end-1c'), self.diags_input.get('1.0', 'end-1c'), self.med_input.get('1.0', 'end-1c'), self.disp_input.get('1.0', 'end-1c')), height = 2, width = 25, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=510, y=300)
		# add view records function
		# tk.Button(self, text="VIEW RECORDS", command=lambda: controller.show_frame("PatientFormView"), height = 2, width = 25, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#ffffff", activeforeground = "#000000").place(x=510, y=380)



	def add_details(self, date_in, diag_in, phys_in, diags_in, med_in, dis_in):
		# add details to new patient id if records does not exist, if it exists, append
		# print(date_in.get_date())
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

class GeriaticForm(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 2)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.subtitle_font = tkfont.Font(family='Helvetica', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=10)

		page_title = tk.Label(self, text="Geriatric Depression Scale – Short Form", font=self.title_font)
		page_title.place(x=460, y=68)

		patient_name_label = tk.Label(self, text="<FAMILY NAME, First Name>", font=self.title_font)
		patient_name_label.place(x=90, y=110)

		question_label = tk.Label(self, text="Question", font=self.subtitle_font)
		question_label.place(x=190, y=145)
		score_label = tk.Label(self, text="SCORE", font=self.subtitle_font)
		score_label.place(x=970, y=145)

		#  form starts here
		
		with open("./data/geriatic_questions.txt", 'r') as f:
			questions = f.read().splitlines()
		f.close()

		y_value = 175
		self.score = 0
		self.lob = []
		self.losl = []
		for i in range(len(questions)):
			b = []
			question_label = tk.Label(self, text=str(i + 1) + ".) " + questions[i], font=self.label_font)
			question_label.place(x=90, y=y_value)

			yes_b = tk.Button(self, text="Yes", command=partial(self.set_score, 1,i), height = 1, width = 5, bd = 1)
			yes_b.place(x=690, y=y_value) 
			no_b = tk.Button(self, text="No", command=partial(self.set_score, -1,i), height = 1, width = 5, bd = 1)
			no_b.place(x=790, y=y_value)
			score_label = tk.Label(self, text="", font=self.label_font)
			score_label.place(x=940, y=y_value)

			b.append(yes_b)
			b.append(no_b)
			self.lob.append(b)
			self.losl.append(score_label)

			y_value = y_value + 30

		self.total_score = tk.Label(self, text="Total: ", font=self.subtitle_font)
		self.total_score.place(x=940, y=635)
		self.total_score_value = tk.Label(self, text="", font=self.label_font)
		self.total_score_value.place(x=980, y=635)

	def set_score(self, vote, i):
		self.score = self.score + vote
		if vote == 1:
			(self.lob[i][1]).config(state = "disabled", bd = 0)
			(self.lob[i][0]).config(bg = "#0060ba", fg = "#ffffff")
			self.losl[i]['text'] = "Score 1 point for yes" 
		else:
			(self.lob[i][0]).config(state = "disabled", bd = 0)
			(self.lob[i][1]).config(bg = "#0060ba", fg = "#ffffff")
			self.losl[i]['text'] = "Score 1 point for no"
		if self.score >= 0:
			self.total_score_value['text'] = str(self.score) 

class FirstConsForm(tk.Frame):

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

class FamAssessForm(tk.Frame):

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

		tk.Button(form_frame, text="Add Details", command=lambda: self.add_details_map(self.genogram.get('1.0', 'end-1c'), self.fammap.get('1.0', 'end-1c'), self.ecomap.get('1.0', 'end-1c')), height = 2, width = 25, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=405, y=230)

		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=275)

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
			b = tk.Button(form_frame, text="✓", command=partial(self.set_var, i), height = 1, width = 5, bd = 1,fg = "#000000", bg = "#e3e3e3")
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
		# add family members
		# tk.Button(self, text="VIEW RECORDS", command=lambda: controller.show_frame("PatientFormView"), height = 2, width = 25, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#ffffff", activeforeground = "#000000").place(x=510, y=380)

	def set_var(self, i):
		if self.b_var[i] == 0:
			self.b_var[i] = 1
			vote =self.b_var[i]
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
		# add details to new patient id if records does not exist, if it exists, append
		# print(date_in.get_date())
		print(genogram)
		print(fammap)
		print(ecomap)

		self.genogram.delete('1.0', 'end')
		self.fammap.delete('1.0', 'end')
		self.ecomap.delete('1.0', 'end')

	def add_details(self, name, scr_in, if_in, lf_in, c_in):
		# add details to new patient id if records does not exist, if it exists, append
		# print(date_in.get_date())
		if name == "":
			messagebox.showwarning("Warning", "Please input a family member")
		else:
			print(name)
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

########################

class review_of_systems_form(tk.Frame):

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

		y_value = 70

		self.heent_var = []
		self.respi_var = []
		self.cardio_var = []
		self.gastro_var = []
		self.genito_var = []
		self.meta_var = []
		self.neuro_var = []
		self.musculo_var = []
		self.skin_var = []

		label = tk.Label(form_frame, text="Review of Systems:", font=self.label_font_2)
		label.place(x=25, y=25)

		with open("./data/heent.txt", 'r') as f:
			self.heent_opt = f.read().splitlines()
		f.close()

		heent_label = tk.Label(form_frame, text="HEENT", font=self.label_font, fg="#636363")
		heent_label.place(x=25, y=45)

		for i in range(len(self.heent_opt)):
			self.heent_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.heent_opt[i], variable=self.heent_var[i])
			cb.place(x=25, y=y_value)
			y_value = y_value + 20

		self.heent_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.heent_var[len(self.heent_opt)])
		cb.place(x=25, y=y_value)
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
			self.respi_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.respi_opt[i], variable=self.respi_var[i])
			cb.place(x=25, y=y_value)
			y_value = y_value + 20

		self.respi_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.respi_var[len(self.respi_opt)])
		cb.place(x=25, y=y_value)
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
			self.cardio_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.cardio_opt[i], variable=self.cardio_var[i])
			cb.place(x=25, y=y_value)
			y_value = y_value + 20

		self.cardio_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.cardio_var[len(self.cardio_opt)])
		cb.place(x=25, y=y_value)
		y_value = y_value + 20

		self.other_cardio = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_cardio.place(x=50, y=y_value)


		y_value = 25

		with open("./data/gastro.txt", 'r') as f:
			self.gastro_opt = f.read().splitlines()
		f.close()

		gastro_label = tk.Label(form_frame, text="Gastrointestinal", font=self.label_font, fg="#636363")
		gastro_label.place(x=300, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.gastro_opt)):
			self.gastro_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.gastro_opt[i], variable=self.gastro_var[i])
			cb.place(x=300, y=y_value)
			y_value = y_value + 20

		self.gastro_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.gastro_var[len(self.gastro_opt)])
		cb.place(x=300, y=y_value)
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
			self.genito_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.genito_opt[i], variable=self.genito_var[i])
			cb.place(x=300, y=y_value)
			y_value = y_value + 20

		self.genito_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.genito_var[len(self.genito_opt)])
		cb.place(x=300, y=y_value)
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
			self.meta_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.meta_opt[i], variable=self.meta_var[i])
			cb.place(x=300, y=y_value)
			y_value = y_value + 20

		self.meta_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.meta_var[len(self.meta_opt)])
		cb.place(x=300, y=y_value)
		y_value = y_value + 20

		self.other_meta = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_meta.place(x=325, y=y_value)


		y_value = 25

		with open("./data/neuro.txt", 'r') as f:
			self.neuro_opt = f.read().splitlines()
		f.close()

		neuro_label = tk.Label(form_frame, text="Neurologic", font=self.label_font, fg="#636363")
		neuro_label.place(x=575, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.neuro_opt)):
			self.neuro_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.neuro_opt[i], variable=self.neuro_var[i])
			cb.place(x=575, y=y_value)
			y_value = y_value + 20

		self.neuro_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.neuro_var[len(self.neuro_opt)])
		cb.place(x=575, y=y_value)
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
			self.musculo_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.musculo_opt[i], variable=self.musculo_var[i])
			cb.place(x=575, y=y_value)
			y_value = y_value + 20

		self.musculo_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.musculo_var[len(self.musculo_opt)])
		cb.place(x=575, y=y_value)
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
			self.skin_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.skin_opt[i], variable=self.skin_var[i])
			cb.place(x=575, y=y_value)
			y_value = y_value + 20

		self.skin_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.skin_var[len(self.skin_opt)])
		cb.place(x=575, y=y_value)
		y_value = y_value + 20

		self.other_skin = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_skin.place(x=600, y=y_value)


		# tk.Button(form_frame, text="ADD", command=lambda: self.add_details(), height = 2, width = 10, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=875, y=65)

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("review_of_systems_form_2"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=65)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("FirstConsForm"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def add_details(self):
		print("ADDED")
		# self.controller.frames["review_of_systems_form_2"].next_button.config(state="disabled")
		for i in range(len(self.heent_var)):
			if i >= len(self.heent_opt):
				if self.heent_var[i].get() == 1:
					print(self.other_heent.get("1.0",'end-1c')) # get the string on the text field
					self.other_heent.delete('1.0', 'end') # clear the text field
			else:
				if self.heent_var[i].get() == 1:
					print(self.heent_opt[i])
			self.heent_var[i] = tk.IntVar()

		for i in range(len(self.respi_var)):
			if i >= len(self.respi_opt):
				if self.respi_var[i].get() == 1:
					print(self.other_respi.get("1.0",'end-1c')) # get the string on the text field
					self.other_respi.delete('1.0', 'end') # clear the text field
			else:
				if self.respi_var[i].get() == 1:
					print(self.respi_opt[i])
			self.respi_var[i] = tk.IntVar()

		for i in range(len(self.cardio_var)):
			if i >= len(self.cardio_opt):
				if self.cardio_var[i].get() == 1:
					print(self.other_cardio.get("1.0",'end-1c')) # get the string on the text field
					self.other_cardio.delete('1.0', 'end') # clear the text field
			else:
				if self.cardio_var[i].get() == 1:
					print(self.cardio_opt[i])
			self.cardio_var[i] = tk.IntVar()

		for i in range(len(self.gastro_var)):
			if i >= len(self.gastro_opt):
				if self.gastro_var[i].get() == 1:
					print(self.other_gastro.get("1.0",'end-1c')) # get the string on the text field
					self.other_gastro.delete('1.0', 'end') # clear the text field
			else:
				if self.gastro_var[i].get() == 1:
					print(self.gastro_opt[i])
			self.gastro_var[i] = tk.IntVar()

		for i in range(len(self.genito_var)):
			if i >= len(self.genito_opt):
				if self.genito_var[i].get() == 1:
					print(self.other_genito.get("1.0",'end-1c')) # get the string on the text field
					self.other_genito.delete('1.0', 'end') # clear the text field
			else:
				if self.genito_var[i].get() == 1:
					print(self.genito_opt[i])
			self.genito_var[i] = tk.IntVar()

		for i in range(len(self.meta_var)):
			if i >= len(self.meta_opt):
				if self.meta_var[i].get() == 1:
					print(self.other_meta.get("1.0",'end-1c')) # get the string on the text field
					self.other_meta.delete('1.0', 'end') # clear the text field
			else:
				if self.meta_var[i].get() == 1:
					print(self.meta_opt[i])
			self.meta_var[i] = tk.IntVar()

		for i in range(len(self.neuro_var)):
			if i >= len(self.neuro_opt):
				if self.neuro_var[i].get() == 1:
					print(self.other_neuro.get("1.0",'end-1c')) # get the string on the text field
					self.other_neuro.delete('1.0', 'end') # clear the text field
			else:
				if self.neuro_var[i].get() == 1:
					print(self.neuro_opt[i])
			self.neuro_var[i] = tk.IntVar()

		for i in range(len(self.musculo_var)):
			if i >= len(self.musculo_opt):
				if self.musculo_var[i].get() == 1:
					print(self.other_musculo.get("1.0",'end-1c')) # get the string on the text field
					self.other_musculo.delete('1.0', 'end') # clear the text field
			else:
				if self.musculo_var[i].get() == 1:
					print(self.musculo_opt[i])
			self.musculo_var[i] = tk.IntVar()

		for i in range(len(self.skin_var)):
			if i >= len(self.skin_opt):
				if self.skin_var[i].get() == 1:
					print(self.other_skin.get("1.0",'end-1c')) # get the string on the text field
					self.other_skin.delete('1.0', 'end') # clear the text field
			else:
				if self.skin_var[i].get() == 1:
					print(self.skin_opt[i])
			self.skin_var[i] = tk.IntVar()

class review_of_systems_form_2(tk.Frame):

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

		with open("./data/famhistory.txt", 'r') as f:
			self.famhist_opt = f.read().splitlines()
		f.close()

		famhist_label = tk.Label(form_frame, text="Family History: relationship", font=self.label_font_2, fg="#636363")
		famhist_label.place(x=25, y=y_value)
		y_value = y_value + 25

		for i in range(len(self.famhist_opt)):
			self.famhist_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.famhist_opt[i], variable=self.famhist_var[i])
			cb.place(x=25, y=y_value)
			y_value = y_value + 20

		self.famhist_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.famhist_var[len(self.famhist_opt)])
		cb.place(x=25, y=y_value)
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
			self.immunohist_var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text=self.immunohist_opt[i], variable=self.immunohist_var[i])
			cb.place(x=250, y=y_value)
			y_value = y_value + 20

		self.immunohist_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="Boosters:", variable=self.immunohist_var[len(self.immunohist_opt)])
		cb.place(x=250, y=y_value)
		y_value = y_value + 20

		self.other_booster = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_booster.place(x=300, y=y_value)
		y_value = y_value + 30

		self.immunohist_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="Combination:", variable=self.immunohist_var[len(self.immunohist_opt)+1])
		cb.place(x=250, y=y_value)
		y_value = y_value + 20

		self.other_combi = tk.Text(form_frame, height = 1, width = 20, wrap="word")
		self.other_combi.place(x=300, y=y_value)
		y_value = y_value + 30

		self.immunohist_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="others:", variable=self.immunohist_var[len(self.immunohist_opt)+2])
		cb.place(x=250, y=y_value)
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

		self.lob = []
		b = []

		self.smoker_var = 0

		yes_b = tk.Button(form_frame, text="Yes", command=partial(self.set_score, 1, 0), height = 1, width = 4, bd = 1)
		yes_b.place(x=270, y=y_value) 
		no_b = tk.Button(form_frame, text="No", command=partial(self.set_score, -1, 0), height = 1, width = 4, bd = 1)
		no_b.place(x=320, y=y_value)

		b.append(yes_b)
		b.append(no_b)
		self.lob.append(b)
		y_value = y_value + 30

		pack_label = tk.Label(form_frame, text="Pack years?", font=self.label_font, fg="#636363")
		pack_label.place(x=250, y=y_value)
		self.pack_smoke = tk.Text(form_frame, height = 1, width = 5, wrap="word")
		self.pack_smoke.place(x=320, y=y_value)
		y_value = y_value + 30

		quit_cb = tk.Checkbutton(form_frame, text="Quit, when?")
		quit_cb.place(x=250, y=y_value)

		self.quit_cb_text = tk.Text(form_frame, height = 1, width = 10, wrap="word")
		self.quit_cb_text.place(x=360, y=y_value)
		y_value = y_value + 30

		y_value = 25

		alcohol_label = tk.Label(form_frame, text="Alcohol Beverage Drinker?", font=self.label_font, fg="#636363")
		alcohol_label.place(x=475, y=y_value)
		y_value = y_value + 20

		self.alcohol_var = 0

		yes_b = tk.Button(form_frame, text="Yes", command=partial(self.set_score, 1, 1), height = 1, width = 4, bd = 1)
		yes_b.place(x=495, y=y_value) 
		no_b = tk.Button(form_frame, text="No", command=partial(self.set_score, -1, 1), height = 1, width = 4, bd = 1)
		no_b.place(x=545, y=y_value)

		b = []
		b.append(yes_b)
		b.append(no_b)
		self.lob.append(b)
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

		yes_b = tk.Button(form_frame, text="Yes", command=partial(self.set_score, 1, 2), height = 1, width = 4, bd = 1)
		yes_b.place(x=495, y=y_value) 
		no_b = tk.Button(form_frame, text="No", command=partial(self.set_score, -1, 2), height = 1, width = 4, bd = 1)
		no_b.place(x=545, y=y_value)

		b = []
		b.append(yes_b)
		b.append(no_b)
		self.lob.append(b)
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

		tk.Button(form_frame, text="ADD", command=lambda: self.add_details(), height = 2, width = 10, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=875, y=65)
		# add selected details from checkboxes
		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("review_of_systems_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def add_details(self):
		print("ADDED")

		print(self.medhist_illness.get("1.0",'end-1c')) # get the string on the text field
		self.medhist_illness.delete('1.0', 'end') # clear the text field

		print(self.medhist_hospt.get("1.0",'end-1c')) # get the string on the text field
		self.medhist_hospt.delete('1.0', 'end') # clear the text field

		print(self.medhist_allergy.get("1.0",'end-1c')) # get the string on the text field
		self.medhist_allergy.delete('1.0', 'end') # clear the text field

		############### get details for family history
		for i in range(len(self.famhist_var)):
			if i >= len(self.famhist_opt):
				if self.famhist_var[i].get() == 1:
					print(self.other_famhist.get("1.0",'end-1c')) # get the string on the text field
					self.other_famhist.delete('1.0', 'end') # clear the text field
			else:
				if self.famhist_var[i].get() == 1:
					print(self.famhist_opt[i])
			self.famhist_var[i] = tk.IntVar()

			############### get details for immunization history
		for i in range(len(self.immunohist_var)):
			if i >= len(self.immunohist_opt):
				if i == len(self.immunohist_opt):
					if self.immunohist_var[i].get() == 1:
						print(self.other_booster.get("1.0",'end-1c'))
						self.other_booster.delete('1.0', 'end')
				elif i == len(self.immunohist_opt)+1:
					if self.immunohist_var[i].get() == 1:
						print(self.other_combi.get("1.0",'end-1c'))
						self.other_combi.delete('1.0', 'end')
				elif i == len(self.immunohist_opt)+2:
					if self.immunohist_var[i].get() == 1:
						print(self.other_immunohist.get("1.0",'end-1c'))
						self.other_immunohist.delete('1.0', 'end')
			else:
				if self.immunohist_var[i].get() == 1:
					print(self.immunohist_opt[i])
			self.immunohist_var[i] = tk.IntVar()

		print(self.pack_smoke.get("1.0",'end-1c')) # get the string on the text field
		self.pack_smoke.delete('1.0', 'end') # clear the text field

		print(self.quit_cb_text.get("1.0",'end-1c')) # get the string on the text field
		self.quit_cb_text.delete('1.0', 'end') # clear the text field

		print(self.alco_freq.get("1.0",'end-1c')) # get the string on the text field
		self.alco_freq.delete('1.0', 'end') # clear the text field

		print(self.alco_dur.get("1.0",'end-1c')) # get the string on the text field
		self.alco_dur.delete('1.0', 'end') # clear the text field

		print(self.alco_type.get("1.0",'end-1c')) # get the string on the text field
		self.alco_type.delete('1.0', 'end') # clear the text field

		print(self.exercise_type.get("1.0",'end-1c')) # get the string on the text field
		self.exercise_type.delete('1.0', 'end') # clear the text field

		print(self.g_type.get("1.0",'end-1c')) # get the string on the text field
		self.g_type.delete('1.0', 'end') # clear the text field

		print(self.p_type.get("1.0",'end-1c')) # get the string on the text field
		self.p_type.delete('1.0', 'end') # clear the text field

		print(self.menarche.get("1.0",'end-1c')) # get the string on the text field
		self.menarche.delete('1.0', 'end') # clear the text field

		print(self.menopause.get("1.0",'end-1c')) # get the string on the text field
		self.menopause.delete('1.0', 'end') # clear the text field

		print(self.coitus.get("1.0",'end-1c')) # get the string on the text field
		self.coitus.delete('1.0', 'end') # clear the text field

		print(self.born.get("1.0",'end-1c')) # get the string on the text field
		self.born.delete('1.0', 'end') # clear the text field

		print(self.via.get("1.0",'end-1c')) # get the string on the text field
		self.via.delete('1.0', 'end') # clear the text field

		print(self.to_a_g.get("1.0",'end-1c')) # get the string on the text field
		self.to_a_g.delete('1.0', 'end') # clear the text field

		print(self.bm_p.get("1.0",'end-1c')) # get the string on the text field
		self.bm_p.delete('1.0', 'end') # clear the text field

		print(self.bm_year.get("1.0",'end-1c')) # get the string on the text field
		self.bm_year.delete('1.0', 'end') # clear the text field

		print(self.mb_compli.get("1.0",'end-1c')) # get the string on the text field
		self.mb_compli.delete('1.0', 'end') # clear the text field
		

	def set_score(self, vote, i):
		if vote == 1:
			(self.lob[i][1]).config(state = "disabled", bd = 0)
			(self.lob[i][0]).config(bg = "#0060ba", fg = "#ffffff")
		else:
			(self.lob[i][0]).config(state = "disabled", bd = 0)
			(self.lob[i][1]).config(bg = "#0060ba", fg = "#ffffff")
		
		if i == 0:
			if vote == 1:
				self.smoker_var = 1
			else:
				self.smoker_var = 0
		elif i == 1:
			if vote == 1:
				self.alcohol_var = 1
			else:
				self.alcohol_var = 0
		else:
			if vote == 1:
				self.exercise_var = 1
			else:
				self.exercise_var = 0

class physical_examination_form(tk.Frame):

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
		bp_label.place(x=225, y=y_value)

		self.bp = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.bp.place(x=250, y=y_value)

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

		self.ge_var = []
		self.ge_cb = []
		self.ge_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ge_var[0])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)
		y_value = y_value + 25

		self.ge_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ge_var[1])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)

		self.ge_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ge_find.place(x=225, y=y_value)

		self.ge_cb[0].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 0))
		self.ge_cb[1].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 1))

		y_value = y_value + 25
		sk_label = tk.Label(form_frame, text="Skin/Integument:", font=self.label_font_2, fg="#636363")
		sk_label.place(x=25, y=y_value)

		self.sk_var = []
		self.sk_cb = []
		self.sk_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.sk_var[0])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)
		y_value = y_value + 25

		self.sk_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.sk_var[1])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)

		self.sk_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.sk_find.place(x=225, y=y_value)

		self.sk_cb[0].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 0))
		self.sk_cb[1].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 1))

		y_value = y_value + 25
		mu_label = tk.Label(form_frame, text="Musculoskeletal:", font=self.label_font_2, fg="#636363")
		mu_label.place(x=25, y=y_value)

		self.mu_var = []
		self.mu_cb = []
		self.mu_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.mu_var[0])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)
		y_value = y_value + 25

		self.mu_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.mu_var[1])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)

		self.mu_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.mu_find.place(x=225, y=y_value)

		self.mu_cb[0].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 0))
		self.mu_cb[1].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 1))

		y_value = y_value + 25
		he_label = tk.Label(form_frame, text="HEENT:", font=self.label_font_2, fg="#636363")
		he_label.place(x=25, y=y_value)

		self.he_var = []
		self.he_cb = []
		self.he_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.he_var[0])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)
		y_value = y_value + 25

		self.he_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.he_var[1])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)

		self.he_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.he_find.place(x=225, y=y_value)

		self.he_cb[0].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 0))
		self.he_cb[1].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 1))

		y_value = y_value + 25
		re_label = tk.Label(form_frame, text="Respiratory:", font=self.label_font_2, fg="#636363")
		re_label.place(x=25, y=y_value)

		self.re_var = []
		self.re_cb = []
		self.re_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.re_var[0])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)
		y_value = y_value + 25

		self.re_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.re_var[1])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)

		self.re_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.re_find.place(x=225, y=y_value)

		self.re_cb[0].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 0))
		self.re_cb[1].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 1))

		y_value = y_value + 25
		ca_label = tk.Label(form_frame, text="Cardiovascular:", font=self.label_font_2, fg="#636363")
		ca_label.place(x=25, y=y_value)

		self.ca_var = []
		self.ca_cb = []
		self.ca_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ca_var[0])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)
		y_value = y_value + 25

		self.ca_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ca_var[1])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)

		self.ca_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ca_find.place(x=225, y=y_value)

		self.ca_cb[0].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 0))
		self.ca_cb[1].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 1))

		y_value = y_value + 25
		ga_label = tk.Label(form_frame, text="Gastrointestinal:", font=self.label_font_2, fg="#636363")
		ga_label.place(x=25, y=y_value)

		self.ga_var = []
		self.ga_cb = []
		self.ga_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ga_var[0])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)
		y_value = y_value + 25

		self.ga_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ga_var[1])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)

		self.ga_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ga_find.place(x=225, y=y_value)

		self.ga_cb[0].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 0))
		self.ga_cb[1].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 1))

		y_value = y_value + 25
		gn_label = tk.Label(form_frame, text="Genitourinary:", font=self.label_font_2, fg="#636363")
		gn_label.place(x=25, y=y_value)

		self.gn_var = []
		self.gn_cb = []
		self.gn_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.gn_var[0])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)
		y_value = y_value + 25

		self.gn_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.gn_var[1])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)

		self.gn_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.gn_find.place(x=225, y=y_value)

		self.gn_cb[0].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 0))
		self.gn_cb[1].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 1))

		y_value = y_value + 25
		ie_label = tk.Label(form_frame, text="IE:", font=self.label_font_2, fg="#636363")
		ie_label.place(x=25, y=y_value)

		self.ie_var = []
		self.ie_cb = []
		self.ie_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ie_var[0])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)
		y_value = y_value + 25

		self.ie_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ie_var[1])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)

		self.ie_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ie_find.place(x=225, y=y_value)

		self.ie_cb[0].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 0))
		self.ie_cb[1].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 1))

		y_value = y_value + 25
		dre_label = tk.Label(form_frame, text="DRE:", font=self.label_font_2, fg="#636363")
		dre_label.place(x=25, y=y_value)

		self.dre_var = []
		self.dre_cb = []
		self.dre_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.dre_var[0])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)
		y_value = y_value + 25

		self.dre_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.dre_var[1])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)

		self.dre_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.dre_find.place(x=225, y=y_value)

		self.dre_cb[0].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 0))
		self.dre_cb[1].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 1))

		y_value = y_value + 25
		ne_label = tk.Label(form_frame, text="Neuropsych:", font=self.label_font_2, fg="#636363")
		ne_label.place(x=25, y=y_value)

		self.ne_var = []
		self.ne_cb = []
		self.ne_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ne_var[0])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)
		y_value = y_value + 25

		self.ne_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ne_var[1])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)

		self.ne_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ne_find.place(x=225, y=y_value)

		self.ne_cb[0].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 0))
		self.ne_cb[1].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 1))

		y_value = y_value + 25

		# tk.Button(form_frame, text="ADD", command=lambda: self.add_details(), height = 2, width = 10, bd = 0, bg = "#259400", fg = "#ffffff", activebackground = "#cf0007").place(x=875, y=65)
		# add selected details from checkboxes
		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("assessment_table"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

		tk.Label(form_frame, text="*BMI weight in kg height in meters squared or weight in lbs x 705 inches", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=200)
		tk.Label(form_frame, text="**IBW quick estimate:", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=280)
		tk.Label(form_frame, text="for females 105 lbs for first 5 feet+ 5 lbs for every inch above five feet, for males 106 lbs for first 5 feet and 5 lbs for every inch above five feet", font=self.notes_font, fg="#636363", width = 15, wraplength = 100).place(x=865, y=325)

	def check_cb(self, cb_arr, cb_var_arr, textfield, i):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				cb_arr[i+1].config(state="disabled")
				textfield.config(state="disabled")
			else:
				cb_arr[i+1].config(state="normal")
				textfield.config(state="normal")
		else:
			if cb_var_arr[i].get() == 1:
				cb_arr[i-1].config(state="disabled")
				textfield.config(state="normal")
			else:
				cb_arr[i-1].config(state="normal")
				textfield.config(state="disabled")

	def add_details(self):
		print("ADDED")

		print(self.ge_find.get("1.0",'end-1c')) # get the string on the text field
		self.ge_find.delete('1.0', 'end') # clear the text field

		print(self.sk_find.get("1.0",'end-1c')) # get the string on the text field
		self.sk_find.delete('1.0', 'end') # clear the text field

		print(self.mu_find.get("1.0",'end-1c')) # get the string on the text field
		self.mu_find.delete('1.0', 'end') # clear the text field

		print(self.he_find.get("1.0",'end-1c')) # get the string on the text field
		self.he_find.delete('1.0', 'end') # clear the text field

		print(self.re_find.get("1.0",'end-1c')) # get the string on the text field
		self.re_find.delete('1.0', 'end') # clear the text field

		print(self.ca_find.get("1.0",'end-1c')) # get the string on the text field
		self.ca_find.delete('1.0', 'end') # clear the text field

		print(self.ga_find.get("1.0",'end-1c')) # get the string on the text field
		self.ga_find.delete('1.0', 'end') # clear the text field

		print(self.gn_find.get("1.0",'end-1c')) # get the string on the text field
		self.gn_find.delete('1.0', 'end') # clear the text field

		print(self.ie_find.get("1.0",'end-1c')) # get the string on the text field
		self.ie_find.delete('1.0', 'end') # clear the text field

		print(self.dre_find.get("1.0",'end-1c')) # get the string on the text field
		self.dre_find.delete('1.0', 'end') # clear the text field

		print(self.ne_find.get("1.0",'end-1c')) # get the string on the text field
		self.ne_find.delete('1.0', 'end') # clear the text field

class assessment_table(tk.Frame):

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

		self.strat_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="Advice", variable=self.strat_var[0])
		cb.place(x=695, y=205)

		self.strat_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="Flyers/pamphlets", variable=self.strat_var[1])
		cb.place(x=695, y=225)

		self.strat_var.append(tk.IntVar())
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
		## include physical examination details

		print(self.drugs.get("1.0",'end-1c')) # get the string on the text field
		self.drugs.delete('1.0', 'end') # clear the text field

		print(self.diet.get("1.0",'end-1c')) # get the string on the text field
		self.diet.delete('1.0', 'end') # clear the text field

		print(self.lifestyle.get("1.0",'end-1c')) # get the string on the text field
		self.lifestyle.delete('1.0', 'end') # clear the text field

		print(self.exer.get("1.0",'end-1c')) # get the string on the text field
		self.exer.delete('1.0', 'end') # clear the text field

		print(self.referral.get("1.0",'end-1c')) # get the string on the text field
		self.referral.delete('1.0', 'end') # clear the text field

		print(self.follow_up.get("1.0",'end-1c')) # get the string on the text field
		self.follow_up.delete('1.0', 'end') # clear the text field

		if self.strat_var[0].get() == 1:
			print("Advice")
			self.strat_var[0] = tk.IntVar()

		if self.strat_var[1].get() == 1:
			print("Flyers/pamphlets")
			self.strat_var[1] = tk.IntVar()

		if self.strat_var[2].get() == 1:
			print(self.health_strat_others.get("1.0",'end-1c')) # get the string on the text field
			self.health_strat_others.delete('1.0', 'end')
			self.strat_var[2] = tk.IntVar()

	def add_to_table(self, assessment, icd, dpra):
		id = self.tree.insert('', 'end', text="Assessment: " + assessment)
		sub_id_1 = self.tree.insert(id, 'end', text="ICD Code")
		self.tree.insert(sub_id_1, 'end', text=icd)
		sub_id_2 = self.tree.insert(id, 'end', text="Diagnostic/Prognostic Risk Assessments")
		self.tree.insert(sub_id_2, 'end', text=dpra)

class family_apgar_form(tk.Frame):

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

		for i in range(0, len(apgar_questions), 2):
			cLabelFrame = tk.Frame(form_frame)
			cLabelFrame.place(x=90, y=y_value)

			tk.Label(cLabelFrame, text=apgar_questions[i], font=self.label_font, wraplength=350, justify="left").grid(row=0, column=0, sticky="w")
			tk.Label(cLabelFrame, text=apgar_questions[i+1], font=self.label_font2, wraplength=350, justify="left").grid(row=1, column=0, sticky="w")

			var = []
			cb_arr = []
			var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text="0", variable=var[0])
			cb.place(x=480, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text="1", variable=var[1])
			cb.place(x=520, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text="2", variable=var[2])
			cb.place(x=560, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text="0", variable=var[3])
			cb.place(x=620, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar())
			cb = tk.Checkbutton(form_frame, text="1", variable=var[4])
			cb.place(x=660, y=y_value)
			cb_arr.append(cb)

			var.append(tk.IntVar())
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


	def check_cb(self, cb_arr, cb_var_arr, i, average, index): # will not add a button, must update database with every data change
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
			avg_value = (self.vote_1_arr[i] + self.vote_2_arr[i]) / 2
			self.average[i]['text'] = str(avg_value)
			self.avg_vote[i] = avg_value

		avg_value = 0
		for i in range(len(self.avg_vote)):
			avg_value = avg_value + self.avg_vote[i]

		if avg_value <= 3:
			self.overall_avg_txt['text'] = str(avg_value) +" - Severely dysfunctional" 
		elif avg_value <= 6:
			self.overall_avg_txt['text'] = str(avg_value) + " - Moderately dysfunctional" 
		else:
			self.overall_avg_txt['text'] = str(avg_value) + " - Highly functional"


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

class followup_patient_form(tk.Frame):

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

		self.p_name = tk.Label(form_frame, text="<insert patient name here>", font=self.label_font_3)
		self.p_name.place(x=140, y=50)

		f_date_label = tk.Label(form_frame, text="Date of Follow-up: ", font=self.label_font_2)
		f_date_label.place(x=90, y=80)

		self.f_date_input = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd") # working
		self.f_date_input.place(x=200, y=80)

		f_reasons_label = tk.Label(form_frame, text="Reasons for Follow-up: ", font=self.label_font_2)
		f_reasons_label.place(x=90, y=110)

		self.r_var = []
		self.r_cb_arr = []
		self.r_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="continuing care from previous visit", variable=self.r_var[0])
		cb.place(x=230, y=110)
		self.r_cb_arr.append(cb)

		self.r_var.append(tk.IntVar())
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

		# self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("FirstConsForm"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		# self.next_button.place(x=875, y=25)

	def check_cb(self, cb_arr, cb_var_arr, i):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				cb_arr[i+1].config(state="disabled")
			else:
				cb_arr[i+1].config(state="normal")
		else:
			if cb_var_arr[i].get() == 1:
				cb_arr[i-1].config(state="disabled")
			else:
				cb_arr[i-1].config(state="normal")

	def add_details(self):
		print(self.r_date_input.get_date())
		print(self.f_s.get('1.0', 'end-1c'))
		print(self.f_medication.get('1.0', 'end-1c'))

class followup_patient_form_2(tk.Frame):

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

		pe_label = tk.Label(form_frame, text="O:", font=self.label_font_2, fg="#636363")
		pe_label.place(x=25, y=y_value)

		hr_label = tk.Label(form_frame, text="HR:", font=self.label_font, fg="#636363")
		hr_label.place(x=150, y=y_value)

		self.hr = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.hr.place(x=175, y=y_value)

		bp_label = tk.Label(form_frame, text="BP:", font=self.label_font, fg="#636363")
		bp_label.place(x=225, y=y_value)

		self.bp = tk.Text(form_frame, height = 1, width = 4, wrap="word")
		self.bp.place(x=250, y=y_value)

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

		self.ge_var = []
		self.ge_cb = []
		self.ge_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ge_var[0])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)
		y_value = y_value + 25

		self.ge_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ge_var[1])
		cb.place(x=150, y=y_value)
		self.ge_cb.append(cb)

		self.ge_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ge_find.place(x=225, y=y_value)

		self.ge_cb[0].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 0))
		self.ge_cb[1].config(command=partial(self.check_cb, self.ge_cb, self.ge_var, self.ge_find, 1))

		y_value = y_value + 25
		sk_label = tk.Label(form_frame, text="Skin/Integument:", font=self.label_font_2, fg="#636363")
		sk_label.place(x=25, y=y_value)

		self.sk_var = []
		self.sk_cb = []
		self.sk_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.sk_var[0])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)
		y_value = y_value + 25

		self.sk_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.sk_var[1])
		cb.place(x=150, y=y_value)
		self.sk_cb.append(cb)

		self.sk_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.sk_find.place(x=225, y=y_value)

		self.sk_cb[0].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 0))
		self.sk_cb[1].config(command=partial(self.check_cb, self.sk_cb, self.sk_var, self.sk_find, 1))

		y_value = y_value + 25
		mu_label = tk.Label(form_frame, text="Musculoskeletal:", font=self.label_font_2, fg="#636363")
		mu_label.place(x=25, y=y_value)

		self.mu_var = []
		self.mu_cb = []
		self.mu_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.mu_var[0])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)
		y_value = y_value + 25

		self.mu_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.mu_var[1])
		cb.place(x=150, y=y_value)
		self.mu_cb.append(cb)

		self.mu_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.mu_find.place(x=225, y=y_value)

		self.mu_cb[0].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 0))
		self.mu_cb[1].config(command=partial(self.check_cb, self.mu_cb, self.mu_var, self.mu_find, 1))

		y_value = y_value + 25
		he_label = tk.Label(form_frame, text="HEENT:", font=self.label_font_2, fg="#636363")
		he_label.place(x=25, y=y_value)

		self.he_var = []
		self.he_cb = []
		self.he_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.he_var[0])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)
		y_value = y_value + 25

		self.he_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.he_var[1])
		cb.place(x=150, y=y_value)
		self.he_cb.append(cb)

		self.he_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.he_find.place(x=225, y=y_value)

		self.he_cb[0].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 0))
		self.he_cb[1].config(command=partial(self.check_cb, self.he_cb, self.he_var, self.he_find, 1))

		y_value = y_value + 25
		re_label = tk.Label(form_frame, text="Respiratory:", font=self.label_font_2, fg="#636363")
		re_label.place(x=25, y=y_value)

		self.re_var = []
		self.re_cb = []
		self.re_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.re_var[0])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)
		y_value = y_value + 25

		self.re_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.re_var[1])
		cb.place(x=150, y=y_value)
		self.re_cb.append(cb)

		self.re_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.re_find.place(x=225, y=y_value)

		self.re_cb[0].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 0))
		self.re_cb[1].config(command=partial(self.check_cb, self.re_cb, self.re_var, self.re_find, 1))

		y_value = y_value + 25
		ca_label = tk.Label(form_frame, text="Cardiovascular:", font=self.label_font_2, fg="#636363")
		ca_label.place(x=25, y=y_value)

		self.ca_var = []
		self.ca_cb = []
		self.ca_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ca_var[0])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)
		y_value = y_value + 25

		self.ca_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ca_var[1])
		cb.place(x=150, y=y_value)
		self.ca_cb.append(cb)

		self.ca_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ca_find.place(x=225, y=y_value)

		self.ca_cb[0].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 0))
		self.ca_cb[1].config(command=partial(self.check_cb, self.ca_cb, self.ca_var, self.ca_find, 1))

		y_value = y_value + 25
		ga_label = tk.Label(form_frame, text="Gastrointestinal:", font=self.label_font_2, fg="#636363")
		ga_label.place(x=25, y=y_value)

		self.ga_var = []
		self.ga_cb = []
		self.ga_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ga_var[0])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)
		y_value = y_value + 25

		self.ga_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ga_var[1])
		cb.place(x=150, y=y_value)
		self.ga_cb.append(cb)

		self.ga_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ga_find.place(x=225, y=y_value)

		self.ga_cb[0].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 0))
		self.ga_cb[1].config(command=partial(self.check_cb, self.ga_cb, self.ga_var, self.ga_find, 1))

		y_value = y_value + 25
		gn_label = tk.Label(form_frame, text="Genitourinary:", font=self.label_font_2, fg="#636363")
		gn_label.place(x=25, y=y_value)

		self.gn_var = []
		self.gn_cb = []
		self.gn_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.gn_var[0])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)
		y_value = y_value + 25

		self.gn_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.gn_var[1])
		cb.place(x=150, y=y_value)
		self.gn_cb.append(cb)

		self.gn_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.gn_find.place(x=225, y=y_value)

		self.gn_cb[0].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 0))
		self.gn_cb[1].config(command=partial(self.check_cb, self.gn_cb, self.gn_var, self.gn_find, 1))

		y_value = y_value + 25
		ie_label = tk.Label(form_frame, text="IE:", font=self.label_font_2, fg="#636363")
		ie_label.place(x=25, y=y_value)

		self.ie_var = []
		self.ie_cb = []
		self.ie_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ie_var[0])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)
		y_value = y_value + 25

		self.ie_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ie_var[1])
		cb.place(x=150, y=y_value)
		self.ie_cb.append(cb)

		self.ie_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ie_find.place(x=225, y=y_value)

		self.ie_cb[0].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 0))
		self.ie_cb[1].config(command=partial(self.check_cb, self.ie_cb, self.ie_var, self.ie_find, 1))

		y_value = y_value + 25
		dre_label = tk.Label(form_frame, text="DRE:", font=self.label_font_2, fg="#636363")
		dre_label.place(x=25, y=y_value)

		self.dre_var = []
		self.dre_cb = []
		self.dre_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.dre_var[0])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)
		y_value = y_value + 25

		self.dre_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.dre_var[1])
		cb.place(x=150, y=y_value)
		self.dre_cb.append(cb)

		self.dre_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.dre_find.place(x=225, y=y_value)

		self.dre_cb[0].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 0))
		self.dre_cb[1].config(command=partial(self.check_cb, self.dre_cb, self.dre_var, self.dre_find, 1))

		y_value = y_value + 25
		ne_label = tk.Label(form_frame, text="Neuropsych:", font=self.label_font_2, fg="#636363")
		ne_label.place(x=25, y=y_value)

		self.ne_var = []
		self.ne_cb = []
		self.ne_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="no significant findings", variable=self.ne_var[0])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)
		y_value = y_value + 25

		self.ne_var.append(tk.IntVar())
		cb = tk.Checkbutton(form_frame, text="findings:", variable=self.ne_var[1])
		cb.place(x=150, y=y_value)
		self.ne_cb.append(cb)

		self.ne_find = tk.Text(form_frame, height = 1, width = 75, wrap="word")
		self.ne_find.place(x=225, y=y_value)

		self.ne_cb[0].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 0))
		self.ne_cb[1].config(command=partial(self.check_cb, self.ne_cb, self.ne_var, self.ne_find, 1))

		self.next_button = tk.Button(form_frame, text="Next Page", command=lambda: controller.show_frame("followup_assessment_table"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=65)

		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("followup_patient_form"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)

	def check_cb(self, cb_arr, cb_var_arr, textfield, i):
		if i == 0:
			if cb_var_arr[i].get() == 1:
				cb_arr[i+1].config(state="disabled")
				textfield.config(state="disabled")
			else:
				cb_arr[i+1].config(state="normal")
				textfield.config(state="normal")
		else:
			if cb_var_arr[i].get() == 1:
				cb_arr[i-1].config(state="disabled")
				textfield.config(state="normal")
			else:
				cb_arr[i-1].config(state="normal")
				textfield.config(state="disabled")

	def add_details(self):
		print("ADDED")

		print(self.ge_find.get("1.0",'end-1c')) # get the string on the text field
		self.ge_find.delete('1.0', 'end') # clear the text field

		print(self.sk_find.get("1.0",'end-1c')) # get the string on the text field
		self.sk_find.delete('1.0', 'end') # clear the text field

		print(self.mu_find.get("1.0",'end-1c')) # get the string on the text field
		self.mu_find.delete('1.0', 'end') # clear the text field

		print(self.he_find.get("1.0",'end-1c')) # get the string on the text field
		self.he_find.delete('1.0', 'end') # clear the text field

		print(self.re_find.get("1.0",'end-1c')) # get the string on the text field
		self.re_find.delete('1.0', 'end') # clear the text field

		print(self.ca_find.get("1.0",'end-1c')) # get the string on the text field
		self.ca_find.delete('1.0', 'end') # clear the text field

		print(self.ga_find.get("1.0",'end-1c')) # get the string on the text field
		self.ga_find.delete('1.0', 'end') # clear the text field

		print(self.gn_find.get("1.0",'end-1c')) # get the string on the text field
		self.gn_find.delete('1.0', 'end') # clear the text field

		print(self.ie_find.get("1.0",'end-1c')) # get the string on the text field
		self.ie_find.delete('1.0', 'end') # clear the text field

		print(self.dre_find.get("1.0",'end-1c')) # get the string on the text field
		self.dre_find.delete('1.0', 'end') # clear the text field

		print(self.ne_find.get("1.0",'end-1c')) # get the string on the text field
		self.ne_find.delete('1.0', 'end') # clear the text field

class followup_assessment_table(tk.Frame):

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

		# add selected details from checkboxes
		self.next_button = tk.Button(form_frame, text="Prev Page", command=lambda: controller.show_frame("followup_patient_form_2"), height = 2, width = 10, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007")
		self.next_button.place(x=875, y=25)


	def add_follow_up(self):
		## include physical examination details

		print(self.drugs.get("1.0",'end-1c')) # get the string on the text field
		self.drugs.delete('1.0', 'end') # clear the text field

		print(self.diet.get("1.0",'end-1c')) # get the string on the text field
		self.diet.delete('1.0', 'end') # clear the text field

		print(self.lifestyle.get("1.0",'end-1c')) # get the string on the text field
		self.lifestyle.delete('1.0', 'end') # clear the text field

		print(self.exer.get("1.0",'end-1c')) # get the string on the text field
		self.exer.delete('1.0', 'end') # clear the text field

		print(self.referral.get("1.0",'end-1c')) # get the string on the text field
		self.referral.delete('1.0', 'end') # clear the text field

		print(self.follow_up.get("1.0",'end-1c')) # get the string on the text field
		self.follow_up.delete('1.0', 'end') # clear the text field

		if self.strat_var[0].get() == 1:
			print("Advice")
			self.strat_var[0] = tk.IntVar()

		if self.strat_var[1].get() == 1:
			print("Flyers/pamphlets")
			self.strat_var[1] = tk.IntVar()

		if self.strat_var[2].get() == 1:
			print(self.health_strat_others.get("1.0",'end-1c')) # get the string on the text field
			self.health_strat_others.delete('1.0', 'end')
			self.strat_var[2] = tk.IntVar()

	def add_to_table(self, assessment, icd, dpra):
		id = self.tree.insert('', 'end', text="Assessment: " + assessment)
		sub_id_1 = self.tree.insert(id, 'end', text="ICD Code")
		self.tree.insert(sub_id_1, 'end', text=icd)
		sub_id_2 = self.tree.insert(id, 'end', text="Diagnostic/Prognostic Risk Assessments")
		self.tree.insert(sub_id_2, 'end', text=dpra)

class ReferralForm(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 5)
		submenu_buttons_3(self, self.controller, 2)

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

		self.r_date_input = DateEntry(form_frame, style = "my.DateEntry", locale = "en_US", date_pattern = "yyyy/mm/dd") # working
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

		tk.Button(form_frame, text="Add Referral", command=lambda: self.add_referral(self.r_date_input.get_date(), self.referring_phys.get("1.0",'end-1c'), self.phys_referred.get("1.0",'end-1c'), self.r_referral.get("1.0",'end-1c')), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=770, y=115)
		tk.Label(form_frame, text="________"*17, font=self.label_font, fg="#636363").place(x=90, y=220)

		page_subtitle_2 = tk.Label(form_frame, text="Clinical Summary", font=self.title_font)
		page_subtitle_2.place(x=400, y=225)

		p_name_label = tk.Label(form_frame, text="Name of Patient:", font=self.label_font_2)
		p_name_label.place(x=90, y=255)
		self.p_name = tk.Label(form_frame, text="<insert patient name here>", font=self.label_font)
		self.p_name.place(x=200, y=255)

		p_agegender_label = tk.Label(form_frame, text="Age/Gender:", font=self.label_font_2)
		p_agegender_label.place(x=90, y=275)
		self.p_agegender = tk.Label(form_frame, text="<insert patient age and gender here>", font=self.label_font)
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

		tk.Button(form_frame, text="Add Summary", command=lambda: self.add_summary(self.p_name['text'], self.p_agegender['text'], self.p_working_impre.get("1.0",'end-1c'), self.p_brief_hist.get("1.0",'end-1c'), self.p_summ_lab.get("1.0",'end-1c'), self.p_summ_med.get("1.0",'end-1c')), height = 2, width = 16, bd = 0, bg = "#0060ba", fg = "#ffffff", activebackground = "#cf0007").place(x=770, y=415)

	def add_referral(self, date, referring_phys, phys_referred, reason):
		print(date)
		print(referring_phys)
		print(phys_referred)
		print(reason)
		self.referring_phys.delete('1.0', 'end')
		self.phys_referred.delete('1.0', 'end')
		self.r_referral.delete('1.0', 'end')

	def add_summary(self, name, agegender, working_impre, brief_hist, summ_lab, summ_med):
		print(name)
		print(agegender)
		print(working_impre)
		print(brief_hist)
		print(summ_lab)
		print(summ_med)
		self.p_working_impre.delete('1.0', 'end')
		self.p_brief_hist.delete('1.0', 'end')
		self.p_summ_lab.delete('1.0', 'end')
		self.p_summ_med.delete('1.0', 'end')

if __name__ == "__main__":
	app = SampleApp()
	app.title("Family Oriented Medical Record")
	app.geometry("1200x700")
	app.resizable(width=False, height=False)
	app.mainloop()