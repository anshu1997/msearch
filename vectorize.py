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

def getsim(srstr, parent = root):
	q = [root]
	corpus=[]
	while(q):
		u = q.pop(0)
		#print(u.data['title'])
		if u.data['mimeType'] =='application/vnd.google-apps.folder':
			corpus.append(str(u.data['title']))
		for i in range(len(u.children)):
			q.append(u.children[i])

	vectorizer = TfidfVectorizer(max_features=10000)
	vectorizer.fit(corpus)
	X = vectorizer.transform(corpus)
	#print(vectorizer.get_feature_names())
	srstr=[srstr]
	Y =vectorizer.transform(srstr)
	#print(X.shape)
	#print(Y.shape)
	cosine_similarit = cosine_similarity(Y, X).flatten()
	#print(len(cosine_similarit))
	print("\n")
	for i in range(len(corpus)):
		if cosine_similarit[i]>0.1:
			print(corpus[i],cosine_similarit[i])