import unittest as ut
import numpy as np
import Pephon as pt
class CalcTest(ut.TestCase):
    def setUp(self):
        self.mk=pt.MyClass()
    def test_add(self):
        self.assertEqual(self.mk.Return_k(self.mk.Progression(1,2,3),2),6)
    def test_add1(self):
        self.assertEqual(self.mk.presenceElement
                         (2,self.mk.Progression(1,2,3)),True)
    def test_add3(self):
        self.assertEqual(self.mk.elemReturn
                         (1,self.mk.Progression(1,2,3)),4)
   
        
if __name__ == '__main__':
    import xmlrunner
    runner=xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
