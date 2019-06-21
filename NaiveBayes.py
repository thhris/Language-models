def trainer(data):
    ndoc = len(data)

    ##class 0 prior
    ncla0 = 0
    for c in data:
        if(c[1] == '0'):
            ncla0 += 1
    prior = []
    prior.append(ncla0/ndoc)
    print("Prior probabilities")
    print("Class 0 prior probability: " + str(prior[0]))
    
    ##class 1 prior
    ncla1 = 0
    for c in data:
        if(c[1] == '1'):
            ncla1 += 1
    prior.append(ncla1/ndoc)
    print("Class 1 prior probability: " + str(prior[1]) + "\n")

    vocab = []
    f3 = open("sampleTrain.vocab.txt", "r")
    vocab.extend(f3.read().split())

    ##class 0 probability
    bigdoc0 = []
    for c in data:
        if(c[1] == '0'):
            bigdoc0.extend(c[2])
    count0 = {}
    likelihood = {}
    for w in vocab:
        count0[w] = 0
        for wd in bigdoc0:
            if w == wd:
                count0[w] += 1

    print("Class 0 probabilities")
    for w in vocab:
        likelihood[w, 0] = ((count0[w]+1)/(sum(count0.values()) + len(vocab)))
        x = {}
        print("Word:", str(w), "Prob:", str(likelihood[w, 0]))

    ##class 1 probability
    bigdoc1 = []
    for c in data:
        if(c[1] == '1'):
            bigdoc1.extend(c[2])
    count1 = {}
    for w in vocab:
        count1[w] = 0
        for wd in bigdoc1:
            if w == wd:
                count1[w] += 1
    print()
    print("Class 1 probabilities")
    for w in vocab:
        likelihood[w, 1] = ((count1[w]+1)/(sum(count1.values()) + len(vocab)))
        print("Word:", str(w), "Prob:", str(likelihood[w, 1]))
    
    return (prior, likelihood, vocab)

def tester(testdoc, prior, likelihood, vocab):
    sum0 = 1
    sum0 *= prior[0]
    for w in testdoc:
        if w in vocab:
            sum0 *= likelihood[w, 0]
    sum1 = 1
    sum1 *= prior[1]
    for w in testdoc:
        if w in vocab:
            sum1 *= likelihood[w, 1]
    
    return (sum0,sum1)

f1 = open("sampleTrain.txt", "r")
traindata = []
for line in f1:
    traindata.append([(line.split()[0]),(line.split()[1]),(line.split()[2:])])

f2 = open("sampleTest.txt", "r")
testdata = []
for line in f2:
    testdata.append([(line.split()[0]),(line.split()[1]),(line.split()[2:])])

res = trainer(traindata)
print()
correct = 0

for x in range (0,6):
    res2 = tester(testdata[x][2], res[0], res[1], res[2])
    if res2[0] > res2[1]:
        print("d" + str(x+5) + " : 0")
        if testdata[x][1] == '0':
            correct += 1
    else:
        print("d" + str(x+5) + " : 1")
        if testdata[x][1] == '1':
            correct += 1

accuracy = correct / len(testdata)
print("Accuracy:", accuracy)
