from datetime import datetime as dt

def get_days_from_today(date):
    
    try:
        user_date = dt.strptime(date,'%Y-%m-%d')
        start = dt.today()
        delta = start - user_date
        return delta.days
    except ValueError:
       print("The date does not match format '%Y-%m-%d'")
  
num = (get_days_from_today("2024-02-01"))
print(num)