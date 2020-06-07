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

class GeriatricForm(tk.Frame): # Form for Geriatric Depression Scale 

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 2)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.subtitle_font = tkfont.Font(family='Helvetica', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=10)

		page_title = tk.Label(self, text="Geriatric Depression Scale – Short Form", font=self.title_font)
		page_title.place(x=460, y=68)

		self.patient_name_label = tk.Label(self, text="", font=self.title_font)
		self.patient_name_label.place(x=90, y=110)

		question_label = tk.Label(self, text="Question", font=self.subtitle_font)
		question_label.place(x=190, y=145)
		score_label = tk.Label(self, text="SCORE", font=self.subtitle_font)
		score_label.place(x=970, y=145)

		#  form starts here
		
		with open("./data/geriatic_questions.txt", 'r') as f:
			self.questions = f.read().splitlines()
		f.close()

		y_value = 175
		self.score = 0
		self.list_of_scores = []
		self.lob = []
		self.losl = []
		for i in range(len(self.questions)):
			b = []
			question_label = tk.Label(self, text=str(i + 1) + ".) " + self.questions[i], font=self.label_font)
			question_label.place(x=90, y=y_value)

			yes_b = tk.Button(self, text="Yes", command=partial(self.set_score, 1,i), height = 1, width = 5, bd = 1)
			yes_b.place(x=690, y=y_value) 
			no_b = tk.Button(self, text="No", command=partial(self.set_score, -1,i), height = 1, width = 5, bd = 1)
			no_b.place(x=790, y=y_value)
			score_label = tk.Label(self, text="", font=self.label_font)
			score_label.place(x=940, y=y_value)

			b.append(yes_b)
			b.append(no_b)
			self.list_of_scores.append(0)
			self.lob.append(b)
			self.losl.append(score_label)

			y_value = y_value + 30

		self.total_score = tk.Label(self, text="Total: ", font=self.subtitle_font)
		self.total_score.place(x=940, y=635)
		self.total_score_value = tk.Label(self, text="", font=self.label_font)
		self.total_score_value.place(x=980, y=635)

		self.sub_bttn = tk.Button(self, text="Submit", command=lambda: self.submit(), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.sub_bttn.place(x=90, y=635)

		self.res_bttn = tk.Button(self, text="Show Results", command=lambda: controller.show_frame("GeriatricFormRes"), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.res_bttn.place(x=90, y=660)
		self.res_bttn.config(state = "disabled")

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT last_name, first_name, middle_name FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.patient_name_label['text'] = res[0] + ", " + res[1] + " " + res[2]
		else:
			self.patient_name_label['text'] = ""

		cur.execute(("SELECT depression_score FROM patientdepressionscale WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			self.res_bttn.config(state = "disabled")
		else:
			self.res_bttn.config(state = "normal")

		for i in range(15):
			self.list_of_scores[i] = 0
			self.score = 0
			self.losl[i]['text'] = "" 

		self.score = 0
		for i in range(len(self.questions)):
			(self.lob[i][1]).config(state = "normal", bg = "SystemButtonFace", fg = "#000000", bd = 1)
			(self.lob[i][0]).config(state = "normal", bg = "SystemButtonFace", fg = "#000000", bd = 1)
			self.losl[i]['text'] = ""
			self.total_score_value['text'] = ""

	def set_score(self, vote, i):
		self.score = self.score + vote
		if vote == 1:
			(self.lob[i][1]).config(state = "disabled", bd = 0)
			(self.lob[i][0]).config(bg = "#0060ba", fg = "#ffffff")
			self.losl[i]['text'] = "Score 1 point for yes" 
			self.list_of_scores[i] = 1
		else:
			(self.lob[i][0]).config(state = "disabled", bd = 0)
			(self.lob[i][1]).config(bg = "#0060ba", fg = "#ffffff")
			self.losl[i]['text'] = "Score 1 point for no"
			self.list_of_scores[i] = 0
		if self.score >= 0:
			self.total_score_value['text'] = str(self.score) 

	def submit(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT depression_score FROM patientdepressionscale WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()
		if res is None:
			cur.execute(("INSERT INTO patientdepressionscale (q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15, depression_score, patient_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"), 
				(self.list_of_scores[0], self.list_of_scores[1], self.list_of_scores[2], self.list_of_scores[3], self.list_of_scores[4], self.list_of_scores[5], 
					self.list_of_scores[6], self.list_of_scores[7], self.list_of_scores[8], self.list_of_scores[9], self.list_of_scores[10], self.list_of_scores[11], 
					self.list_of_scores[12], self.list_of_scores[13], self.list_of_scores[14], int(self.score), self.controller.patient_id.get()))
			mydb.commit()
		else:
			cur.execute(("UPDATE patientdepressionscale SET q_1 = %s, q_2 = %s, q_3 = %s, q_4 = %s, q_5 = %s, q_6 = %s, q_7 = %s, q_8 = %s, q_9 = %s, q_10 = %s, q_11 = %s, q_12 = %s, q_13 = %s, q_14 = %s, q_15 = %s, depression_score = %s WHERE patient_id = %s"), 
				(self.list_of_scores[0], self.list_of_scores[1], self.list_of_scores[2], self.list_of_scores[3], self.list_of_scores[4], self.list_of_scores[5], 
					self.list_of_scores[6], self.list_of_scores[7], self.list_of_scores[8], self.list_of_scores[9], self.list_of_scores[10], self.list_of_scores[11], 
					self.list_of_scores[12], self.list_of_scores[13], self.list_of_scores[14], int(self.score), self.controller.patient_id.get()))
			mydb.commit()

		self.res_bttn.config(state = "normal")

class GeriatricFormRes(tk.Frame): # For viewing of previous Geriatric Depression Scale result only

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		menu_frame(self, self.controller, 2)

		self.title_font = tkfont.Font(family='Times New Roman', size=12, weight="bold")
		self.subtitle_font = tkfont.Font(family='Helvetica', size=10, weight="bold")
		self.label_font = tkfont.Font(family='Helvetica', size=10)

		page_title = tk.Label(self, text="Geriatric Depression Scale – Short Form", font=self.title_font)
		page_title.place(x=460, y=68)

		self.patient_name_label = tk.Label(self, text="", font=self.title_font)
		self.patient_name_label.place(x=90, y=110)

		question_label = tk.Label(self, text="Question", font=self.subtitle_font)
		question_label.place(x=190, y=145)
		score_label = tk.Label(self, text="SCORE", font=self.subtitle_font)
		score_label.place(x=970, y=145)

		#  form starts here
		
		with open("./data/geriatic_questions.txt", 'r') as f:
			self.questions = f.read().splitlines()
		f.close()

		y_value = 175
		self.score = 0
		self.list_of_scores = []
		self.lob = []
		self.losl = []
		for i in range(len(self.questions)):
			b = []
			question_label = tk.Label(self, text=str(i + 1) + ".) " + self.questions[i], font=self.label_font)
			question_label.place(x=90, y=y_value)

			yes_b = tk.Button(self, text="Yes", height = 1, width = 5, bd = 1)
			yes_b.place(x=690, y=y_value) 
			no_b = tk.Button(self, text="No", height = 1, width = 5, bd = 1)
			no_b.place(x=790, y=y_value)
			score_label = tk.Label(self, text="", font=self.label_font)
			score_label.place(x=940, y=y_value)

			b.append(yes_b)
			b.append(no_b)
			self.list_of_scores.append(0)
			self.lob.append(b)
			self.losl.append(score_label)

			y_value = y_value + 30

		self.total_score = tk.Label(self, text="Total: ", font=self.subtitle_font)
		self.total_score.place(x=940, y=635)
		self.total_score_value = tk.Label(self, text="", font=self.label_font)
		self.total_score_value.place(x=980, y=635)

		self.res_bttn = tk.Button(self, text="Return", command=lambda: controller.show_frame("GeriatricForm"), height = 1, width = 12, bd = 0, bg = "#183873", fg = "#ffffff")
		self.res_bttn.place(x=90, y=635)

	def load_data(self):
		cn = cfg.dbconnect()
		cur = cn.cursor(buffered=True)
		
		cur.execute(("SELECT last_name, first_name, middle_name FROM patient WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			self.patient_name_label['text'] = res[0] + ", " + res[1] + " " + res[2]
		else:
			self.patient_name_label['text'] = ""

		cur.execute(("SELECT q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13, q_14, q_15, depression_score FROM patientdepressionscale WHERE patient_id = %s"), (self.controller.patient_id.get(),))
		res = cur.fetchone()

		if res is not None:
			for i in range(15):
				if res[i] == 1:
					(self.lob[i][1]).config(state = "disabled", bd = 0)
					(self.lob[i][0]).config(state = "disabled", bg = "#0060ba", fg = "#ffffff")
					self.losl[i]['text'] = "Score 1 point for yes" 
				else:
					(self.lob[i][0]).config(state = "disabled", bd = 0)
					(self.lob[i][1]).config(state = "disabled", bg = "#0060ba", fg = "#ffffff")
					self.losl[i]['text'] = "Score 1 point for no"
				if res[15] > 0:
					self.total_score_value['text'] = str(res[15]) 
				else:
					self.total_score_value['text'] = "0"
		else:
			self.total_score_value['text'] = ""
			for i in range(len(self.questions)):
				(self.lob[i][1]).config(state = "disabled", bg = "SystemButtonFace", fg = "#000000")
				(self.lob[i][0]).config(state = "disabled", bg = "SystemButtonFace", fg = "#000000")
				self.losl[i]['text'] = ""
