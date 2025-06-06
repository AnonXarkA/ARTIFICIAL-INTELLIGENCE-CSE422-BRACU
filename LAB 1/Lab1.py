try:
    import heapq

    class queue:     #queue class is used to store and manage the priority queue for A*search
        def __init__(self):
            self.towns = []
        def push(self,town,value):  #"push" method adding a city to the queue,
            heapq.heappush(self.towns,(value,town)) 
        def pop(self):                 #"pop" method removing and returning the city with the lowest priority 
            return heapq.heappop(self.towns)[1]
        def ifempty(self):   #"ifempty" method checking if the queue is empty,
            if self.towns == []:
                return True
            else:
                return False
        # def inspect(self):   # this method to printing the contents of the queue.
        #     print(self.towns)                  

    class nodes:   #nodes class is used to store information about cities, with each instance having a city name and distance.
        def __init__(self,town=None,lenght= None):
            self.town = str(town)
            self.lenght = str(lenght)
#A
    city_dict = {}

    def new_dict():
        cit =[]
        distan = []
        file = open("input.txt","r")  #opening and reading from input.txt
        f1 = file.read().splitlines()
        for line in f1:
            l = line.split(" ")
            cit = l[2:len(l):2]  #slicing cities except heuristic city
            distan = l[3::2]  ##slicing distance except heuristic dist

            city1 = l[0]  #heuristic and first city
            for item1,item2 in zip(cit,distan): #used zip function to loop over 2 list at a time
                city2 = item1  #neighboring nodes
                dist = int(item2) #distance from parentnode
                city_dict.setdefault(city1, []).append(nodes(city2,dist))  #taking first city as key and its corresponding city and distance as values
                city_dict.setdefault(city2, []).append(nodes(city1, dist)) # similarly corresponding city, distance from first city will be same .  

    def huris_dict():
        h_dict ={}
        with open("input.txt","r") as file:
            for l in file:
                l = l.strip().split(" ")
                n = l[0].strip()   #heuristic city
                d = int(l[1].strip())  #heuristic distance
                h_dict[n] = d  #storing key and values in the empty dictionary h_dict
            return h_dict

    def heu(n,val): #n = city , val = distance , it is h(n)
        return val[n]

    def staralgo(s,e):
        track = {}   #empty dictionary to storing city paths
        lenght = {} #empty dictionary to storing city distance 
        que = queue()
        he = huris_dict()
        que.push(s,0)  #pushing start city 
        lenght[s]=0
        track[s] =  None
        new_list = []  #total expanded list
        while (que.ifempty()==False):
            now = que.pop()  #poping city from queue as present node
            new_list.append(now)  #appending present node
            if now == e:
                break
            for n in city_dict[now]: #getting all content from dictionary
                path_cost = lenght[now] + int(n.lenght)  #g(n) = path cost to reach a node
                if (n.town not in lenght or path_cost < lenght[n.town]):
                    lenght[n.town] = path_cost #distance of new city = g(n)
                    path1_cost = path_cost + heu(n.town, he) #f(n) = g(n) + h(n)
                
                    que.push(n.town, path1_cost)
                    track[n.town] = now # this loop is for each city which will expanding from start city and this  will repeat untill now = end
        printing(s,e,track,lenght,new_list)

    def printing(s,e,track,lenght,new_list):
        f_path = [] # final path
        x = e
        while track.get(x) != None:
            f_path.append(x)
            x = track[x]
        f_path.append(s)
        f_path.reverse()
        print("Path : " + str(f_path))
        print("Total Distance : " + str(lenght[e])+ "km")               

    def main():
        source = input("Start node: ")
        destination = input("Destination: ")
        while new_dict() == False:
            print("NO PATH FOUND")
        new_dict()
        staralgo(source, destination)

    if __name__ == "__main__" :
        main()           
except:
    print("NO PATH FOUND")