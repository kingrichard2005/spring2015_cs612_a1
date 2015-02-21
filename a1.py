#-------------------------------------------------------------------------------
# Name:        cs612-a1
# Description: Assignment 1 methods for loading data with Numpy
#
# Author:      kingrichard2005
#
# Created:     2015-02-20
# Copyright:   (c) kingrichard2005 2015
# Licence:     MIT
#-------------------------------------------------------------------------------
import numpy as np
import unittest
from tempfile import TemporaryFile

class TestHelper():
   # A test helper class
   def __init__(self, numberOfNumbers = 100, rangeOfEachNumber = 100 ):
      self.tempTestFile    = TemporaryFile();
      self.aBunchOfIntegers = np.random.randint(rangeOfEachNumber, size=numberOfNumbers);
      self.writeABunchOfNumbersToATempFile();

   def writeABunchOfNumbersToATempFile(self):
      try:
         # Writes a bunch of numbers to a temp test file
         np.save(self.tempTestFile, self.aBunchOfIntegers)
         self.tempTestFile.seek(0);
      except:
         print "error in writeABunchOfNumbersToAFile(...)"

class DataManager():
    # Assignment 1 class
    def __init__(self):
        self.OneD        = [];
        self.TwoD        = [[]];
        self.array1      = [[]];
        self.array2      = [[]];
        self.array3      = [[]];
        self.File1Handle = TemporaryFile();
        self.File2Handle = TemporaryFile();
        self.File3Handle = TemporaryFile();

    def method1LoadAFileToOneD( self, aFileObj ):
        try:
            # Method 1
            self.OneD = np.load(aFileObj);
        except:
            print "error in method1LoadAFile(...)"

    def method2CreateTwoD( self, rangeOfRandInts = 100, square_dim = 5 ):
        try:
            # Method 2
            self.TwoD = np.random.random_integers(rangeOfRandInts, size=(square_dim,square_dim));
        except:
            print "error in method2PlaceRandomIntsInSquareMatrix(...)"

    def method3SortOneD( self ):
        try:
          # Method 3
          self.SortOneD = np.sort(self.OneD, kind='mergesort');
        except:
            print "error in method3SortOneD()"

    def method4PartitionTwoD( self, splitNdx1 = 0, splitNdx2 = 2, splitNdx3 = 4 ):
        try:
            # Method 4
            horizontalColumnAxisNdx = 1
            splitArrays = np.split(self.TwoD, [splitNdx1, splitNdx2, splitNdx3], axis = horizontalColumnAxisNdx)
            self.array1 = splitArrays[0];
            self.array2 = splitArrays[1];
            self.array3 = splitArrays[2];
        except:
            print "error in method4PartitionTwoD(...)"

    def method5PlacePartitionsInFiles( self ):
        try:
            np.save(self.File1Handle, self.array1)
            self.File1Handle.seek(0);

            np.save(self.File2Handle, self.array2)
            self.File2Handle.seek(0);

            np.save(self.File3Handle, self.array3)
            self.File3Handle.seek(0);
        except:
            print "error in method5PlacePartitionsInFiles()"

class TestUM(unittest.TestCase):
    # Data Manager tester
    def setUp(self):
        # Arrange: Create a test helper that provides
        # a file with a bunch of integers
        self.ts = TestHelper();
 
    def test_method1_load_a_file(self):
        # Arrange: Create a DataMananger
        dataManager = DataManager();
        # Act: Load a bunch of integers  
        dataManager.method1LoadAFileToOneD(self.ts.tempTestFile); 
        # Assert: 
        expected = self.ts.aBunchOfIntegers;
        result = dataManager.OneD;
        self.assertEqual( np.array_equal(expected,result), True ) 

if __name__ == "__main__":
    unittest.main();
    print "testing complete"
    #ts          = TestHelper();
    #dataManager = DataManager();
    #dataManager.method1LoadAFileToOneD(ts.tempTestFile);
    #dataManager.method2CreateTwoD();
    #dataManager.method3SortOneD();
    #dataManager.method4PartitionTwoD();
    #dataManager.method5PlacePartitionsInFiles()
