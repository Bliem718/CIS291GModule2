#This program is made by Bryan Liem. This part of the program imports StoreWorkerClasses.py for the classes and tests
#the functions of each of the classes.
import StoreWorkerClasses

#Sets a variable to the StoreWorker class with the following attributes.
Worker1 = StoreWorkerClasses.StoreWorker("Li Zhanguo", 1, 8, [20, 20])

#Gets Worker1's employee number.
print(Worker1.get_employee_number)

#Increases Worker1's years twice.
Worker1.increase_year()
Worker1.increase_year()

#Gets Worker1's bonus. Also prints the info of the worker.
print(Worker1.get_bonus())
print(Worker1)

#Sets a variable to the StoreWorker class with the following attributes.
Manager1 = StoreWorkerClasses.Manager("Chen Haoyu", 2, 8, [30, 20], 100)

#Gets Manager1's employee number. Also prints the info of the manager.
print(Manager1.get_employee_number)
print(Manager1)

#Increases Manager1's years twice.
Manager1.increase_year()
Manager1.increase_year()

#Gets Manager1's bonus. Also prints the info of the manager.
print(Manager1.get_bonus())
print(Manager1)

#Prints the manager's name and the salary in one line.
print(f'{Manager1.name} {Manager1.get_salary()}')

#Raises the Manager1's salary by 100. Also prints the info of the manager.
Manager1.give_raise(100)
print(Manager1)