-- joins joins are used to canect the maches data ther are four type of join 
-- 1) inner join
-- 2) outer join 
-- 3) lift join 
-- 4) Right join 

create database Amazon;
use Amazon;

create table orders
(Id int primary key,
Name varchar(50) not null,
price float,
orderdate Date);

create table Payment
(Id int primary key auto_increment,
Paymentmode varchar(50),
paymentDate  date);

insert into Orders values
(1,"Redmi",21000,"2023-04-21"),
(2,"vivo20",25000,"2025-08-21"),
(3,"mi",23000,"2025-06-1"),
(4,"iphone",27000,"2025-09-04"),
(6,"samsung",21000,"2025-03-03"),
(7,"oneplus",30000,"2025-02-24");

insert into Payment values
(1,"cash","2023-04-20"),
(2,"phonepay","2025-08-25"),
(3,"gpy","2025-06-29"),
(4,"banktanjection","2025-09-23"),
(5,"check","2025-03-1"),
(8,"cash","2025-02-08");
-- join or inner join both are same
select orders.id,orders.name,
payment.paymentmode
from orders
join payment
on orders.id=payment.id;
-- join 
select * 
from orders
join payment
on orders.id =payment.id;
-- inner join
select * 
from orders
inner join payment
on orders.id =payment.id;

-- left join

select *
from orders
left join payment
on orders.id = payment.id;
-- right join
select *
from orders
right join payment
on orders.id = payment.id;

-- cross join
select *
from orders
cross join payment
on orders.id = payment.id;

use world;

select city.countrycode,country.surfacearea,
countrylanguage.language
from city
join country
on city.countrycode = country.code
join countrylanguage
on city.countrycode = countrylanguage.countrycode;


select  country.code,country.surfacearea,
countrylanguage.language
from country
join countrylanguage
on country.code=countrylanguage.countrycode
where country.code ="Ind";
