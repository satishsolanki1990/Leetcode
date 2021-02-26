"""
1436. Destination City
You are given the array paths,
where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

"""

class Solution:
    def destCity(self, paths):
        '''
        logic: using dictionary to keep track of paths
        '''
        origin = {}
        destination = {}
        for i in paths:
            origin[i[0]] = 1
            destination[i[1]] = 1
            if i[0] in destination:
                # remove i[0]
                destination.pop(i[0], None)
            if i[1] in origin:
                destination.pop(i[1], None)

        return list(destination.keys())[0]

sol=Solution()
paths=[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sol.destCity(paths))