import unittest
from solution import Solution

class ZigzagTestCase(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
    def test_convert_case1(self):        
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        
    def test_convert_case2(self):        
        self.assertEqual(self.solution.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        
    def test_convert_case3(self):        
        self.assertEqual(self.solution.convert('A', 1), 'A')
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ZigzagTestCase('test_convert_case1'))
    suite.addTest(ZigzagTestCase('test_convert_case2'))
    suite.addTest(ZigzagTestCase('test_convert_case3'))
    return suite
    
    
if __name__ == '__main__':
  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite()) 
    