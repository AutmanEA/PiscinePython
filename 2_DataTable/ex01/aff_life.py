import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv


def main():
    """
    """
    dataset = pd.DataFrame(load_csv("res/life_expectancy_years.csv"))
    dataset.plot()
    plt.show()
    pass


if __name__ == "__main__":
    main()
