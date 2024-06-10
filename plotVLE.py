import pandas as pd
import plotly.express as px

# Load the data from the CSV file
df_vapor = pd.read_csv('./vapor.csv')

# Ensure that the CSV file has columns named 'Temperature (C)' and 'Pressure (bar)'
temperature_c_vapor = df_vapor['Temperature (C)']
pressure_bar_vapor = df_vapor['Pressure (bar)']

# Create the plot using Plotly
fig = px.scatter(df_vapor, x='Temperature (C)', y='Pressure (bar)',
                 title='VLE of CO₂', labels={'Temperature (C)': 'Temperature (℃)', 'Pressure (bar)': 'Pressure (bar)'},
                 template='plotly_white')

# Update layout for better visual appeal
fig.update_layout(
    xaxis=dict(title='Temperature (℃)'),
    yaxis=dict(title='Pressure (bar)'),
    font=dict(family="Arial, sans-serif", size=14),
    title=dict(font=dict(size=18)),
    autosize=True
)

# Save the plot to an HTML file
fig.write_html('CO2VLE.html')

print("Interactive plot saved as CO2VLE.html")