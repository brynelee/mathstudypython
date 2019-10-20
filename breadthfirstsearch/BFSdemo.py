class Node:
    def __init__(self, number):
        self.num = number
        self.nodes = []

    def setNode(self, num):
        if(self.nodes.__contains__(num) == False):
            node = Node(num)
            self.nodes.append(node)
            return node
        else:
            return None

    def setNodeUnder(self, num, base):
        if (self.num == num):
            return self.setNode(num)

        baseNode = self.get(base, self.nodes)
        if baseNode == None:
            return None
        else:
            return baseNode.setNode(num)

    def get(self, num, nodes=None):
        if(self.nodes == None or len(nodes) == 0):
            return None
        else:
            someNodes = []
            for node in nodes:
                if node.num == num:
                    return node
                for n in node.nodes:
                    someNodes.append(n)
            return self.get(num, someNodes)
    
    def search(self):
        print(self.num)
        self.printNodes(self.nodes)

    def printNodes(self, nodes=None):
        if nodes == None or len(nodes) == 0:
            return
        else:
            someNodes = []
            for node in nodes:
                print(node.num)
                for n in node.nodes:
                    someNodes.append(n)
            return self.printNodes(someNodes)

if __name__ == "__main__":
    
    root = Node(110)
    root.setNode(123)
    root.setNode(879)
    root.setNode(945)
    root.setNode(131)
    root.setNodeUnder(162, 123)
    root.setNodeUnder(587, 123)
    root.setNodeUnder(580, 945)
    root.setNodeUnder(762, 945)
    root.setNodeUnder(906, 131)
    root.setNodeUnder(681, 587)

    root.search()