import unittest
from bottle import Bottle



class testBottle(unittest.TestCase):

    


    def testInitNoNegativeCapacity(self):
        self.assertRaises(Exception,Bottle.__init__,-3)
        
    def testCannotSetVolumeWhileClosed(self):
        testBottle =  Bottle(5)
        self.assertRaises(Exception,testBottle.setVolume,3)

    def testCannotSetVolumeLargerThanCapacity(self):
        testBottle =  Bottle(5)
        self.assertRaises(Exception,testBottle.setVolume,6)

    def testGetVolume(self):
        testBottle = Bottle(5)
        testBottle.changeState()
        testBottle.setVolume(3)
        self.assertEqual(testBottle.getVolume(),3)

    def testChangeState(self):
        testBottle = Bottle(5)
        testBottle.changeState()
        self.assertEqual(testBottle.open, True)

            
if __name__ == '__main__':
    unittest.main()