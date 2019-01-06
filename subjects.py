subjects = dict()
subjects={
    "transform calculus": ["tc"],
    "soft computing": ["sctie","sct"],
    "regression and time series": ["rstm"],
    "operations research":["or"],
    "design and analysis of algorithms":["daa","algo"],
    "systems programming":["system"],
    "probability statistics":["probstats"],
    "economics":["econ"],
    "cryptography and network security":["crypto"],
    "partial differential equations":["pde"],
    "numerical solutions of pde":["nsopde"],
    "mathematical methods":["mm"],
    "computer organization architecture":["coa"],
    "advanced numerical techniques":["ant"],
    "object oriented system design":["oop","oosd"],
    "linear algebra":["la"]
    #"discrete mathematics":["discrete"],
    #"modern algebra":["modern"],
    #"finite automata",
    #"functional analysis":["functional"],
    #"measure theory":["measure"],
    #"fluid mechanics":["fluid"],
}

def searchterm(srstr) :
    retname=srstr
    for name, namearr in subjects.iteritems():
        flag=0
        for i in namearr:
            if srstr==i:
                retname=name
                flag=1
                break
            if flag==1:
                break
        if flag==1:
            break
    #print(retname)
    return retname