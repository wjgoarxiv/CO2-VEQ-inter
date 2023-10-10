import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import mpld3

def rcparams():
    rcParams['figure.figsize'] = 5, 4
    rcParams['font.family'] = 'sans-serif'

    # Check whether Arial or SF Pro Display are installed in the computer
    try:
        rcParams['font.sans-serif'] = ['SF Pro Display']
    except:
        try:
            rcParams['font.sans-serif'] = ['Arial']
        except:
            print("ERROR Note that Arial and SF Pro are not installed in the computer. The program will use the default font.")
            pass

    # Label should be far away from the axes
    rcParams['axes.labelpad'] = 8
    rcParams['xtick.major.pad'] = 7
    rcParams['ytick.major.pad'] = 7

    # Add minor ticks
    rcParams['xtick.minor.visible'] = True
    rcParams['ytick.minor.visible'] = True

    # Tick width
    rcParams['xtick.major.width'] = 1
    rcParams['ytick.major.width'] = 1
    rcParams['xtick.minor.width'] = 0.5
    rcParams['ytick.minor.width'] = 0.5

    # Tick length
    rcParams['xtick.major.size'] = 5
    rcParams['ytick.major.size'] = 5
    rcParams['xtick.minor.size'] = 3
    rcParams['ytick.minor.size'] = 3

    # Tick color
    rcParams['xtick.color'] = 'black'
    rcParams['ytick.color'] = 'black'

    rcParams['font.size'] = 14
    rcParams['axes.titlepad'] = 10
    rcParams['axes.titleweight'] = 'normal'
    rcParams['axes.titlesize'] = 18

    # Axes settings
    rcParams['axes.labelweight'] = 'normal'
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['axes.labelsize'] = 16
    rcParams['xtick.direction'] = 'in'
    rcParams['ytick.direction'] = 'in'

# Load the data from the CSV files
df_vapor = pd.read_csv('./vapor.csv')

# Ensure that the CSV files have columns named 'Temperature (C)' and 'Pressure (bar)'
temperature_c_vapor = df_vapor['Temperature (C)']
pressure_bar_vapor = df_vapor['Pressure (bar)']

# Create the plot
fig, ax1 = plt.subplots()

# Assign attributes
rcparams()

color = 'black'
ax1.set_xlabel(r'Temperature (℃)')
ax1.set_ylabel('Pressure (bar)', color=color)
ax1.scatter(temperature_c_vapor, pressure_bar_vapor, color=color, s=2, linestyle='solid', marker='o')
ax1.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # to ensure the right y-label is not slightly clipped
plt.title(r'VLE of CO₂')
plt.grid(True)
plt.tight_layout()

# Convert the plot to an interactive HTML object using mpld3
mpld3.save_html(fig, 'vapor.html')