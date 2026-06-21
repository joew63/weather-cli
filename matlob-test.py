import matplotlib.pyplot as plt

dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [65, 68, 70, 67, 72, 76, 75]

plt.plot(dates, temps)
plt.title("Daily Temperature")
plt.xlabel("Dates")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()
