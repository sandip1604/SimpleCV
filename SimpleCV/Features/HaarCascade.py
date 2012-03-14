from SimpleCV.base import *

class HaarCascade():
     _mCascade = None
     _mName = None
     def __init__(self, fname, name=None):
          if( name is None ):
               self._mName = fname
          else:
               self._mName = name
               
          if (not os.path.exists(fname)):
               warnings.warn("Could not find Haar Cascade file " + fname)
               return None
          self._mCascade = cv.Load(fname)

     def load(self, fname, name = None):
          if( name is None ):
               self._mName = fname
          else:
               self._mName = name
               
          if (not os.path.exists(fname)):
               warnings.warn("Could not find Haar Cascade file " + fname)
               return None

          self._mCascade = cv.Load(fname)

     def getCascade(self):
          return self._mCascade

     def getName(self):
          return self._mName
    
     def setName(self,name):
          self._mName = name
