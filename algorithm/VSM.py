import math
class VSM:
    Lengths = {}
    inverse_index = {}

    def _calcWtd(self, frequence, df):
        if df == self.N:
            result = 0
        elif frequence == 0:
            result = 0
        else:
            result = (1 + math.log(frequence, 2)) * math.log(float(self.N) / df, 2)
        return result

    def __init__(self, Number=21576):
        # initialize using the inverse index, and total documents number.
        self.N = Number
        import index
        self.inverse_index = index.index
        for word in self.inverse_index:
            for record in self.inverse_index[word]:
                if record["doc"] in self.Lengths:
                    self.Lengths[record["doc"]] += self._calcWtd(record["frequence"], len(self.inverse_index[word]))**2
                else:
                    self.Lengths[record["doc"]] = self._calcWtd(record["frequence"], len(self.inverse_index[word]))**2
        for docID in self.Lengths:
            self.Lengths[docID] = self.Lengths[docID]**0.5

    def search(self, query, K=21576):
        # input a query and disired number of top results. ouput a array of docID
        queryWords = query.split(" ")
        Scores = {}
        for word in queryWords:
            if word in self.inverse_index:
                for record in self.inverse_index[word]:
                    if record["doc"] in Scores:
                        Scores[record["doc"]] += self._calcWtd(record["frequence"], len(self.inverse_index[word]))
                    else:
                        Scores[record["doc"]] = self._calcWtd(record["frequence"], len(self.inverse_index[word]))
        for docID in Scores:
            Scores[docID] /= float(self.Lengths[docID])
        sort = sorted(Scores.items(), key = lambda e: e[1], reverse = True)
        if K < len(sort):
            small = K
        else:
            small = len(sort)
        result = []
        for index in range(small):
            result.append(sort[index][0])
        return result
