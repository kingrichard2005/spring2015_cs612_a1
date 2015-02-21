import numpy as np
from tempfile import TemporaryFile

class TestHelper():
   # A test helper class
   def __init__(self, numberOfNumbers = 100, rangeOfEachNumber = 100 ):
      self.tempTestFile    = TemporaryFile();
      self.aBunchOfNumbers = np.random.randint(rangeOfEachNumber, size=numberOfNumbers);
      self.writeABunchOfNumbersToAFile();

   def writeABunchOfNumbersToAFile(self):
      try:
         # Writes a bunch of numbers to a temp test file
         np.save(self.tempTestFile, self.aBunchOfNumbers)
         self.tempTestFile.seek(0);
      except:
         print "error in writeABunchOfNumbersToAFile(...)"

class DataManager():
   # Assignment 1 class
   def __init__(self, inFileObject):
      # TODO: factor methods out of DataManager class initializer
      # Method 1
      self.OneD     = np.load(inFileObject);
      # Method 2
      self.TwoD     = np.random.random_integers(100, size=(5,5))
      # Method 3
      self.SortOneD = np.sort(self.OneD, kind='mergesort');
      # Method 4
      splitNdx1     =  0
      splitNdx2     =  2
      splitNdx3     =  4
      splitArrays   = np.split(self.TwoD, [splitNdx1, splitNdx2, splitNdx3], axis = 1)
      self.array1   = splitArrays[0];
      self.array2   = splitArrays[1];
      self.array3   = splitArrays[2];

if __name__ == "__main__":
    try:
       ts          = TestHelper()
       dataManager = DataManager( ts.tempTestFile )
    except:
        print "error in a1.main"