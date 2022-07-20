-- There is a table courses with columns: student and class
-- Please list out all classes which have more than or equal to 5 students.

SELECT class
FROM courses
GROUP BY class
HAVING count(distinct(student)) >= 5;


-- Database