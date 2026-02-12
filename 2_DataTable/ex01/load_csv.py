import pandas as pd


def load_csv(path: str) -> pd.DataFrame | None:
    """
    Loads CSV file from path and displays its dimensions
    - returns None on path error
    """
    if not isinstance(path, str):
        return None
    try:
        dataset = pd.read_csv(path)
    except Exception:
        return None
    print("Loading dataset of dimensions", dataset.shape)
    pd.options.display.show_dimensions = False
    pd.options.display.max_columns = 8
    return dataset
