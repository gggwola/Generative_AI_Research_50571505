"""
Descriptive statistics for the Generative AI survey data.

Input : 02_Quantitative_Analysis/Data_Processed/20260301_GenAI_SurveyData_Cleaned_v01.csv
Output: 02_Quantitative_Analysis/Outputs/Tables/
Author: <your name>
Date  : 2026-03-05
"""

import pandas as pd

DATA = "../Data_Processed/20260301_GenAI_SurveyData_Cleaned_v01.csv"

def main():
    df = pd.read_csv(DATA)
    print(df.describe(include="all"))

if __name__ == "__main__":
    main()
