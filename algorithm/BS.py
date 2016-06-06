#support and not or , consider not as a binary operation
#you can input 'school AND teacher OR student NOT you' to search documents have both 'school' and 'teacher', or 'student', which don't have 'you'

class boolsearch:
    def __init__(self):
        # initialize 
        import index
        self.inverse_index = index.index

    def search(self, entry):
        #main bool search, return the final result
        self.entry = entry
        def BSAND(list1, list2):
            #calculate two word on the AND operation
            i = 0
            j = 0
            while i < len(list1) && j <len(list2):
            	if list1[i]["doc"] == list2[j]["doc"]:
            		result.append(list1[i])
            		i = i + 1
            		j = j + 1
            	else:
            		if list1[i]["doc"] < list2[j]["doc"]:
            			i = i + 1
            		else:
            			j = j + 1
            return result

        def BSOR(list1, list2):
            #calculate two word on the OR operation
            i = 0
            j = 0
            while i < len(list1) || j <len(list2):
            	if list1[i]["doc"] == list2[j]["doc"]:
            		result.append(list1[i])
            		i = i + 1
            		j = j + 1
            	else:
            		if list1[i]["doc"] < list2[j]["doc"]:
            			result.append(list1[i])
            			i = i + 1
            		else:
            			result.append(list2[j])
            			j = j + 1
            return result

        def BSNOT(list1, list2):
        	#calculate two word on the NOT operation
        	while i < len(list1) || j <len(list2):
            	if list1[i]["doc"] == list2[j]["doc"]:
            		i = i + 1
            		j = j + 1
            	else:
            		if list1[i]["doc"] < list2[j]["doc"]:
            			result.append(list1[i])
            			i = i + 1
            		else:
            			j = j + 1
            return result

        def Minp(a, aa, b, bb, c, cc):
        	if b > c:
        		d = b
        		dd = bb
        		b = c
        		bb = cc
        		c = d
        		cc = dd
        	if a > b:
        		d = a
        		dd = aa
        		a = b
        		aa = bb
        		b = d
        		dd = bb
        	if a != -1:
        		return a, aa
        	if b != -1:
        		return b, bb
        	return c, cc

        def Maxp(a, aa, b, bb, c, cc):
        	if a < b:
        		if b < c:
        			return c, cc
        		else:
        			return b, bb
        	else:
        		if a < c:
        			return c, cc
        	return a, aa

        text = self.entry
        text.replace(' ','')
        i, ii = Minp(text.find('AND'), 'AND', text.find('OR'), 'OR', text.find('NOT'), 'NOT')
        if i < 0:
        	i = len(text)
        word1 = text[:i]
        text = text[i:]
        result = self.inverse_index.get(word1)
        while len(text) > 0:
        	i, ii = Maxp(text.find('AND'), 'AND', text.find('OR'), 'OR', text.find('NOT'), 'NOT')
            if i != -1:
            	j, jj = Minp(text.find('AND'), 'AND', text.find('OR'), 'OR', text.find('NOT'), 'NOT')
            	text = text[len(jj):]
            	k, kk = Minp(text.find('AND'), 'AND', text.find('OR'), 'OR', text.find('NOT'), 'NOT')
            	if k < 0:
            		k = len(text)
            	word2 = text[:k]
            	text = text[k:]
            	result2 = self.inverse_index.get(word2)
            	if jj == 'AND':
            		result = BSAND(result, result2)
            	if jj == 'OR':
            		result = BSOR(result, result2)
            	if jj == 'NOT':
            		result = BSNOT(result, result2)
            else:
            	break

        return result








