-- Write a SQL query to find all duplicate emails in a table named Person.
--
--  +----+---------+
--  | Id | Email   |
--  +----+---------+
--  | 1  | a@b.com |
--  | 2  | c@d.com |
--  | 3  | a@b.com |
--  +----+---------+

SELECT Email FROM (SELECT count(*) AS counter, Email FROM Person GROUP BY Email ) AS Table1
WHERE counter > 1;