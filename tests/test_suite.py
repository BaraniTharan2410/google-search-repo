import unittest
from tests.home.home_test import HomeTests

#get test from all the classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTests)

#create test suite combining all the testcases
smoke_test = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smoke_test)