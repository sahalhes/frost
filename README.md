# FuturiStock

We team DevX has decided to make an AI Model which predicts top and bottom performing stocks of the day.
FuturiStock is a stock prediction project that utilizes a momentum investing strategy, incorporating SMA values, EMA values, last volume, and average volume to predict top and bottom-performing stocks with profit/loss predictions.
Statistical arbitrage was employed as an additional analytical approach, specifically focusing on a period of 100 days. This method involves identifying statistical patterns and deviations from historical data over the specified timeframe. By analyzing the statistical relationships between different stocks and market indicators during this 100-day period, the project aims to uncover potential trading opportunities and enhance the overall accuracy of stock predictions. This approach adds a quantitative dimension to the analysis, contributing valuable insights to the comprehensive strategy implemented in FuturiStock.


## Project URL
Visit the project [FuturiStock](#) .

## Technologies Used
- **Python**: Backend development using Flask.
- **HTML**: Frontend structure.
- **CSS**: Styling the frontend.
- **Bootstrap**: Frontend framework for responsive design.
- **JavaScript**: Enhancing frontend interactivity.

## Google Technologies Used
- **Google fonts**: In styling
- **Google colab**: While testing and debugging the AI model
- **Google chart**: For further development of project where graphs are to be plotted


## Principles Behind

- **SMA (Simple Moving Average)**: Technical indicator used in stock analysis.
- **EMA (Exponential Moving Average)**: Weighted moving average used in stock analysis.
- **Average Volume**: The average number of shares traded over a specific period. It is a key metric for assessing market interest in a stock.
- **Last Volume**: The total number of shares traded in the most recent trading session. It provides insights into the current level of market activity for a particular stock.
- **Momentum Strategy**: This strategy utilizes various indicators, including SMA (Simple Moving Average), EMA (Exponential Moving Average), Average Volume, and Last Volume. SMA and EMA serve as technical indicators, providing insights into a stock's price trends over time. Average Volume represents the average number of shares traded, offering a measure of market interest. Last Volume indicates the total shares traded in the most recent session, giving a snapshot of current market activity.
- **Statistical Arbitrage**: This approach focuses on analyzing statistical patterns and deviations over a specific period, typically 100 days. It involves identifying relationships between different stocks and market indicators. By exploring relationships between different stocks and market indicators over this timeframe, the approach aims to uncover potential trading opportunities. 


## How It Works
The FuturiStock project employs a momentum investing strategy, considering SMA values, EMA values, last volume, and average volume to predict the top and bottom-performing stocks. The algorithm evaluates historical stock data and provides profit/loss predictions.

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sahalhes/frost

   Navigate to the project directory.

2. Install dependencies:
    ```bash
   pip install -r requirements.txt

3. Run the Flask application locally:
    ```bash
   python app.py

4. Open your web browser and visit http://localhost:5000 to see the project in action.

## Further Plans

While building this project in short period of time we have encountered a lot of problems and solved it, our next major problem lies in the optimization of algorithm website and making this project more user friendly, hence we have put our plan for our next goals.

### Main Website Navigation:

- Create a user-friendly main website for easy navigation.
- Include features to explore and understand the project.

### Custom Stock Prediction:

- Enable users to enter a specific stock symbol to get its prediction.
- Provide detailed insights into individual stocks.
- The duration of analysis is now set to be 100 days , but we plan to make it custom so that user can input and get the data.

### Algorithm website Optimization:

- Implement optimizations to speed up the prediction process.
- Enhance the efficiency of the algorithm for real-time predictions.

### Graphical Interpretation:

- Incorporate graphical representation of data on the main website.
- Create a separate algorithm website with graphical insights into stock analysis.

