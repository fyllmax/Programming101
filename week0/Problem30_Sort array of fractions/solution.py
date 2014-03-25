# Imports
from collections import OrderedDict
from operator import itemgetter


# Function
def sort_fractions(fractions):
    fractionsDictionary = {}

    for fraction in fractions:
        fractionsDictionary[fraction] = fraction[0] / fraction[1]

    orderedFractionsDict = OrderedDict(
        sorted(fractionsDictionary.items(), key=itemgetter(1)))

    outputOrderedFractions = []
    for fraction in orderedFractionsDict:
        outputOrderedFractions.append(fraction)

    return outputOrderedFractions


# Main
def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))

# Programe run
if __name__ == '__main__':
    main()
