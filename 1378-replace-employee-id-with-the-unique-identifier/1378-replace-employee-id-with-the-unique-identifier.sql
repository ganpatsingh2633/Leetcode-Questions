# Write your MySQL query statement below
select unique_id , name from Employees
left join EmployeeUNI e
on(e.id = Employees.id)
