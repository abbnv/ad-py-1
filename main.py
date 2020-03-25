from application.salary import calculate_salary
import application.db.people as peoples
import datetime

if __name__ == '__main__':
    calculate_salary()
    peoples.get_employees()

    now = datetime.datetime.today()
    print(f"Сегодня: {now}")
