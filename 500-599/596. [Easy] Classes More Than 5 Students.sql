-- There is a table courses with columns: student and class
-- Please list out all classes which have more than or equal to 5 students.

SELECT class FROM
(SELECT count(distinct(student)) as counter, class FROM courses GROUP BY class) AS t
WHERE counter >= 5;