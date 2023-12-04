import unittest
import math
from add import addNumbers



class testAddingNumbers(unittest.TestCase):

    testCases = [
        (1,2,3),
        (1.5,1.5,3),
        (0.2,1,1.2)

    ]


    def test(self):
        for case in self.testCases:
            self.assertEqual(addNumbers(case[0],case[1]),case[2])

    def testComplex(self):
        testA = complex(3,5)
        testB = complex(4,5)
        result = testA + testB
        self.assertEqual(addNumbers(testA,testB),result)
    
    def testIEEE(self):
        testNumber = 0;
        testNumber = addNumbers(testNumber,0.1)
        testNumber = addNumbers(testNumber,0.1)
        testNumber = addNumbers(testNumber,0.1)
        self.assertTrue(math.isclose(testNumber,0.3))
        testNumber = 0;
        for i in range(10):
            testNumber = addNumbers(testNumber,0.1)
        self.assertTrue(math.isclose(testNumber,1))
        
if __name__ == '__main__':
    unittest.main()