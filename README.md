
# Commodity Price Visualization

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project provides visualizations for analyzing the daily prices of various commodities across different markets in India. The dataset includes information on commodity names, market locations, dates, and the prices (minimum, maximum, and modal) recorded for each commodity. These visualizations aim to provide insights into price trends, comparisons across markets, and regional price variations.

## Dataset
The dataset contains the following columns:
- **State**: The state in which the market is located.
- **District**: The district where the market is located.
- **Market**: The market name where commodity prices were recorded.
- **Commodity**: The name of the commodity (e.g., wheat, rice).
- **Variety**: The specific variety of the commodity.
- **Grade**: The grade or quality of the commodity.
- **Arrival_Date**: The date when the prices were recorded.
- **Min_x0020_Price**: The minimum price for the commodity on that day in the market.
- **Max_x0020_Price**: The maximum price for the commodity on that day in the market.
- **Modal_x0020_Price**: The most common price for the commodity on that day in the market (often used as a representative price).

## Features
- **Line Chart**: Track commodity price trends over time.
- **Bar Chart**: Compare prices of commodities across different markets.
- **Box Plot**: Analyze price distributions for a commodity across markets or districts.
- **Heatmap**: Visualize price variations across states or districts.
- **Scatter Plot**: Correlate prices of different commodities across markets or time.

## Installation
To set up the project locally, follow these steps:

### Prerequisites
- Python 3.x
- Required Python libraries: `matplotlib`, `pandas`, `seaborn`, `plotly`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/csePriyanshu/commodity-price-visualization.git
   cd commodity-price-visualization
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the dataset and place it in the `data/` directory, or update the path in the script.

## Usage
1. **Load the Dataset**: 
   Ensure the dataset is in CSV format and placed in the `data/` folder. Update the dataset path in the script if necessary.

2. **Run the Visualization Scripts**: 
   Generate different types of visualizations by running the provided Python scripts. 
   For example, to generate a line chart for a specific commodity:
   ```bash
   python line_chart.py
   ```

3. **Available Scripts**:
   - `line_chart.py`: Generates line charts for commodity price trends over time.
   - `bar_chart.py`: Compares commodity prices across different markets.
   - `box_plot.py`: Displays the price distribution across markets.
   - `heatmap.py`: Visualizes price variations across states or districts.
   
4. **View the Visualizations**: 
   The visualizations will either be displayed interactively or saved in the `output/` folder.

## Visualizations
Here are some example visualizations you can generate with this project:

- **Line Chart**: Track commodity prices (e.g., Modal Price) over time across markets.
  ![Line Chart Example](images/line_chart_example.png)

- **Bar Chart**: Compare the maximum prices of a commodity across multiple markets.
  ![Bar Chart Example](images/bar_chart_example.png)

- **Box Plot**: Show the price distribution of commodities across different districts or states.
  ![Box Plot Example](images/box_plot_example.png)

- **Heatmap**: Visualize the variation of prices (e.g., modal prices) across states for specific commodities.
  ![Heatmap Example](images/heatmap_example.png)

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

For any questions or suggestions, feel free to open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
