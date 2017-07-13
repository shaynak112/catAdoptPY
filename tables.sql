

DROP TABLE if EXISTS cats;
CREATE TABLE cats(name text not null, age integer not null, gender text, breed text, colour text,  imageURL text, trait1 text, trait2 text, trait3 text, description text, adopted text not null, rescue text not null);

INSERT INTO cats VALUES('Baby Girl',10,'female','tabby','multi-color','static/images/1.jpg','affectionate','playful','inquisitive',' ','no','Amanda Rescue');

INSERT INTO cats VALUES('Nemo',9,'male','shorthair','grey','static/images/2.jpg','wild','trusting','cuddly','Nemo would be described as wild, trusting, and cuddly. Nemo loves following around his human and being picked up and cuddled. He is a cheerful cat and never grumpy.','no','Meow Rescue');



DROP TABLE if EXISTS applications;
CREATE TABLE applications (fullName text not null, age integer not null, email text not null, phone text not null, address text not null, occupation text not null, catName text not null, refName text not null, refRelationship text not null, refPhone text not null, dateApplied date, followUp text, sucessful text);
INSERT INTO applications VALUES ('Shayna',26,'shayna@shaynak112.com','1112223333','123 Shayna Street','Student','Zia','Ben','friend','3334445555','2017-06-15','called June 18-BB','approved');


DROP TABLE if EXISTS rescues;
CREATE TABLE rescues (rescueName text not null, address text, phone text not null, email text, website text, contactPerson text not null, approved default 'no', dateApplied date, dateApproved date, password text);

INSERT INTO rescues VALUES('Shayna Rescue','123 Gladsmore','1112223333','shayna@shaynak112.com','www.shaynarescue.com','Shayna K','yes','2017-06-19','2017-06-20','shayna');


TABLES

rescues
rescueName text not null
address text
phone text not null
email text
website text
contactPerson text not null
approved default 'no' #can change to yes
dateApplied date #todays date
dateApproved date #null
password text #if this is nll when approved, it will be randomly generated

applications
fullName text not null
age integer not null
email text not null
phone text not null
address text not null
occupation text not null
catName text not null #drop down
refName text not null
refRelationship text not null
refPhone text not null
dateApplied date # date of submission
followUp text # can be changed
sucessful text # approved, pending, denied


cats
name text not null
age integer not null
gender text
breed text
colour text
imageURL text #image upload
trait1 text
trait2 text
trait3 text
description text
adopted text not null #default to no
rescue text not null #drop down or use sessions