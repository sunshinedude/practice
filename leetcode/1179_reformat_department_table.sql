-- Problem

-- Table: Department
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | revenue       | int     |
-- | month         | varchar |
-- +---------------+---------+
-- (id, month) is the primary key of this table.
-- The table has information about the revenue of each department per month.
-- The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
--
--
-- Write an SQL query to reformat the table such that there is a department
-- id column and a revenue column for each month.
--
-- The query result format is in the following example:
--
-- Department table:
-- +------+---------+-------+
-- | id   | revenue | month |
-- +------+---------+-------+
-- | 1    | 8000    | Jan   |
-- | 2    | 9000    | Jan   |
-- | 3    | 10000   | Feb   |
-- | 1    | 7000    | Feb   |
-- | 1    | 6000    | Mar   |
-- +------+---------+-------+
--
-- Result table:
-- +------+-------------+-------------+-------------+-----+-------------+
-- | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
-- +------+-------------+-------------+-------------+-----+-------------+
-- | 1    | 8000        | 7000        | 6000        | ... | null        |
-- | 2    | 9000        | null        | null        | ... | null        |
-- | 3    | null        | 10000       | null        | ... | null        |
-- +------+-------------+-------------+-------------+-----+-------------+
--
-- Note that the result table has 13 columns (1 for the department id + 12 for the months).

-- SQL Schema

Create table If Not Exists Department (id int, revenue int, month varchar(5))
Truncate table Department
insert into Department (id, revenue, month) values ('1', '8000', 'Jan')
insert into Department (id, revenue, month) values ('2', '9000', 'Jan')
insert into Department (id, revenue, month) values ('3', '10000', 'Feb')
insert into Department (id, revenue, month) values ('1', '7000', 'Feb')
insert into Department (id, revenue, month) values ('1', '6000', 'Mar')

-- Solution with case when

select id, sum (case when month = 'Jan' then revenue end) as Jan_Revenue,
sum (case when month = 'Feb' then revenue end) as Feb_Revenue,
sum (case when month = 'Mar' then revenue end) as Mar_Revenue,
sum (case when month = 'Apr' then revenue end) as Apr_Revenue,
sum (case when month = 'May' then revenue end) as May_Revenue,
sum (case when month = 'Jun' then revenue end) as Jun_Revenue,
sum (case when month = 'Jul' then revenue end) as Jul_Revenue,
sum (case when month = 'Aug' then revenue end) as Aug_Revenue,
sum (case when month = 'Sep' then revenue end) as Sep_Revenue,
sum (case when month = 'Oct' then revenue end) as Oct_Revenue,
sum (case when month = 'Nov' then revenue end) as Nov_Revenue,
sum (case when month = 'Dec' then revenue end) as Dec_Revenue
from Department
group by id

-- Solution with pivot

select * from Department
pivot(
sum(revenue)
  for month in (
  'Jan' Jan_Revenue,
  'Feb' Feb_Revenue,
  'Mar' Mar_Revenue,
  'Apr' Apr_Revenue,
  'May' May_Revenue,
  'Jun' Jun_Revenue,
  'Jul' Jul_Revenue,
  'Aug' Aug_Revenue,
  'Sep' Sep_Revenue,
  'Oct' Oct_Revenue,
  'Nov' Nov_Revenue,
  'Dec' Dec_Revenue
  )
)
order by id;