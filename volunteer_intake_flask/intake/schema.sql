DROP TABLE IF EXISTS volunteer;
DROP TABLE IF EXISTS emergency_contact;

CREATE TABLE volunteer (
	volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
	active INTEGER,
	name TEXT NOT NULL,
	address TEXT,
	city TEXT,
	state TEXT,
	zip INTEGER,
	home_phone TEXT,
	occupation TEXT,
	employer TEXT,
	cell_phone TEXT,
	email TEXT,
	dob TEXT,
	availability TEXT,
	pref_location TEXT,
	pref_time TEXT,
	interest TEXT,
	skills_or_quals TEXT,
	experience TEXT,
	/* 0 for unchecked, 1 for checked from here on out */
	/* Organization - Event - Fundraising */
	photo_video INTEGER,
	food_service INTEGER,
	decoration_setup INTEGER,
	fundraising INTEGER,
	promotion INTEGER,
	/* Students' Lives */
	transportation INTEGER,
	med_assistance_advo INTEGER,
	med_dental_care INTEGER,
	nutrition INTEGER
	other TEXT,
	job_seeking INTEGER,
	aana INTEGER,
	/* Class/Education */
	field_trip_transit INTEGER,
	in_prison INTEGER,
	workshop_or_fitness INTEGER,
	guest_speaker INTEGER,
	topic TEXT,
	/* Facilities */
	dorm_helper INTEGER,
	maintenance INTEGER,
	cleaning INTEGER,
	painting INTEGER,
	light_const INTEGER,
	landscaping INTEGER,
	gardening INTEGER,
	lib_mngt INTEGER,
	homegoods_mngt INTEGER,
	/* Office/Clerical Work - Advocacy */
	town_hall_guest_spkr INTEGER,
	pol_legal_advo INTEGER,
	mail_prep INTEGER,
	internet_research INTEGER,
	comp_data_entry INTEGER,
	recruitment INTEGER,
	comp_tech_assistant INTEGER,
	desktop_pub_graphic_design INTEGER
);

CREATE TABLE emergency_contact (
	emg_contact_id REFERENCES volunteer(id),
	name TEXT,
	relationship TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	zip TEXT,
	home_phone TEXT,
	work_phone TEXT,
	cell_phone TEXT,
	email TEXT
);
