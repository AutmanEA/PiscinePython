import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def main():
    """
    """
    filename = "life_expectancy_years.csv"
    path = f"/home/ael-atmi/Cursus/PicPython/2_DataTable/res/{filename}"
    df = pd.DataFrame(load_csv(path))
    df_france = df[df['country']=='France'].T[1:]
    df_france.plot(kind='line',
                   title='France life expectancy projection',
                   xlabel='Year',
                   ylabel='Life Expectancy',
                   legend=None)
    plt.show()


if __name__ == "__main__":
    main()
