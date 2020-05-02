from sklearn.model_selection import train_test_split


def split_data(df, test_size=0.2, seed=None):
    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df["Treatment"]
    )
    return train_df, test_df
