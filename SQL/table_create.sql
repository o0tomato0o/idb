drop table if exists Job_Require_Language;
drop table if exists Job_Require_Skillset;
drop table if exists Job;
drop table if exists Company;
drop table if exists Location;
drop table if exists Language;
drop table if exists Skillset;
drop table if exists Member;


CREATE TABLE Company(
	company_ID INTEGER,
	company_name TEXT,
	company_description TEXT,
	company_image TEXT,
	company_site TEXT,
	PRIMARY KEY (company_ID)
);

CREATE TABLE Location(
	location_ID INTEGER,
	location_name TEXT,
	location_description TEXT,
	location_image TEXT,
	PRIMARY KEY (location_ID)
);


CREATE TABLE Language(
	language_ID INTEGER,
	language_name TEXT,
	language_description TEXT,
	language_image TEXT,
	language_wiki_description TEXT,
	language_wiki_link TEXT,
	PRIMARY KEY (language_ID)
);


CREATE TABLE Skillset(
	skillset_ID INTEGER,
	skillset_name TEXT,
	skillset_description TEXT,
	skillset_image TEXT,
	skillset_wiki_description TEXT,
	skillset_wiki_link TEXT,
	PRIMARY KEY (skillset_ID)
);

CREATE TABLE Member(
	member_ID INTEGER,
	member_name TEXT,
	member_bio TEXT,
	member_major_responsibility TEXT,
	member_commit INTEGER,
	member_issue INTEGER,
	member_unittest INTEGER,
	member_image TEXT,
	member_leader INTEGER,
	PRIMARY KEY (member_ID)
);


CREATE TABLE Job(
	job_ID INTEGER,
	job_title TEXT,
	location_ID INTEGER NOT NULL,
	company_ID INTEGER NOT NULL,
	job_description TEXT,
	link TEXT,
	PRIMARY KEY (job_ID),
	FOREIGN KEY (location_ID) REFERENCES Location (location_ID) ON DELETE CASCADE,
	FOREIGN KEY (company_ID) REFERENCES Company (company_ID) ON DELETE CASCADE
);


CREATE TABLE Job_Require_Language(
	job_ID INTEGER,
	language_ID INTEGER,
	PRIMARY KEY (language_ID, job_ID),
	FOREIGN KEY (language_ID) REFERENCES Language (language_ID),
	FOREIGN KEY (job_ID) REFERENCES Job (job_ID) ON DELETE CASCADE
);


CREATE TABLE Job_Require_Skillset(
	job_ID INTEGER,
	skillset_ID INTEGER,
	PRIMARY KEY (skillset_ID, job_ID),
	FOREIGN KEY (skillset_ID) REFERENCES Skillset (skillset_ID),
	FOREIGN KEY (job_ID) REFERENCES Job (job_ID) ON DELETE CASCADE
);