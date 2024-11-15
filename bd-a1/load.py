import pandas as pd
import sys
from dpre import preprocessing
from vis import visualize
from eda import EDA
from model import K_model
import os
import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


def load(file_path):
    try :
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
    preprocessed_df = preprocessing(df)
    visualize(df)
    EDA(df)
    K_model(preprocessed_df)

if __name__ == "__main__":
    df_path = sys.argv[1]
    df = load(df_path)    