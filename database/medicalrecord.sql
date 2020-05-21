DROP DATABASE IF EXISTS `med_record`;

CREATE Database `med_record`;
USE `med_record`;

DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient` (
  `patient_id` int(10) NOT NULL AUTO_INCREMENT,
  `last_name` varchar(30) DEFAULT 'Last Name',
  `first_name` varchar(60) DEFAULT 'First Name',
  `middle_name` varchar(30) DEFAULT 'Middle Name',
  `address` varchar(150) NOT NULL,
  `birthdate` date,
  `age` int(3) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `civil_status` varchar(30) NOT NULL,
  `contact_no` varchar(20) DEFAULT NULL,
  `occupation` varchar(50) NOT NULL,
  PRIMARY KEY (`patient_id`)
);

DROP TABLE IF EXISTS `patientconsultation`;
CREATE TABLE `patientconsultation` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `date_of_consult` date,
  `complaint` varchar(500) DEFAULT NULL,
  `history_of_illness` varchar(500) DEFAULT NULL,
  `context` varchar(360) DEFAULT NULL,
  `present_medication` varchar(360) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientrevofsys`;
CREATE TABLE `patientrevofsys` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `heent_1` int(1) DEFAULT 0,
  `heent_2` int(1) DEFAULT 0,
  `heent_3` int(1) DEFAULT 0,
  `heent_4` int(1) DEFAULT 0,
  `heent_5` int(1) DEFAULT 0,
  `heent_6` int(1) DEFAULT 0,
  `heent_7` int(1) DEFAULT 0,
  `heent_8` int(1) DEFAULT 0,
  `heent_others` varchar(360) DEFAULT NULL,
  `respi_1` int(1) DEFAULT 0,
  `respi_2` int(1) DEFAULT 0,
  `respi_3` int(1) DEFAULT 0,
  `respi_4` int(1) DEFAULT 0,
  `respi_5` int(1) DEFAULT 0,
  `respi_others` varchar(360) DEFAULT NULL,
  `cardio_1` int(1) DEFAULT 0,
  `cardio_2` int(1) DEFAULT 0,
  `cardio_3` int(1) DEFAULT 0,
  `cardio_4` int(1) DEFAULT 0,
  `cardio_5` int(1) DEFAULT 0,
  `cardio_6` int(1) DEFAULT 0,
  `cardio_7` int(1) DEFAULT 0,
  `cardio_others` varchar(360) DEFAULT NULL,
  `gastro_1` int(1) DEFAULT 0,
  `gastro_2` int(1) DEFAULT 0,
  `gastro_3` int(1) DEFAULT 0,
  `gastro_4` int(1) DEFAULT 0,
  `gastro_5` int(1) DEFAULT 0,
  `gastro_6` int(1) DEFAULT 0,
  `gastro_7` int(1) DEFAULT 0,
  `gastro_8` int(1) DEFAULT 0,
  `gastro_9` int(1) DEFAULT 0,
  `gastro_others` varchar(360) DEFAULT NULL,
  `genito_1` int(1) DEFAULT 0,
  `genito_2` int(1) DEFAULT 0,
  `genito_3` int(1) DEFAULT 0,
  `genito_4` int(1) DEFAULT 0,
  `genito_5` int(1) DEFAULT 0,
  `genito_6` int(1) DEFAULT 0,
  `genito_7` int(1) DEFAULT 0,
  `genito_8` int(1) DEFAULT 0,
  `genito_others` varchar(360) DEFAULT NULL,
  `meta_1` int(1) DEFAULT 0,
  `meta_2` int(1) DEFAULT 0,
  `meta_3` int(1) DEFAULT 0,
  `meta_4` int(1) DEFAULT 0,
  `meta_5` int(1) DEFAULT 0,
  `meta_6` int(1) DEFAULT 0,
  `meta_others` varchar(360) DEFAULT NULL,
  `neuro_1` int(1) DEFAULT 0,
  `neuro_2` int(1) DEFAULT 0,
  `neuro_3` int(1) DEFAULT 0,
  `neuro_4` int(1) DEFAULT 0,
  `neuro_5` int(1) DEFAULT 0,
  `neuro_6` int(1) DEFAULT 0,
  `neuro_7` int(1) DEFAULT 0,
  `neuro_8` int(1) DEFAULT 0,
  `neuro_others` varchar(360) DEFAULT NULL,
  `musculo_1` int(1) DEFAULT 0,
  `musculo_2` int(1) DEFAULT 0,
  `musculo_3` int(1) DEFAULT 0,
  `musculo_4` int(1) DEFAULT 0,
  `musculo_5` int(1) DEFAULT 0,
  `musculo_others` varchar(360) DEFAULT NULL,
  `skin_1` int(1) DEFAULT 0,
  `skin_2` int(1) DEFAULT 0,
  `skin_3` int(1) DEFAULT 0,
  `skin_4` int(1) DEFAULT 0,
  `skin_5` int(1) DEFAULT 0,
  `skin_6` int(1) DEFAULT 0,
  `skin_7` int(1) DEFAULT 0,
  `skin_others` varchar(360) DEFAULT NULL,
  `famhist_illness` varchar(500) DEFAULT NULL,
  `famhist_hospt` varchar(500) DEFAULT NULL,
  `famhist_allergy` varchar(500) DEFAULT NULL,
  `famhist_1` int(1) DEFAULT 0,
  `famhist_2` int(1) DEFAULT 0,
  `famhist_3` int(1) DEFAULT 0,
  `famhist_4` int(1) DEFAULT 0,
  `famhist_5` int(1) DEFAULT 0,
  `famhist_6` int(1) DEFAULT 0,
  `famhist_7` int(1) DEFAULT 0,
  `famhist_others` varchar(360) DEFAULT NULL,
  `immuno_1` int(1) DEFAULT 0,
  `immuno_2` int(1) DEFAULT 0,
  `immuno_3` int(1) DEFAULT 0,
  `immuno_4` int(1) DEFAULT 0,
  `immuno_5` int(1) DEFAULT 0,
  `immuno_6` int(1) DEFAULT 0,
  `immuno_7` int(1) DEFAULT 0,
  `immuno_8` int(1) DEFAULT 0,
  `immuno_9` int(1) DEFAULT 0,
  `immuno_10` int(1) DEFAULT 0,
  `immuno_11` int(1) DEFAULT 0,
  `immuno_12` int(1) DEFAULT 0,
  `immuno_13` int(1) DEFAULT 0,
  `immuno_14` int(1) DEFAULT 0,
  `immuno_15` int(1) DEFAULT 0,
  `immuno_booster` varchar(360) DEFAULT NULL,
  `immuno_combi` varchar(360) DEFAULT NULL,
  `immuno_others` varchar(360) DEFAULT NULL,
  `smoker` int(1) DEFAULT 0,
  `smoker_pack` varchar(20) DEFAULT NULL,
  `smoker_quit` int(1) DEFAULT 0,
  `smoker_quit_when` varchar(30) DEFAULT NULL,
  `drinker` int(1) DEFAULT 0,
  `drinker_freq` varchar(50) DEFAULT NULL,
  `drinker_dur` varchar(50) DEFAULT NULL,
  `drinker_type` varchar(50) DEFAULT NULL,
  `exercise` int(1) DEFAULT 0,
  `exercise_type` varchar(100) DEFAULT NULL,
  `ob_g` varchar(100) DEFAULT NULL,
  `ob_p` varchar(100) DEFAULT NULL,
  `menarche` varchar(20) DEFAULT NULL,
  `menopause` varchar(20) DEFAULT NULL,
  `coitus` varchar(20) DEFAULT NULL,
  `bm_born` varchar(50) DEFAULT NULL,
  `bm_via` varchar(50) DEFAULT NULL,
  `bm_g` varchar(50) DEFAULT NULL,
  `bm_p` varchar(50) DEFAULT NULL,
  `bm_year` varchar(50) DEFAULT NULL,
  `bm_compli` varchar(50) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id2` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientassessment`;
