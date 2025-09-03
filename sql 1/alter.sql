/* alter statement
1) rename
2) addcolum
3} remove colum
4) change Data type 
5)  Drop

*/
use mydata;

-- rename table name--
alter table collage
rename new_collage;

-- add colume in  table--
alter table new_collage
add column fees int not null;

select*from new_collage;

-- add multipal column--

alter table new_collage
add column subject varchar(50) not null,
add column  class int,
add column dob date ;



-- remove colume in table--
alter table new_collage
drop column subject;


-- drop multipal colume
alter table new_collage
drop column fees,
drop column dob,
drop column class;

-- drop table 
drop table employ;
-- change data type of colume in table--
alter table new_collage
modify column id float;

select*from new_collage;



-- change the constraints of existing table
alter table new_collage
modify column mobile bigint not null;

insert into new_collage (id,name,age)values (12.4,"niru",20);

alter table new_collage
modify column mobile bigint add constraints unique ;
-- drop colume in table--
alter table new_collage
 add constraints unique mobile ;
insert into new_collage values
(15.4,"vasudev",40,"dewas",55125);
-- operaters
select *from new_collage
where age!=20;

select *from new_collage
where age<=20;


select *from new_collage
where age<=20;

select *from new_collage
where city!="indore";

-- and or operater
select *from new_collage
where age<=20 and city='indore';

select *from new_collage
where age<20 or city='indore';

select *from new_collage
where age>20 and city='indore';

select *from new_collage
where age>20 or city='indore';

select *from new_collage
where  city='indore' and
(age=30 or age=40);


select *from new_collage
where  city='indore' or
(age=30 and age=40);

-- not operatyer
select*from new_collage
where not city="dewas";

select*from new_collage
where not (age=20 or age=30);

select*from new_collage
where not (age=20 and city="indore");

-- in or not in  operater
select*from new_collage
where age in (30,40);

select*from new_collage
where age not in (30,40);

select*from new_collage
where age not in (30,40) and city="dewas";

-- bitwen operater
select*from new_collage
where age between 21 and 29;

select*from new_collage
where age between 21 and 29;