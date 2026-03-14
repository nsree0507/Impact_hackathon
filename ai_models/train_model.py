from ai_models.generate_rules import generate_association_rules


DATASET_PATH = "datasets/transactions.csv"


def train():

    rules = generate_association_rules(DATASET_PATH)

    print("Generated Rules:")
    print(rules[['antecedents', 'consequents', 'confidence']])

    # Save rules to CSV
    rules.to_csv("datasets/generated_rules.csv", index=False)

    print("Rules saved to datasets/generated_rules.csv")


if __name__ == "__main__":
    train()
