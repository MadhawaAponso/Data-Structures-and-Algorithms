class TreeNode:
    def __init__(self,data, childern = []):
        self.data = data
        self.childern = childern
        
    def __str__(self,level = 0):
        s = " "* level + (self.data) +"\n"
        for x in self.childern:
            s += x.__str__(level+1)
        return s
    def Add_to_list(self , new_node):
        self.childern.append(new_node)
        
drinks = TreeNode("drinks",[])
cold = TreeNode("cold",[])
hot = TreeNode("hot",[])
tea = TreeNode("tea",[])
coffee = TreeNode("coffee",[])
cola = TreeNode("cola",[])
fanta = TreeNode("fanta",[])

drinks.Add_to_list(cold)
drinks.Add_to_list(hot)
hot.Add_to_list(tea)
hot.Add_to_list(coffee)
cold.Add_to_list(cola)
cold.Add_to_list(fanta)

print(drinks)

        

        