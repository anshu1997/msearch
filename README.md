# msearch
<b>Utility : </b> Search a particular Google Drive folder for notes, lectures, assignments and books related to a course.<br><br>
![img1](https://github.com/anshu1997/msearch/blob/master/img1.gif)
<br>
### Overview
• <b>auth.py :</b> After verification of drive credentials, a directory tree of the corresponding folder is built by performing a BFS traversal and is stored as <b>driveTree.obj</b><br>
• <b>disp.py :</b> Once a user query is passed, the request is sent to /result endpoint, where the list of links are displayed. These links are basically the desired drive files. <br> How to get this list of links?&nbsp As of now, a <b>cosine similarity</b> score decides whether to enter a particular sub-folder, i.e. go down the branch of the directory tree to fetch the required files. The threshold for cosine similarity between the query and sub-folder names is set to 0.3