CREATE TABLE `patientassessment` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `hr` varchar(10) DEFAULT NULL,
  `bp` varchar(10) DEFAULT NULL,
  `rr` varchar(10) DEFAULT NULL,
  `temp` varchar(10) DEFAULT NULL,
  `height` varchar(10) DEFAULT NULL,
  `bmi` varchar(10) DEFAULT NULL,
  `ibw` varchar(10) DEFAULT NULL,
  `hip_circ` varchar(10) DEFAULT NULL,
  `waist_circ` varchar(10) DEFAULT NULL,
  `head_circ` varchar(10) DEFAULT NULL,
  `abw` varchar(10) DEFAULT NULL,
  `ge_1` int(1) DEFAULT 0,
  `ge_2` int(1) DEFAULT 0,
  `ge_others` varchar(360) DEFAULT NULL,
  `skin_1` int(1) DEFAULT 0,
  `skin_2` int(1) DEFAULT 0,
  `skin_others` varchar(360) DEFAULT NULL,
  `musculo_1` int(1) DEFAULT 0,
  `musculo_2` int(1) DEFAULT 0,
  `musculo_others` varchar(360) DEFAULT NULL,
  `heent_1` int(1) DEFAULT 0,
  `heent_2` int(1) DEFAULT 0,
  `heent_others` varchar(360) DEFAULT NULL,
  `respi_1` int(1) DEFAULT 0,
  `respi_2` int(1) DEFAULT 0,
  `respi_others` varchar(360) DEFAULT NULL,
  `cardio_1` int(1) DEFAULT 0,
  `cardio_2` int(1) DEFAULT 0,
  `cardio_others` varchar(360) DEFAULT NULL,
  `gastro_1` int(1) DEFAULT 0,
  `gastro_2` int(1) DEFAULT 0,
  `gastro_others` varchar(360) DEFAULT NULL,
  `genito_1` int(1) DEFAULT 0,
  `genito_2` int(1) DEFAULT 0,
  `genito_others` varchar(360) DEFAULT NULL,
  `ie_1` int(1) DEFAULT 0,
  `ie_2` int(1) DEFAULT 0,
  `ie_others` varchar(360) DEFAULT NULL,
  `dre_1` int(1) DEFAULT 0,
  `dre_2` int(1) DEFAULT 0,
  `dre_others` varchar(360) DEFAULT NULL,
  `neuro_1` int(1) DEFAULT 0,
  `neuro_2` int(1) DEFAULT 0,
  `neuro_others` varchar(360) DEFAULT NULL,
  `assessment` varchar(500) DEFAULT NULL,
  `icd_code` varchar(500) DEFAULT NULL,
  `dpra` varchar(500) DEFAULT NULL,
  `ti_drugs` varchar(360) DEFAULT NULL,
  `ti_diet` varchar(360) DEFAULT NULL,
  `ti_lifestyle` varchar(360) DEFAULT NULL,
  `ti_exer` varchar(360) DEFAULT NULL,
  `ti_ref` varchar(360) DEFAULT NULL,
  `ti_follow` varchar(360) DEFAULT NULL,
  `strat_1` int(1) DEFAULT 0,
  `strat_2` int(1) DEFAULT 0,
  `strat_3` int(1) DEFAULT 0,
  `strat_others` varchar(360) DEFAULT NULL,
  `famassessment` varchar(500) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id3` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientdepressionscale`;
