#support and not or , consider not as a binary operation
#you can input 'school AND teacher OR student NOT you' to search documents have both 'school' and 'teacher', or 'student', which don't have 'you'
import nltk

class boolsearch:
    def __init__(self):
        # initialize 
        import index
        self.inverse_index = index.index
        # self.inverse_index = {}
        self.logical_words = set(["'AND'", "'OR'", "'NOT'"])
        self.stemmer = nltk.PorterStemmer()

    def _BSOR(self, list1, list2):
        return list(set(list1 + list2))

    def _BSNOT(self, list1, list2):
        return list(set(list1) - set(list2))

    def _BSAND(self, list1, list2):
        #calculate two word on the AND operation
        i = 0
        j = 0
        list1.sort()
        list2.sort()
        result = []
        while i < len(list1) and j <len(list2):
            if list1[i] == list2[j]:
                result.append(list1[i])
                i = i + 1
                j = j + 1
            else:
                if list1[i] < list2[j]:
                    i = i + 1
                else:
                    j = j + 1
        return result

    def search(self, entry, k):
        #main bool search, return the final result
        self.entry = entry
        text = self.entry.split(" ")
        result = []
        logic = "'OR'"  # and the first word
        for word in text:
            word = self.stemmer.stem(word)
            if word in self.logical_words:
                logic = word
            else:
                new_index = self.inverse_index.get(word)
                if new_index:
                    result2 = [x["doc"] for x in new_index]
                    if logic == "'AND'":
                        result = self._BSAND(result, result2)
                    if logic == "'OR'":
                        result = self._BSOR(result, result2)
                    if logic == "'NOT'":
                        result = self._BSNOT(result, result2)
        if k > len(result):
            k = len(result)
        print k
        return result[:k]

if __name__ == '__main__':
    bs = boolsearch()
    print bs.search("schools 'AND' you")
    # print bs.search("school 'AND' teacher 'NOT' student 'OR' you")
