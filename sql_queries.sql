CREATE TABLE Admint
(
	AdmintId int auto_increment key,
    AdmintName Varchar(200),
    AdmintPassword Varchar(100),
    AdmintEmail Varchar(200),
    AdmintContact Varchar(100),
    AdmintFlat Varchar(100),
    AdmintWing Varchar(100),
    AdmintRole Varchar(100)
);

Create table Maintainance
(
    MaintainanceId int auto_increment key,
	AdmintId int,
    Amount int,
	AsOfMonth varchar(500),
    IsPaid bit
);

CREATE table Entry
(
	EntryId int auto_increment key,
    timein Varchar(100),
	timeout varchar(100),
	Reason varchar(500),
    contact varchar(100),
	name1 varchar(100)
);


















