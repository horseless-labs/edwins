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
	location TEXT,
	times TEXT,
    selected_interests TEXT,
    other_interests TEXT,
    skills TEXT,
    experience TEXT,
    oef TEXT,
    students_lives TEXT,
    other_students_lives TEXT,
    class_education TEXT,
    guest_speaker TEXT,
    facilities TEXT,
    clerical_advo TEXT
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
