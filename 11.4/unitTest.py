import unittest
import random
import time
from queue import Queue



class testQueue(unittest.TestCase):

    testCases = [
        (1,1),
        (11,11),
        (444,444),
        (3,3)
    ]

    def testAssertIn(self):
        testQueue = Queue()
        for case in self.testCases:
            testQueue.add(case[0])
            self.assertIn(case[1],testQueue)

    def testRuntime(self):
        testQueue = Queue()
        for i in range(1000000):
            testQueue.add(random.randint(1,999))
        startTime = time.time()
        testQueue.count(186)
        endTime = time.time()
        executionTime = (endTime-startTime) * 1000
        self.assertTrue(executionTime < 500)        
    


            
if __name__ == '__main__':
    unittest.main()