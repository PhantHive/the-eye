class NGram:
    def __init__(self, sentence, N=1, language='french'):
        self.sentence = sentence
        self.language = language
        self.N = N
        self.tokenizedSentence = [sentence]

    def ngram(self):
        if isinstance(self.N, int):

            tuplesList = []
            for list in self.tokenizedSentence:
                sublist = []
                for w in list:
                    subsublist = []
                    for i in range(self.N + 1):
                        try:
                            subsublist.append(list[list.index(w) + i])
                        except(IndexError):
                            pass

                    sublist.append(tuple(subsublist))

                for w in reversed(list):
                    subsublist = []
                    if list.index(w) != 0:
                        for i in range(self.N + 1):
                            try:
                                subsublist.append(list[list.index(w) - i])
                            except(IndexError):
                                pass

                        sublist.append(tuple(subsublist))
                tuplesList.append(sublist)
            return tuplesList


