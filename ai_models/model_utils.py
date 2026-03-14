import pandas as pd


def load_transactions(file_path):
    """
    Load transaction dataset
    """

    df = pd.read_csv(file_path)

    return df


def create_basket(df):
    """
    Convert transaction data into basket format
    """

    basket = (
        df.groupby(['Customer_ID', 'Product'])['Product']
        .count()
        .unstack()
        .fillna(0)
    )

    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    return basket
