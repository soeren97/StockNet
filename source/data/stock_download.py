from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd
from datetime import datetime

# googl=yf.Ticker("GOOGL")
# amzn=yf.Ticker("AMZN")
# # type("data") for at se data
# end_date=datetime.today()
# start_date=datetime(2022,1,1)

# stock_data=yf.download("AMZN", start_date, end_date, interval="3mo")
# print(stock_data)
# amzn_hist=amzn.history(start=start_date,end=end_date, interval='2m')
# googl_hist=googl.history(start=start_date,end=end_date, interval='2m')
# print(amzn_hist)
# print(googl_hist)



def dates(test,end_date_unformat=None):
    if not end_date_unformat:
        end_date=datetime.today()
    start_date=datetime(*test) #start_date_unformat
    return start_date, end_date
()
def init_data(start_date,end_date,stock_name,interval):
    return yf.download(stock_name,start_date,end_date,interval = interval)

def init_data_extra(stock_name, start_date,end_date,interval):
    stock_name_Ticker=yf.Ticker(stock_name)
    stock_name_hist=stock_name_Ticker.history(start=start_date,end=end_date,interval=interval)
    return stock_name_hist
test=[2023,1,1]
start_date,end_date= dates(test)

# print(init_data(start_date, end_date, "AMZN", "1mo"))

# print(init_data_extra("GOOGL",start_date,end_date,"1mo"))


class StockLoader:
    def __init__(self,stock_name: str, interval: str) -> None:
        """Initilize variables. 

        Args:
            stock_name (str): Name of company for stock data retrival.
            interval (str): The interval at which the stockdata is retrieved.
        """        
        self.start_date: list[int]|None = None
        self.end_date: datetime = datetime.today()
        self.stock_name: str = stock_name
        self.interval: str = interval

    def dates(self,start_date_unformat: list[int], end_date_unformat: list[int]|None = None) -> None:
        """Calculates the start and end date for the stock data retrival.

        Args:
            start_date_unformat (list[int]): The start date for the stock data retrival.
            end_date_unformat (list[int] | None, optional): The end date for the stock data retival, Defaults to None.
        """        
        if end_date_unformat:
            self.end_date=datetime(*end_date_unformat)
        self.start_date=datetime(*start_date_unformat) #start_date_unformat

    def init_data(self) -> pd.DataFrame:
        """Download stock data.

         Opening, highest, lowest, closing, Adj closing price and volume of the day.

        Returns:
            pd.DataFrame: Download of the price data and volume of the stock.
        """        
        return yf.download(self.stock_name,self.start_date,self.end_date,interval=self.interval)

    def init_data_extra(self) -> pd.DataFrame:
        """Download stock data.
        Opening, highest, lowest, closing, Adj closing price and volume of the day.
        Also includes dividens and stock splits.

        Returns:
            pd.DataFrame: Downloads the price data, volume, dividends and stock splits.
        """        
        stock_name_Ticker=yf.Ticker(self.stock_name)
        stock_name_hist=stock_name_Ticker.history(start=self.start_date,end=self.end_date,interval=self.interval)
        return stock_name_hist


    
    def multiplot_stock_prices(self, data: pd.DataFrame) -> None:
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
        fig.suptitle(f"Stock Prices for {self.stock_name}")

        # Closing Price
        axes[0, 0].plot(data.index, data['Close'], label='Closing Price', color='blue')
        axes[0, 0].set_xlabel('Date')
        axes[0, 0].set_ylabel('Closing Price')
        axes[0, 0].legend()

        # Highest Price
        axes[0, 1].plot(data.index, data['High'], label='Highest Price', color='green')
        axes[0, 1].set_xlabel('Date')
        axes[0, 1].set_ylabel('Highest Price')
        axes[0, 1].legend()

        # Opening Price
        axes[1, 0].plot(data.index, data['Open'], label='Opening Price', color='orange')
        axes[1, 0].set_xlabel('Date')
        axes[1, 0].set_ylabel('Opening Price')
        axes[1, 0].legend()

        # Lowest Price
        axes[1, 1].plot(data.index, data['Low'], label='Lowest Price', color='red')
        axes[1, 1].set_xlabel('Date')
        axes[1, 1].set_ylabel('Lowest Price')
        axes[1, 1].legend()

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

loader_AMZN=StockLoader("AMZN","1mo")
loader_AMZN.dates([2014,1,1], [2023,12,24])
data=loader_AMZN.init_data()
data_extra=loader_AMZN.init_data_extra()

loader_GOOG=StockLoader("GOOGL","1mo")
loader_GOOG.dates([2014,1,1], [2023,12,24])
data=loader_GOOG.init_data()
data_extra=loader_GOOG.init_data_extra()

print(data)
print(data_extra)
loader_GOOG.multiplot_stock_prices(data)
loader_AMZN.multiplot_stock_prices(data)



