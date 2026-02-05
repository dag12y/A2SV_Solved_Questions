class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """        
        store={}
        for s in cpdomains:
            temp=s.split(" ")
            dots=[]
            for i,letter in enumerate(temp[1]):
                if letter == '.' : dots.append(i)
            domains=[temp[1][i+1:] for i in dots]
            domains.append(temp[1])
            for domain in domains:
                if domain in store:
                    store[domain]=store[domain]+int(temp[0])
                else:
                    store[domain]=int(temp[0])
        
        result =[]
        for key,value in store.items():
            result.append(str(value)+" "+key)
        
        return result

