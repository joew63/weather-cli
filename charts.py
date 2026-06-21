import matplotlib.pyplot as plt
from database import get_rows

def show_charts():
    rows = get_rows()
    dates = list()
    temps = list()

    for row in rows:
        dates.append(row[0])
        temps.append(row[2])

    plt.plot(dates,temps)
    plt.title("Daily Temperature")
    plt.xlabel("Dates")
    plt.ylabel("Temperature")
    plt.show()
