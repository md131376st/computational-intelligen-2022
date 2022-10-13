import logging
import random
import itertools
from collections import OrderedDict


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


def findMinWightGreedy(N):
    sortList = sorted(problem(N, 42), key=lambda l: (len(l), l))
    sortList = list(sortList for sortList, _ in itertools.groupby(sortList))
    acceptedList = [False for i in range(N)]
    mySelections = []
    w = 0
    for i in sortList:
        if False in acceptedList:
            if i not in mySelections:
                NewList = False
                for j in i:
                    if not acceptedList[j]:
                        NewList = True
                        acceptedList[j] = True
                if NewList:
                    mySelections.append(i)
                    w += len(i)
            else:
                continue
        else:
            break

    logging.info(
        f"Greedy solution for N={N}: w={w} (bloat={(w - N) / N * 100:.0f}%)"
    )
    logging.debug(f"{mySelections}")


def recursiveCall(sortList, mySelections, j, w, acceptedList, reserveList={}):
    if False in acceptedList:
        if j == len(sortList):
            print(reserveList)
            OrderedDict(reserveList, reverse=True)
            neededNumbers = [i for i, x in enumerate(acceptedList) if not x]
            # for x in reserveList.keys():
            #     for i in sortList[j]:
            #         if
            return w

        count = 0
        for i in sortList[j]:
            if not acceptedList[i]:
                count += 1
        if count == len(sortList[j]):
            mySelections.append(sortList[j])
            w = w + len(sortList[j])
            for i in sortList[j]:
                acceptedList[i] = True
        else:
            if count != 0:
                if count not in reserveList:
                    reserveList[count] =[]
                reserveList[count].append(sortList[j])
        j = j + 1
        return recursiveCall(sortList, mySelections, j, w, acceptedList)
    else:
        return w


def searchSolution(N):
    sortList = sorted(problem(N, 42), key=lambda l: (len(l), l))
    sortList = list(sortList for sortList, _ in itertools.groupby(sortList))
    acceptedList = [False for i in range(N)]
    mySelections = []
    w = recursiveCall(sortList, mySelections, 0, 0, acceptedList)
    logging.info(
        f"recursive solution for N={N}: w={w} (bloat={(w - N) / N * 100:.0f}%)"
    )
    logging.debug(f"{mySelections}")


# searchSolution(10)
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    for N in [5, 10, 20, 100, 500, 1000]:
        findMinWightGreedy(N)
    for N in [ 10, 20, 100, 500, 1000]:
        searchSolution(N)
