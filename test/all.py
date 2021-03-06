# all.py
# author: Christophe VG

# all unit tests for the utils

import unittest

if __name__ == '__main__':
  tests = [ unittest.TestLoader().loadTestsFromTestCase(test)
            for test in []
          ]

  all_tests = unittest.TestSuite( tests )
  unittest.TextTestRunner(verbosity=1).run(all_tests)
