
#1
cur.execute('''
                SELECT first_name , last_name ,  employees.department_id ,department.department_name
                FROM employees
                JOIN department  ON department.department_id = employees.department_id
                ''')
#2
cur.execute('''
                SELECT  first_name, last_name  , city , state_province
                FROM employees , locations
                JOIN department  ON department.department_id = employees.department_id AND department.location_id = locations.location_id
                ''')


#3
cur.execute('''
            SELECT  first_name , last_name  ,department.department_name
            FROM employees  
            JOIN department  ON employees.department_id =department.department_id 
            WHERE employees.department_id = 80 OR employees.department_id= 40
            ''')

#4
cur.execute('''
            SELECT  department_id , depart_name 
            FROM departments  
            ''')

#5 тут не правельно
cur.execute('''
            SELECT  first_name , last_name  , manager_id
            FROM employees  
            ''')

#6
cur.execute('''
            SELECT jobs.job_title , first_name, last_name, 
            (SELECT MAX(salary)FROM employees)-salary
            FROM employees 
            JOIN jobs  ON jobs.job_id = employees.job_id
            ''')

#7
cur.execute('''
            SELECT  jobs.job_title ,  AVG(salary)
            FROM employees 
            JOIN jobs  ON jobs.job_id = employees.job_id
            GROUP BY employees.Job_id
            ''')

#8
cur.execute('''
            SELECT first_name , last_name , salary ,locations.city
            FROM employees ,locations
            JOIN department  ON department.department_id = employees.department_id AND department.location_id = locations.location_id
            WHERE locations.city = 'London' OR locations.city = 'Oxford'
            ''')

#9

cur.execute('''
            SELECT department.department_name, COUNT(first_name)
            FROM employees 
            LEFT JOIN department 
            ON department.department_id = employees.department_id
            GROUP BY employees.department_id

            ''')
