import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def convert_data_numbers(nbr):
    """
    """
    try:
        if nbr.endswith('M'):
            return float(nbr[:-1]) * 1000000
        elif nbr.endswith('k'):
            return float(nbr[:-1]) * 1000
        else:
            return float(nbr)
    except:
        return None


def main():
    """
    """
    filename = "population_total.csv"
    path = f"/home/ael-atmi/Cursus/PicPython/2_DataTable/res/{filename}"
    data = load_csv(path)
    if data is None:
        print("Error: path not valid.")
    try:
        df_pop = pd.DataFrame(data.set_index('country'), dtype='str')
        df_pop = df_pop.loc[['France', 'Japan'], '1800':'2050'].map(convert_data_numbers)
        maxpop = int(df_pop.max().max())
        minpop = int(df_pop.min().min())
        df_pop.T.plot(title='Population projections',
                    xlabel='Year',
                    ylabel='Population',
                    )
        yticks = range(minpop - 10000000, maxpop + 10000000, 20000000)
        ylabels = [f'{x // 1000000}M' for x in yticks]
        plt.yticks(yticks, ylabels)
        xticks = range(0,2050 - 1800,40)
        xlabels = [f'{x + 1800}' for x in xticks]
        plt.xticks(xticks, xlabels)
        plt.legend(loc='upper left')
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interupted manualy")


if __name__ == "__main__":
    main()
