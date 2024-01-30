from datetime import datetime


def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        x = current_date - user_date
        return int(x.days)
    except ValueError:
        print(f"ERROR. Time data {date} does not match format '%Y-%m-%d'")
        return None


if __name__ == '__main__':
    date = input("Enter the date in the format YYYY-MM-DD: ")
    print(get_days_from_today(date))
