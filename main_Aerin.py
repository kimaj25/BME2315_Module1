import pandas as pd

df = pd.read_csv("C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/Module 1/BME2315_Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)

