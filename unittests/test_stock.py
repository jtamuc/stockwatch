from instrument import stock
import unittest

class TestStock(unittest.TestCase):
    def setUp(self):
        self.m_stock = stock('MSFT','9/1/2013','9/2/2013') 
    
    def test_web(self):
        '''
        unittest to see make sure this returns two lists:
           1 = dates
           2 = close price
        '''
    
        output = self.m_stock.get_web_data()
        gold = (['2013-10-02', '2013-10-01'], ['33.92', '33.58'])
        self.assertEqual(gold, output)
    
    "TODO: write a unittest for the plot method"
if __name__ == '__main__':
    unittest.main()
    