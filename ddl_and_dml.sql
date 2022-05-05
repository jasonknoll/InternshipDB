/* All DDL needed to create the tables */
CREATE TABLE student (
        ID int NOT NULL,
        Name varchar(255) NOT NULL,
        Email varchar(255) NOT NULL,
        Address varchar(255),
        Phone varchar(255),
        PRIMARY KEY (ID),
);

CREATE TABLE Officer (
        Student_ID int NOT NULL,
        Club_Title varchar(255),
        Name varchar(255) NOT NULL,
        PRIMARY KEY (Student_ID),
        FOREIGN KEY (Student_ID) REFERENCES Student(ID),
        FOREIGN KEY (Name), REFERENCES Student(Name)
);

CREATE TABLE Company (
        Company_Name varchar(255) NOT NULL,
        Address varchar(255),
        Email varchar(255),
        PRIMARY KEY (Company_Name)
);

CREATE TABLE Internship (
        Internship_ID int NOT NULL,
        Student_ID int,
        Company_Name varchar(255) NOT NULL,
        Title varchar(255),
        Dates varchar(255),
        Wages varchar(255),
        Status varchar(255),
        PRIMARY KEY (Internship_ID),
        FOREIGN KEY (Student_ID) REFERENCES Student(ID),
        FOREIGN KEY (Company_Name) REFERENCES Company(Company_Name)
);

CREATE TABLE Duties (
        Internship_ID int NOT NULL,
        Title varchar(255),
        Experience varchar(255),
        Projects varchar(255),
        PRIMARY KEY (Internship_ID),
        FOREIGN KEY (Internship_ID) REFERENCES Internship(Internship_ID)
);


/* DML Examples */

/* Create */
INSERT INTO Student 
VALUES ("Jason Knoll", "jmknoll@school.edu", "1000 Road Ave", "1-800-Stanley Steamer");

INSERT INTO Officer
VALUES (1, "President", "Jason Knoll");


INSERT INTO Internship
VALUES (1, "Arthrex", "Junior Software Engineer", "08/01/2022-12/01/2022", "$90000", "accepted");

INSERT INTO 