import pickle
from head import *
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from sklearn.metrics.pairwise import cosine_similarity
file_pi = open('driveTree.obj', 'r')
mytree = pickle.load(file_pi)

#str(mytree)
#print(mytree)
root=Node(0,0)
root=mytree
   
def bfs(srstr,parent=root) :
	#Initializing queue
    q = [parent]
    corpus=[]
    while(q):
    	u = q.pop(0)
    	if u.data['mimeType'] =='application/vnd.google-apps.folder':
			corpus.append(str(u.data['title']))
        for i in range(len(u.children)):
			q.append(u.children[i])
        
    vectorizer = TfidfVectorizer(max_features=10000)
    vectorizer.fit(corpus)

    srstr=[srstr]
    Y = vectorizer.transform(srstr)

# GET Folder
    q = [parent]

    while(q):
    	u = q.pop(0)
    	levelstr = [str(u.data['title'])]
    	X = vectorizer.transform(levelstr)
    	cosine_similarit = cosine_similarity(Y, X).flatten()
    	if cosine_similarit>0.3: #Threshold for selecting folder
    		break
    	for i in range(len(u.children)):
    		q.append(u.children[i])

# GET Sub-Folder
    flag = 0
    q = []
    newroot = u
    #Append the children of u to q
    for i in range(len(u.children)):
    	q.append(u.children[i])
    while(q):
        u = q.pop(0)
        if u.data['mimeType'] =='application/vnd.google-apps.folder':
            levelstr = [str(u.data['title'])]
            X = vectorizer.transform(levelstr)
            cosine_similarit = cosine_similarity(Y, X).flatten()
            if cosine_similarit>0.3:
                print("%s %f" % (levelstr, cosine_similarit))
                flag = 1
                break
        for i in range(len(u.children)):
    	    q.append(u.children[i])
    
    if flag==1:
    	newroot = u

    q = [newroot]
    listlink=[]
    while(q):
		u = q.pop(0)
		if u.data['mimeType'] !='application/vnd.google-apps.folder':
			listlink.append(u.data)
		for i in range(len(u.children)):
			q.append(u.children[i])
    return listlink

#strr="Probability Statistics"
#bfs(root,strr)
