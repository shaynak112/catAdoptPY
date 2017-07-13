CREATE TABLE applications (id integer primary key autoincrement not null, fullName text not null, age integer not null, email text not null, phone text not null, address text not null, occupation text not null, catName text not null, refName text not null, refRelationship text not null, refPhone text not null);

DROP TABLE if EXISTS cats;
CREATE TABLE cats(name text not null, age integer not null, gender text, breed text, colour text,  imageURL text, trait1 text, trait2 text, trait3 text, description text, adopted text not null, rescue text not null);

INSERT INTO cats VALUES('Baby Girl',10,'female','tabby','multi-color','static/images/1.jpg','affectionate','playful','inquisitive',' ','no','Amanda Rescue');

INSERT INTO cats VALUES('Nemo',9,'male','shorthair','grey','static/images/2.jpg','wild','trusting','cuddly','Nemo would be described as wild, trusting, and cuddly. Nemo loves following around his human and being picked up and cuddled. He is a cheerful cat and never grumpy.','no','Meow Rescue');

INSERT INTO cats VALUES('Audrey',13,'female','short hair','brown','static/images/3.jpg','cuddly','needy','inquisitive','Audrey loves attention and always wants to be where the action is. As long as something is going on, Audrey is the first to find out.','no','Shayna Rescue');

INSERT INTO cats VALUES ('Rolo',7,'female','calico','calico','static/images/4.jpg','mischievious','curious','social',' ','no','Amanda Rescue');

INSERT INTO cats VALUES('Nero',1,'female','tabby','grey','static/images/5.jpg','wild','cuddly','needy','Nero loves stealing food when no one is looking. The spots on her belly make her look partly Bengal.','no','Meow Rescue');

INSERT INTO cats VALUES('Punk',8,'male','short hair','grey','static/images/6.jpg','happy','foodie','gentle giant','Punk was found malnourished in a park and, as a result, he is always begging for food and cannot resist any opportunity to steal some. He is a very content and happy cat.','no','Meow Rescue');

INSERT INTO cats VALUES('Missy',15,'female','short hair','tabby','static/images/7.jpg','serious','affectionate','loyal',' ','no','Amanda Rescue');

INSERT INTO cats VALUES('Little Miss Bacon',4,'female','maine coon','white','static/images/8.jpg','fickle','sweet','stubborn','Little Miss Bacon was taken away from her mother too soon so she is very affectionate and always wants attention, but only on her terms.','no','Shelby Rescue');

INSERT INTO cats VALUES('Armadillo',11,'female','Turkish Van','white','static/images/9.jpg','shy','anxious','needy','Armadillo is very shy and reserved, she gets very scared around humans or other animals who she does not know. It takes some extra time for Armadillo to trust.','no','Shayna Rescue');

INSERT INTO cats VALUES('Mary Elizabeth',10,'female','tabby','orange','static/images/10.jpg','affectionate','playful','laid back','Mary Elizabeth would be described as affectionate, playful, and laid back. Mary Elizabeth is very skeptical around other animals and would do best as an only animal in the house. However, she does love pets from any human.','no','Shelby Rescue');

INSERT INTO cats VALUES('Kinky',11,'male','maine coon','white','static/images/11.jpg','arrogant','sweet','indecisive','Kinky would be described as arrogant, sweet, and indecisive. Kinkly loves attention and always thinks he is the most gorgeous cat in the room. Although he can be demanding, he is very playful and cuddly and loves to spend time with humans.','no','Meow Rescue');

INSERT INTO cats VALUES('Fae',2,'female','tuxedo','black and white','static/images/12.jpg','territorial','playful','rambunctious','Fae is a very energetic and rambunctious younger cat. She loves watching the birds outside.','no','Meow Rescue');

INSERT INTO cats VALUES('Laila',10,'female','calico','white','static/images/13.jpg','mischievious','unique','stubborn','Laila must have her two favourite toys; a grey hippo finger puppet and a small pillow. She can be a bit shy as she refuses to play if she can see someone watching.','no','Amanda Rescue');

INSERT INTO cats VALUES('Zia',14,'female','maine coon','grey','static/images/14.jpg','energetic','playful','loving','Zia is an energetic cat who enjoys drinking out of fish bowls.','no','Shayna Rescue');

INSERT INTO applications VALUES
			(1,'Shayna',26,'shayna@shaynak112.com','1112223333','123 Shayna Street','Student','Zia','Ben','friend','3334445555');

INSERT INTO applications VALUES
			(2,'Alika',23,'akabertbud@yahoo.com','9992223333','125 Shayna Street','Radiation Technologist','Laila','Shayna','sister','1112223333');

DROP TABLE if EXISTS applications;
CREATE TABLE applications (fullName text not null, age integer not null, email text not null, phone text not null, address text not null, occupation text not null, catName text not null, refName text not null, refRelationship text not null, refPhone text not null);
INSERT INTO applications VALUES ('Shayna',26,'shayna@shaynak112.com','1112223333','123 Shayna Street','Student','Zia','Ben','friend','3334445555');
INSERT INTO applications VALUES ('Alika',23,'akabertbud@yahoo.com','9992223333','125 Shayna Street','Radiation Technologist','Laila','Shayna','sister','1112223333');
INSERT INTO applications VALUES ('Ajay',24,'ajay@shaynak112.com','4445556666','225 Shayna Street','Nuclear Medicine Technologist','Missy','Shayna','best friend','1112223333');