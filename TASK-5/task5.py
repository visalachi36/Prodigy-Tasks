import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'output.csv'  # Update with your file path if needed
data = pd.read_csv(file_path)

# Display available columns
print("Columns in the dataset:", data.columns)

# Preprocess: Handle missing data
data.fillna(0, inplace=True)

# Analyze deaths over years
if 'Year' in data.columns and 'Deaths' in data.columns:
    year_deaths = data.groupby('Year')['Deaths'].sum()
    
    # Visualization: Deaths by Year
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=year_deaths.index, y=year_deaths.values)
    plt.title('Deaths Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.grid()
    plt.show()
else:
    print("'Year' or 'Deaths' columns not found in the dataset.")

# Analyze historical population vs. deaths (if both columns exist)
if 'Historical_Population' in data.columns and 'Deaths' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data['Historical_Population'], y=data['Deaths'])
    plt.title('Historical Population vs. Deaths')
    plt.xlabel('Historical Population')
    plt.ylabel('Number of Deaths')
    plt.grid()
    plt.show()
else:
    print("'Historical_Population' or 'Deaths' columns not found in the dataset.")

print("Revised analysis complete.")