months = {
    "January": 31,
    "Febuary": 28,
    "March":   31,
    "April":   30,
    "may":     31,
    'June':    30,
    'july':    31,
    "august":  31,
    "September": 30,
    'Oktober': 31,
    "November": 30,
    "december": 31,

}
input_month = input("enter any month ")
if input_month in months:
    print(months[input_month])
else:
    print(404)

