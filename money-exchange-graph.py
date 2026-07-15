import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as munits
import numpy as np
import mpl_ascii
import requests
import datetime

base = "EUR"
quotes = "RUB"

def main():
    dateToday = datetime.datetime.today()
    first = dateToday.replace(day=1)
    last_month = first - datetime.timedelta(days=1)

    url = "https://api.frankfurter.dev/v2/rates"
    params = {
        "base": base,
        "quotes": quotes,
        "from": last_month.strftime('%Y-%m-%d'),
        "to": dateToday.strftime('%Y-%m-%d')

    }

    response = requests.get(url= url, params= params)

    if response.status_code == 200:
        data = list(response.json())
        filteredData = {x["date"]: float(x["rate"]) for x in data}
        #print(filteredData)
        drawingGraph(data= filteredData)
    else:
        print(f"{response.status_code=}")

def drawingGraph(*, data: dict):
    mpl.use("module://mpl_ascii")
    fig, ax = plt.subplots(figsize=(4,5))
    time = np.arange(len(data))

    rates = np.array(list(data.values()))

    ax.plot(time, rates)
    ax.set_xticks([])
    ax.set_title(f"{base} → {quotes}")

    plt.show()

if __name__ == "__main__":
    main()
