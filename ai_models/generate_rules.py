import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from ai_models.model_utils import load_transactions, create_basket


def generate_association_rules(file_path):

    df = load_transactions(file_path)

    basket = create_basket(df)

    frequent_itemsets = apriori(
        basket,
        min_support=0.02,
        use_colnames=True
    )

    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=0.3
    )

    return rules
