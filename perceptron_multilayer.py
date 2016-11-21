# Universidad de Buenos Aires - Ingenieria.
# Organizacion de Datos.
# Agustin Daniel Palmeira - 90856.
# Perceptron Multilayer.

import cPickle
import os.path
import pandas as pd
from BeautifulSoup import BeautifulSoup

from numpy import *


class PerceptronMultilayer:
    ################################################################################################

    # Constructor:

    # Entry Node: Quantity of entry layer nodes.
    # Hidden Node: Quantity of hidden layer nodes.
    # Out Node: Quantity of the out layer nodes.

    def __init__(self, entry_node, hidden_node, out_node):
        # Arranged neurons at various levels.
        self.hidden_node = hidden_node
        self.out_node = out_node
        self.entry_node = entry_node + 1

        self.ai = ones(self.entry_node)  # Return a new array of given shape and type, filled with ones.
        self.a1 = ones(self.hidden_node)
        self.ao = ones(self.out_node)

        # Weights:
        self.weight1 = random.uniform(-1.0, 1.0, (self.entry_node, self.hidden_node))
        self.weight2 = random.uniform(-1.0, 1.0, (self.hidden_node, self.out_node))

    ################################################################################################

    # Sigmoid Function:

    def sigmoid(self, x):
        return tanh(x)

    ################################################################################################

    # Sigmoid Derivative Function:

    def derivativesigmoid(self, y):
        return 1.0 - pow(y, 2)  # [(Hiperbolic Tangent(x)]'

    ################################################################################################

    def save(self, filename):
        W = [self.weight1, self.weight2]
        cPickle.dump(W, open(filename, 'w'))

    ################################################################################################

    def loadTrainArchive(self, filename):
        W = cPickle.load(open(filename, 'r'))
        self.weight1 = W[0]
        self.weight2 = W[1]

    ################################################################################################

    def evaluate(self, inputs):
        if len(inputs) != self.entry_node - 1:
            raise (ValueError)

        self.ai[0:self.entry_node - 1] = inputs
        self.n1 = dot(transpose(self.weight1), self.ai)
        self.a1 = self.sigmoid(self.n1)
        self.n2 = dot(transpose(self.weight2), self.a1)
        self.ao = self.sigmoid(self.n2)

        return self.ao

    ################################################################################################

    def backPropagation(self, targets, learningfactor):
        if len(targets) != self.out_node:
            raise (ValueError)

        d2 = targets - self.ao
        d1 = dot(self.weight2, d2)

        derivative2fp = self.derivativesigmoid(self.ao) * d2

        change = derivative2fp * reshape(self.a1, (self.a1.shape[0], 1))

        self.weight2 = self.weight2 + learningfactor * change

        derivative1fp = self.derivativesigmoid(self.a1) * d1

        change = derivative1fp * reshape(self.ai, (self.ai.shape[0], 1))

        self.weight1 = self.weight1 + learningfactor * change

        error = sum(0.7 * (targets - self.ao) ** 2)

        return error

    ################################################################################################

    def test(self, entry):
        for p in range(size(entry, axis=0)):
            print (entry[p, :], '->', self.evaluate(entry[p, :]))

    ################################################################################################

    def singletrain(self, inputs, targets):
        self.evaluate(inputs)
        return self.backPropagation(targets, 0.7)

    ################################################################################################

    def trainNetwork(self, entry, output, iterations=1500, N=0.8):

        iteration = 0
        for i in xrange(iterations):
            error = 0.001
            for p in range(size(entry, axis=0)):
                inputs = entry[p, :]
                targets = output[p, :]
                self.evaluate(inputs)
                error = error + self.backPropagation(targets, N)
            if i % 100 == 0 and i != 0:
                print ('error ' + str(error))
                iteration += 1

    ################################################################################################

    def loadcsv(self, path):
        raw_data = pd.read_csv(path, encoding='utf-8', usecols=['Text', 'Prediction'])
        return pd.DataFrame(data=raw_data)

    ################################################################################################


def main():
    print ("Please select an option:")
    print ("")
    print ("1) Generate train archive.")
    print ("2) Load Data & simulation network.")
    print ("3) Delete train archive.")
    print ("4) Quit.")

    ################################################################################################


main()

option = raw_input("Choose an option: ")
continueLoop = True

while continueLoop:
    if option == '1':

            test = PerceptronMultilayer(2, 15, 1)

            dataframe = test.loadcsv("train10lines.csv")
            texts = dataframe.apply(lambda row: row["Text"], axis=1)
            # print(texts)

            # textswithouthtmltags = []
            # for text in texts:
            #    cleantext = BeautifulSoup(text).text
                # print(cleantext)
            #    textswithouthtmltags.append(cleantext)

            # print(textswithouthtmltags)

            splittedreview = []
            splittedreviews = []

            splittedreviewhash = []

            for text in texts:
                splittedreview = text.split(' ')

                for word in splittedreview:
                    wordHash = hash(word)
                    splittedreviewhash.append(wordHash)

                splittedreviews.append(splittedreviewhash)
                # splittedreviewhash = []

            # print(splittedreviewhash)

            entries = ','.join(map(str, splittedreviews))

            # entries = array(splittedreviews)

            result = dataframe.apply(lambda row: row["Prediction"], axis=1)
            results = ','.join(map(str, result))

            test.trainNetwork(entries, results)
            test.test(entries)
            test.save("train.txt")

            # entries = array([[0, 2], [1, 3], [10, 22], [9, 2]])
            # print(entries)

            break

    elif option == '2':
        test = PerceptronMultilayer(2, 15, 1)
        test.loadTrainArchive("train.txt")
        # i.e. ReviewsEntries = array([[0, 2], [3.2, 2.7]])
        # reviewsentries = array(
        #    [[0, 2], [3.2, 2.7]])
        test.test(reviewsentries) #reviewsentries must be loaded the same way as in option 1
        break

    elif option == '3':
        if os.path.exists("train.txt"):
            os.remove("train.txt")
        break

    elif option == '4':
        break
    else:
        print ("")
        raw_input("Select a valid option.")

