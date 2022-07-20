-- Write a SQL query to find all duplicate emails in a table named Person.
--
--  +----+---------+
--  | Id | Email   |
--  +----+---------+
--  | 1  | a@b.com |
--  | 2  | c@d.com |
--  | 3  | a@b.com |
--  +----+---------+

SELECT email
FROM person
GROUP BY email
HAVING count(email) > 1;


-- Database