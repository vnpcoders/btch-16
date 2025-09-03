-- delete and truncate
use mydata;

select * from  mobile;
-- use to delete spacifec row from the table on the basesa of id
delete from mobile
where id =2; 
-- use truncate for remove all data from table
truncate  table new_collage;
 
 -- use drop for remove table from database
 
 drop table student;
 -- rollback and comit 
 use amazon;
 start transaction;
 
 delete  from orders
 where id=4;
 
 select*from orders;
 rollback;
 
 
 