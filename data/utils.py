import pandas as pd
def load_data(file_path):
  return pd.read_csv(file_path)
import pandas as pd
def handle_missing_values(df):
  # Replace missing values with mean for numeric columns
  numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
  df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
  # Replace missing values with mode for categorical columns
  categorical_cols = df.select_dtypes(include=['object']).columns
  df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
  return df
from sklearn.preprocessing import OneHotEncoder
def encode_categorical_variables(df):
  categorical_cols = df.select_dtypes(include=['object']).columns
  encoder = OneHotEncoder(sparse=False)
  encoded_data = encoder.fit_transform(df[categorical_cols])
  encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names(categorical_cols))
  # Concatenate encoded data with numeric data
  numeric_df = df.select_dtypes(include=['int64', 'float64'])
  df = pd.concat([numeric_df, encoded_df], axis=1)
  return df
from sklearn.preprocessing import StandardScaler
def scale_numeric_variables(df):
  numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
  scaler = StandardScaler()
  df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
  return df
def load_data(file_path):
  # Load dataset
  df = pd.read_csv(file_path)
  # Handle missing values
  df = handle_missing_values(df)
  # Encode categorical variables
  df = encode_categorical_variables(df)
  # Scale numeric variables
  df = scale_numeric_variables(df)
  return df
