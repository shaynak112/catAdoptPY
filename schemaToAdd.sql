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


/*new code*/

DROP TABLE if EXISTS applications;
CREATE TABLE applications (fullName text not null, age integer not null, email text not null, phone text not null, address text not null, occupation text not null, catName text not null, refName text not null, refRelationship text not null, refPhone text not null, dateApplied date, followUp text, sucessful text);
INSERT INTO applications VALUES ('Shayna',26,'shayna@shaynak112.com','1112223333','123 Shayna Street','Student','Zia','Ben','friend','3334445555','2017-06-15','called June 18-BB','approved');
INSERT INTO applications VALUES ('Alika',23,'akabertbud@yahoo.com','9992223333','125 Shayna Street','Radiation Technologist','Laila','Shayna','sister','1112223333','2017-06-16','called June 19-MD','approved');
INSERT INTO applications VALUES ('Ajay',24,'ajay@shaynak112.com','4445556666','225 Shayna Street','Nuclear Medicine Technologist','Missy','Shayna','best friend','1112223333','2017-06-17','called June 21-NM','denied');


DROP TABLE if EXISTS rescues;
CREATE TABLE rescues (rescueName text not null, address text, phone text not null, email text, website text, contactPerson text not null, approved default 'no', dateApplied date, dateApproved date, password text);
INSERT INTO rescues VALUES('Shayna Rescue','123 Gladsmore','1112223333','shayna@shaynak112.com','www.shaynarescue.com','Shayna K','yes','2017-06-19','2017-06-20','shayna');
INSERT INTO rescues VALUES('Bob Rescue','444 Humber College','4442223333','bob@rescue.com','www.bobrescue.com','Bob Sir','no','2017-06-16','2017-06-17',NULL);

##sort or search by rescue



##add success stories

INSERT INTO cats VALUES('Venus',3,'female','short hair','grey','static/images/15.jpg','fun','playful','loving','Venus was adopted at age 3 by a young family. She enjoys being the only cat in the family. She loves cuddling with her human friends especially if they are watching TV or reading a book. She also loves sitting in her favourite rocking chair in the middle of the living room so she can always be the centre of attention.','yes','Meow Rescue');
INSERT INTO cats VALUES('Snickers',6,'female','short hair','multi colour','static/images/16.jpg','entertaining','playful','loving','Snickers was adopted at age 6 by a family outside of the city. After being adopted, her family noticed how much Snickers loved watching out the windows at everything, so they decided to try taking her for a walk on the leash. She loves the wind and all the animals she can see on her walks. Now every time the door opens, Snickers is running right up to see if she gets to go outside this time too.','yes','Shayna Rescue');
INSERT INTO cats VALUES('Scruffy',1,'female','Turkish Van','white','static/images/17.jpg','entertaining','energetic','snuggly','Scruffy was adopted as a kitten by Veronika and Johnny; he was part of an abandoned litter left on a foster parents doorstep. He was very scared at first however he warmed up to his family very quickly. Now Scruffy cannot spend enough time with them and he is always eager to play games or even just watch TV.','yes','Meow Rescue');
INSERT INTO cats VALUES('Caramel',13,'female','long hair','orange','static/images/18.jpg','loving','needy','snuggly','Caramel was adopted at age 13 by Ben. Caramel has grown very fond of her sister, Smudge, and they enjoy curling up by the window and watching birds together. Caramel enjoys playing with her catnip toys and they are often hidden in silly places around the apartment.','yes','Shayna Rescue');
INSERT INTO rescues VALUES('Meow Rescue','123 Humber College','4442228888','admin@meow.com','www.meow.com','Alika Meow','yes','2017-06-10','2017-06-11','meow');

#above completed June 23