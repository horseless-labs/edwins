/* Temporary schema for a reduced version of the volunteer intake form.
   For testing purposes only. */

DROP TABLE IF EXISTS volunteer_small;

CREATE TABLE volunteer_small (
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
	dob TEXT
);