CREATE TABLE `patientdepressionscale` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `depression_score` int(2) DEFAULT 0,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id4` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientconsultform`;
CREATE TABLE `patientconsultform` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `date_form` date,
  `diagnosis` varchar(500) DEFAULT NULL,
  `physician_name` varchar(360) DEFAULT NULL,
  `diagnostics` varchar(500) DEFAULT NULL,
  `medications` varchar(500) DEFAULT NULL,
  `dispositions` varchar(500) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id5` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientfamassessment`;
CREATE TABLE `patientfamassessment` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `genogram` varchar(500) DEFAULT NULL,
  `family_map` varchar(500) DEFAULT NULL,
  `ecomap` varchar(500) DEFAULT NULL,
  `fam_1_apgar_score` varchar(5) DEFAULT NULL,
  `fam_2_apgar_score` varchar(5) DEFAULT NULL,
  `avg_apgar_score` varchar(5) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id6` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientfammember`;
CREATE TABLE `patientfammember` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `member_name` varchar(360) DEFAULT NULL,
  `screening` int(1) DEFAULT 0,
  `immunization` int(1) DEFAULT 0,
  `lifestyle_changes` int(1) DEFAULT 0,
  `counseling_needs` int(1) DEFAULT 0,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id7` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientfollowup`;
