from datetime import datetime
import unittest
class TestStock(unittest.TestCase):

    def check_date(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def test_StartDate(self):
        date = '2023-08-23'
        self.assertTrue(self.check_date(date))
        
    def test_EndDate(self):
        date = '2023-08-30'
        self.assertTrue(self.check_date(date))

    def test_TimeSeries(self):
        series = ['1', '2', '3', '4']

        for x in series:
            self.assertTrue(x.isdigit() and 1 <= int(x) <= 4)

    def test_ChartType(self):
        charts = ['1', '2']
        for chart in charts:
            self.assertTrue(chart.isdigit() and (chart == '1' or chart == '2'))
    def test_Symbol(self):
        symbols = ["AAPL", "IBM", "ABR", "MSFT", "TSLA", "NVDA"]
        for symbol in symbols:
            self.assertTrue(symbol.isupper() and len(symbol) > 1 and len(symbol) < 7)

if __name__ == '__main__':
    unittest.main()