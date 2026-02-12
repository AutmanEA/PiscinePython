import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def main():
    """
    This programs loads data life expectancy years
    and displays France plot based on this data
    - France life expectancy over time
    """
    filename = "life_expectancy_years.csv"
    path = f"/home/ael-atmi/Cursus/PicPython/2_DataTable/res/{filename}"
    data = load_csv(path)
    if data is None:
        print("Error: path not valid.")
    try:
        df = pd.DataFrame(data)
        df_france = df[df['country'] == 'France'].T[1:]
        df_france.plot(kind='line',
                       title='France life expectancy projection',
                       xlabel='Year',
                       ylabel='Life Expectancy',
                       legend=None)
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interupted manualy")


if __name__ == "__main__":
    main()
