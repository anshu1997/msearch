from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pickle
from head import *

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

## FUNCTIONS---------------------------------------------------------------------------------------------------

## To display contents of a particular folder
def ListFolder(parent):
  file_list=[]
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
  for f in file_list:
    if f['mimeType']=='application/vnd.google-apps.folder': # if folder
        #filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
        print('Folder title: %s, id: %s' % (f['title'], f['id']))
    else:
        #filelist.append({"title":f['title'],"title1":f['alternateLink']})
        print('File title: %s, id: %s' % (f['title'], f['id']))
  return file_list

## To make tree from parent
def maketree(parent):
  currObj=parent
  if (parent.data['mimeType']!='application/vnd.google-apps.folder'):
    return currObj
  
  file_list=[]
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent.data['id']}).GetList()
  for child in file_list:
    if (child['mimeType']=='application/vnd.google-apps.folder'):
      typ=0
    else:
      typ=1
    print('title: %s' % (child['title']))
    currChild=maketree(Node(child,typ))
    currObj.add_child(currChild)
  return currObj
#--------------------------------------------------------------------------------------------------------------

## Search for MNC folder in drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  if (file1['title']=="MNC2020"):
  	myroot=file1
  	break
print('title: %s, id: %s' % (myroot['title'], myroot['id']))
myroot=Node(myroot,0)

## Build Tree from MNC folder
mytree=maketree(myroot)
# print("\n")
# str(mytree)
# print(mytree)

## SAVE in file
file_pi = open('driveTree.obj', 'w')
pickle.dump(mytree, file_pi)