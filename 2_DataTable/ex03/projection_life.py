import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def main():
    """
    Displays life expectancy scattered with
    gross domestic product in 1900
    """
    file_ley = "life_expectancy_years.csv"
    path_ley = f"/home/ael-atmi/Cursus/PicPython/2_DataTable/res/{file_ley}"
    data_ley = load_csv(path_ley)
    file_ipp = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    path_ipp = f"/home/ael-atmi/Cursus/PicPython/2_DataTable/res/{file_ipp}"
    data_ipp = load_csv(path_ipp)
    if data_ley is None or data_ipp is None:
        print("Error: path not valid.")
    try:
        df_ley = pd.DataFrame(data_ley.set_index('country'))
        df_ipp = pd.DataFrame(data_ipp.set_index('country'))
        df = pd.DataFrame({"ley": df_ley['1900'], "ipp": df_ipp['1900']})
        df = df.dropna()
        plt.plot()
        plt.title('1900'),
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.scatter(df['ipp'], df['ley'])
        plt.xscale('log')
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interupted manualy")


if __name__ == "__main__":
    main()
