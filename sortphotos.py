# Import libraries
# ---------------------------------------------------------- 
import sys
import os
import shutil
import os.path
import time
 
# Functions
# ---------------------------------------------------------- 
def photoDate(f):
  '''Return year/month on which the given photo was taken'''
  
  cDate = time.ctime(os.path.getmtime(f))
  cDate = time.strptime(cDate, "%a %b %d %H:%M:%S %Y")  
  yr = cDate.tm_year
  mo = cDate.tm_mon

  return yr, mo
 
# Source, destination and error directories (hard inputs) 
# ---------------------------------------------------------- 
sourceDir = '/volume1/photo/dimitrios/tosort'
destDir = '/volume1/photo/dimitrios/'
errorDir = destDir + '/unsorted/'
 
# Initialize array with error files
# ---------------------------------------------------------- 
problems = [ ]
 
# Get all JPEGs in the source directory
# ---------------------------------------------------------- 
photos = os.listdir(sourceDir)
photos = [ x for x in photos if x[-4:] == '.jpg' or x[-4:] == '.JPG' ]

# Initialize directories
# ---------------------------------------------------------- 
lastMonth = 0
lastYear = 0
 
# Create the destination folder (if necessary)
# ---------------------------------------------------------- 
if not os.path.exists(destDir):
  os.makedirs(destDir)
if not os.path.exists(errorDir):
  os.makedirs(errorDir)

# Copy photos into year and month subfolders. 
# ---------------------------------------------------------- 
for photo in photos:

  original = sourceDir + '/' + photo
  yr, mo = photoDate(original)

  # Check processing year and month
  # -------------------------------------------------------- 
  if not lastYear == yr or not lastMonth == mo:
    sys.stdout.write('\nProcessing %04d-%02d...' % (yr, mo))
    lastMonth = mo
    lastYear = yr
  else:
    sys.stdout.write('.')
  
  # Generate/Select destination sub-directory
  # -------------------------------------------------------- 
  thisDestDir = destDir + '/%04d/%02d' % (yr, mo)
  if not os.path.exists(thisDestDir):
    os.makedirs(thisDestDir)
  
  # Move files
  # -------------------------------------------------------- 
  try: 
    shutil.move(original, thisDestDir)
  except:
    shutil.move(original, errorDir + photo)  
