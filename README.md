# ARTIFICIAL-INTELLIGENCE-CSE422-BRACU



# ✈️ CSE422 - Lab Assignment 01: A* Search Algorithm

---

[![](https://i.ibb.co/7dzhK4KC/Screenshot-82.png)](https://imgbb.com/)


## 🧩 PROBLEM SCENARIO

On holiday, a flight currently wants to travel to **Bucharest** from **Arad**. But there is no direct way to Bucharest from Arad. However, the cities are connected with each other like a graph. The distance between the connected cities are given.

The flight wants to travel through the most optimal way. To find the optimal path to travel, another information is provided: the straight line distance between any city and the final destination (Bucharest).  

Now apply **A\*** search to determine the most optimal value for the route **Arad to Bucharest** and help the flight. You have to use the straight line distance as the **heuristic** value for the cities.

---

## 🏙️ City Heuristic Table

| City        | Heuristic | City        | Heuristic |
|-------------|-----------|-------------|-----------|
| Arad        | 366       | Mehadia     | 241       |
| Bucharest   | 0         | Neamt       | 234       |
| Craiova     | 160       | Oradea      | 380       |
| Eforie      | 161       | Pitesti     | 100       |
| Fagaras     | 176       | Rimnicu Vilcea | 193     |
| Dobreta     | 242       | Timisoara   | 329       |
| Hirsova     | 151       | Urziceni    | 80        |
| Iasi        | 226       | Vaslui      | 199       |
| Lugoj       | 244       | Zerind      | 374       |

---

## 🔠 City Abbreviations (For Simplicity)

| City           | Abbreviation | City           | Abbreviation |
|----------------|--------------|----------------|--------------|
| Arad           | A            | Neamt          | F            |
| Bucharest      | Z            | Oradea         | B            |
| Craiova        | S            | Pitesti        | P            |
| Eforie         | T            | Rimnicu Vilcea | R            |
| Fagaras        | O            | Timisoara      | C            |
| Dobreta        | V            | Urziceni       | D            |
| Hirsova        | N            | Vaslui         | H            |
| Iasi           | Q            | Zerind         | E            |
| Lugoj          | G            | Mehadia        | L            |

---

## 📥 INPUTS

Your `.txt` file should take each node followed by each destination it can reach and their corresponding distance and heuristics.

You are to read the file, then ask the user to input the **starting** and the **destination** point.

---

## 📤 OUTPUTS

The output will contain:

- The total distance from the starting point to the destination  
- The nodes it followed to calculate the distance

---

## 📝 SAMPLE INPUT

In the text file:

```
Arad 366 Zerind 75 Sibiu 140 Timisoara 118
Zerind 374 Arad 75 Oradea 71
Oradea 380 Zerind 71 Sibiu 151
...
Bucharest 0 Pitesti 101 Fagaras 211 Giurgiu 90 Urziceni 85
Giurgiu 77 Bucharest 90
...
```

Each line starts with a node followed by the **heuristic** of that node.  
Then the neighboring nodes and the distance from the parent node is given as a pair.  
All neighboring city-distance pairs are listed after the heuristic.

> For example, the text file starts with Arad which has a heuristic of 366.  
> It is the parent node to Zerind, Sibiu and Timisoara which are 75, 140 and 118 km away from Arad.  
> Notice that since Bucharest is the End node, it has a heuristic of 0.

---

## 🖥️ CONSOLE EXAMPLE

```
Start node: Arad
Destination: Bucharest
```

---

## ✅ Sample Output

```
Path: Arad -> Sibiu -> Rimnicu -> Pitesti -> Bucharest
Total distance: 418 km
```

---

## 🚫 If No Path Exists

If there is no path found from the Start node to the End node, simply print:

```
NO PATH FOUND
```
