# Pewlett-Hackard-Analysis

## Project Overview

## Purpose
PH has decided to offer retirement packages and needs to find out which positions need to be filled in the future, but PH itself has fallen behind in maintaining the database.

With the help of SQL tools (PostgreSQL and PgAdmin4), PH wants to maintain the data and prepare the company with
several thousand employees for the upcoming "Silver Tsunami".
	
As per the dataset, lots of employees are going to be retiring in the future and PH needs to prepare retirement packages, for
open positions and for employee training.

## Requirements:
 1. Identify the retiring employees by their title.
 2. Determine the sum of retiring employees grouped by title.
 3. Identify the employees eligible for participation in the mentorship program.
 4. Determine the number of roles-to-fill grouped by title and department.
 5. Determine the number of qualified, retirement-ready employees to mentor the next generation grouped by title and department.



## Resources
- **Data Source:**
  - [CSV files](Data_Source/)
    - The data is gathered in six CSV files and the analysis is performed using relational databases.

- **QuickDBD** - To create quick database design for better visualization.
- **PostgreSQL** - A database system to load, build and host company’s data.
- **pgAdmin** - A GUI, using SQL Language to explore, manipulate and extract the data.

## ERD and Schema
 
ERD An entity-relationship diagram (ERD) is crucial to creating a good database design.
   - It is used as a high-level logical data model, which is useful in developing a conceptual design for databases.
   
     ![Pewlett-Hackard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/ERD%20EmployeeDB.png)
      
## Schema:

- [Schema](Queries/schema.sql) A schema is a collection of database objects like tables, triggers, stored procedures, etc.
- Database may have one or more schema. 
- Schemas are important for designing database management systems (DBMS) or relational database management systems (RDBMS).
- Schema is of three types: Physical schema, logical schema and view schema.


## Results


**1.	The list of retiring employees**

-	The table includes employee number, first name, last name, title, from-date and to-date.
-	The query returns 133,776 rows. 
-	The table displays mixed data of employees who are going to retire in the next few years and those who left the jobs.
-	The list is long and extensive and includes duplicate data like some employees appear more than once due to change of title during their career at Pewlett-Hackard.

	![Hewlett-Packard-Ananlysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/retiring%20employees.png)
	
- To retrieve the data we need to join/merge two tables.`'employee as e and title as ti'`.
- Based on `e.emp_no,e.first_name,e.last_name,ti.title,ti.from_date,ti.to_date`.
- We use `INNER JOIN title as ti`, `ON(e.emp_no=ti.emp_no)` and filtered with `birth_date`, to find out who is going to retire in few years.
- With where clause`(e.birth_date BETWEEN '1952-01-01' AND '1955-12-31')`.
	


## 
  
**2.	The list of retiring employees without duplicates**
-	The table includes employee number, first_name, last_name, title, from_date and to_date.
-	We removed duplicate data using where clause on date `(rt.to_date='9999-01-01')`
-	The query returns 72,458 rows. 
- 	The table displays a list of employees who are going to retire in the next few years.
-	In the table each employee is listed only once, by his/her most recent title.

	![Pewlett-Hackard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/retiring%20employees%20wo%20duplicates.png)
	
- To retrieve the unique Retiring employees we need to use `'DISTINCT' clause 'ON'` retiring_emp table with where clause on date `(rt.to_date='9999-01-01')` to get only retiring employees not the employees who left the company.
- `ORDER By clause ON 'emp_no' and 'to_date'` to sort the data by descending order.
	

##

**3.	The number of retiring employees (72458) grouped by title**

-	The table includes employee titles and their sum. 
-	The query returns a cohesive table with 7 rows.
-	From this table we can quickly see how many employees by title will retire in the next few years.
	![Hewlett-Packard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/retiring%20employees%20by%20title.png)
	
- To find out retiring employee count we will use `GROUP BY` clause to group titles from unique title table and sort it for most recent values with `ORDER BY count DESC`.


##

**4.	The employees eligible for the mentorship program**

-	The table contains employee number, first name, last name, birth_date, from_date to_date and title. 
-	The query returns 1,549 rows.
- 	The table displays a list of employees who are eligible for the mentorship program.
	![Hewlett-Packard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/employees%20elig%20mentorship%20program.png)

	
	
- To retrieve this data 3 tables need to be mearged together `employee,titles,dept_emp`,title with `INNER JOIN`.
- Then query filters by `birth_date betwwen ('1965-01-01' AND '1965-12-31')` and `to_date` to include only current values.
- It is unique data because we used `DISTINCT ON(emp_no)`.	
- To ensure most recent values we will use `ORDER BY e.emp_no,ti.from_date DESC`.





## Summary


As the company is preparing for the upcoming "silver tsunami" good plan is very important, especially when too many employees are involved.

Reports above give a good insight about the number of the employees that are about to retire and hold specific titles. 

We need to concentrate on staff and their respective departments so that headquarters can see what to expect in each department separately. 
Here we used `retirement_titles`,`dept_emp`,`departments` table to retrive the Roles Per Staff and Departament which has 90398 rows in it.
	
![Hewlett-Packard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/retirement%20ready%20emp.png)
	

- To retrieve department name information, we can join/merge additional table `departments` into existing table `retirement_titles` with the `inner join`.
- After removing the duplicates, with `DISTINCT ON` command, the table was ready to be used for additional queries.
- `order by  rt.emp_no, rt.to_date DESC` which returns the most recent values.


##

***How many roles will need to be filled as the "silver tsunami" begins to make an impact?*** <br>

Here we can have an additional query that breaks down how many staff will retire per department. 

Since every department will be impacted in some way this query gives more precise numbers what each department can expect and how many roles will need to be filled.

Here we are retrieving roles that need to be fill per title and department.

![Hewlett-Packard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/sum%20retirement%20ready%20emp.png)
	
	
- With the help of group by dept_name and title we can find out number of rolls need to fill per title and department.
	

##

***Are there enough qualified, retirement-ready employees in the departments to mentor the next generation of Pewlett-Hackard employees?*** <br>


To make sure that there are enough qualified staff for training at Pewlett-Hackard we will run another query with an additional filter that returns only employees in higher positions, assuming that those are qualified as mentors.

The results includes only staff in higher positions.

![Hewlett-Packard-Analysis](https://github.com/Lauramasonjar/Pewlett-Hackard-Analysis/blob/main/PNGs/sum%20retirment%20ready%20by%20title%20dept.png)
	
	
- We can find out who is qualified and ready to give training for upcoming candidates.
- We can retrieve dept_name and count(title) from unique_titles_departments and put condition `WHERE ut.titles IN("Senior_staff","Senior Engineer","Technology Leader","Manager")` and `GROUP BY (dept_name and title)` with descending order.
 
