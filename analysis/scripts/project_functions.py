def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns ={"bmi": "BMI"})
        .dropna()
     )
    
    return df
load_and_process("Medical_Cost.csv")

