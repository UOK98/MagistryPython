from datetime import datetime

dates = [
    "The Moscow Times - Wednesday, October 2, 2002",
    "The Guardian - Friday, 11.10.13",
    "Daily News - Thursday, 18 August 1977"
]

formats = [
    "%A, %B %d, %Y",
    "%A, %d.%m.%y",   
    "%A, %d %B %Y"    
]

for date_str, fmt in zip(dates, formats):
    newspaper, date_part = date_str.split(" - ")
    dt = datetime.strptime(date_part, fmt)
    print(f"{newspaper}: {dt}")