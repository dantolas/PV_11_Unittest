import unittest
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

    def testOnlyAddsNumbers(self):
        self.assertRaises(Exception,addNumbers,"Yeet","Yeet")
        
if __name__ == '__main__':
    unittest.main()