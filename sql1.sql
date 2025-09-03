use mydata;

create table student
(Id int not null,Name varchar(40),Age int,City varchar(40));
create table Mobile
(Id int primary key,Model varchar(40) not null,price int not null);

/*insert data  in the table*/

insert into student values
(1,"vasudev",23,"dewas");


insert into student values
(1,"vasudev",22,"dewas"),
(1,"vasudev",21,"dewas"),
(1,"vasudev",20,"dewas");

select*from student;

insert into student(id,name,City)values
(3,'niranjan',"indore");

insert into Mobile values
(1,"vivo",20000),
(2,"iphone",21000),
(3,"1 pluse",25000);

insert into Mobile(id,price)values
(3,45000);

create table laptop(Id int auto_increment key,model varchar(40) unique,price int not null, storage varchar(40) default("123gb"));

insert into laptop values
(1,"de123",6000,"512bg");
select*from laptop;
insert into laptop (model,price) values
("de125",6000);

create table employ(Id int auto_increment key,name varchar(40),age int not null,city varchar(40),check(age>=18));
insert into employ values
(1,"vasu",19,"dewas");


create table collage(Id int auto_increment key primary key, name varchar(40) not null,age int not null,check(age>=18),city varchar(40) default("dewas"),mobile bigint unique);

insert into collage values
(11,"vasudev",20,"indore",9575189285);
insert into collage (name,age,mobile)values ("niranjan",19,9575189288);
select*from collage;

insert into collage (name,age,mobile)values ("niru",20,9575189289);
select*from collage;