CREATE TABLE `patientfollowup` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `followup_date` date,
  `reason_1` int(1) DEFAULT 0,
  `reason_2` int(1) DEFAULT 0,
  `followup_s` varchar(500) DEFAULT NULL,
  `followup_med` varchar(500) DEFAULT NULL,
  `hr` varchar(10) DEFAULT NULL,
  `bp` varchar(10) DEFAULT NULL,
  `rr` varchar(10) DEFAULT NULL,
  `temp` varchar(10) DEFAULT NULL,
  `weight` varchar(10) DEFAULT NULL,
  `ge_1` int(1) DEFAULT 0,
  `ge_2` int(1) DEFAULT 0,
  `ge_others` varchar(360) DEFAULT NULL,
  `skin_1` int(1) DEFAULT 0,
  `skin_2` int(1) DEFAULT 0,
  `skin_others` varchar(360) DEFAULT NULL,
  `musculo_1` int(1) DEFAULT 0,
  `musculo_2` int(1) DEFAULT 0,
  `musculo_others` varchar(360) DEFAULT NULL,
  `heent_1` int(1) DEFAULT 0,
  `heent_2` int(1) DEFAULT 0,
  `heent_others` varchar(360) DEFAULT NULL,
  `respi_1` int(1) DEFAULT 0,
  `respi_2` int(1) DEFAULT 0,
  `respi_others` varchar(360) DEFAULT NULL,
  `cardio_1` int(1) DEFAULT 0,
  `cardio_2` int(1) DEFAULT 0,
  `cardio_others` varchar(360) DEFAULT NULL,
  `gastro_1` int(1) DEFAULT 0,
  `gastro_2` int(1) DEFAULT 0,
  `gastro_others` varchar(360) DEFAULT NULL,
  `genito_1` int(1) DEFAULT 0,
  `genito_2` int(1) DEFAULT 0,
  `genito_others` varchar(360) DEFAULT NULL,
  `ie_1` int(1) DEFAULT 0,
  `ie_2` int(1) DEFAULT 0,
  `ie_others` varchar(360) DEFAULT NULL,
  `dre_1` int(1) DEFAULT 0,
  `dre_2` int(1) DEFAULT 0,
  `dre_others` varchar(360) DEFAULT NULL,
  `neuro_1` int(1) DEFAULT 0,
  `neuro_2` int(1) DEFAULT 0,
  `neuro_others` varchar(360) DEFAULT NULL,
  `assessment` varchar(500) DEFAULT NULL,
  `icd_code` varchar(500) DEFAULT NULL,
  `dpra` varchar(500) DEFAULT NULL,
  `ti_drugs` varchar(360) DEFAULT NULL,
  `ti_diet` varchar(360) DEFAULT NULL,
  `ti_lifestyle` varchar(360) DEFAULT NULL,
  `ti_exer` varchar(360) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id8` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientreferral`;
CREATE TABLE `patientreferral` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `date_of_followup` date,
  `referring_phys` varchar(360) DEFAULT NULL,
  `phys_referred_to` varchar(360) DEFAULT NULL,
  `reasons` varchar(500) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id9` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `patientsummary`;
CREATE TABLE `patientsummary` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `impression` varchar(360) DEFAULT NULL,
  `brief_history` varchar(360) DEFAULT NULL,
  `summ_lab` varchar(500) DEFAULT NULL,
  `summ_meds` varchar(500) DEFAULT NULL,
  `patient_id` int(10),
  CONSTRAINT `pk_log_id` PRIMARY KEY (log_id),
  CONSTRAINT `fk_patient_id10` FOREIGN KEY (patient_id)
  REFERENCES patient(patient_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);