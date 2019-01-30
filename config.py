
# set the path-to-files
TRAIN_FILE = "elo_df_train.csv"
TEST_FILE = "elo_df_test.csv"

SUB_DIR = "./tfDeepFM/example/output"


NUM_SPLITS = 20
RANDOM_SEED = 2017

# types of columns of the dataset dataframe
CATEGORICAL_COLS = [
    "feature1", "feature2", "feature3"
]

NUMERIC_COLS = [
    "new_purchase_date_uptonow", "hist_month_lag_mean"
    # feature engineering
    # "missing_feat", "ps_car_13_x_ps_reg_03",
]

IGNORE_COLS = [
    "card_id", "target"
]
