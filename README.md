# ARTIFICIAL-INTELLIGENCE-CSE422-BRACU

# 🛡️ EEE472/CSE422 - Artificial Intelligence 

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




|







|









 
# Lab Assignment 02: Alpha-Beta Pruning

---

## 📘 Problem Statement

Assume that there are two teams and they are team attacker and team defender. Therefore, at a state of the game one agent in each team is left alive respectively. Here, the defender is given a lifeline called **HP** which will be assigned randomly. 

Furthermore:

- The **attacker** agent will try to give **maximum negative HP** to the defender agent to decrease his (defender’s) chances of survival in the game.  
- The **defender** agent will try to protect himself by receiving the **lowest negative HP** possible from the attacker agent.  
- The attacker can choose from a number of bullets from his gun.  
- Each bullet (move) will cost a certain **maximum negative HP**, randomly assigned within a given range (min, max).

---

You need to implement the **Alpha-Beta Pruning algorithm** to determine the optimal damage outcome.

---

## 🧪 Sample Input 1

```
1. Enter your student id:
17301106

2. Minimum and Maximum value for the range of negative HP:
1 30
```

### Sample Input 1 Explanation

- Ex. 1 (17301106): Use 1st digit of your BRACU student ID  
  → **Number of turns for the attacker agent**  
- Ex. 60 (17301106): Use last 2 digits of your student ID in reverse  
  → **Initial lifeline (HP) for the defender**  
- Ex. 3 (17301106): Use semester code (3rd digit of your student ID)  
  → **Number of bullets (branching factor)**  
- Ex. 1 30: Minimum and maximum range of negative HP values

---

## ✅ Sample Output 1

```
1. Depth and Branches ratio is 2:3
2. Terminal States (leaf node values) are 19,22,9,2,26,16,16,27,16.
3. Left life(HP) of the defender after maximum damage caused by the attacker is 44
4. After Alpha-Beta Pruning Leaf Node Comparisons 7
```

---

### Sample Output 1 Explanation

```
(Application of Alpha-Beta Pruning Algorithm)

MAX   - Level 0 (Attacker’s Turn / Initial Start)       → MAX utility / Best Choice
MIN   - Level 1 (Defender’s Turn)                       → 3 branches
LEAVES - Level 2 (Terminal State)                       → 3^2 = 9 leaf nodes

Terminal Node Values: [19, 22, 9, 2, 26, 16, 16, 27, 16]

Left Life = (60 - 16) = 44
```

> Formula: `Left life HP = Initial life HP - MAX negative HP`  
> Hint: Terminal nodes are randomly generated values within the given range of negative HP.

---

## 🧪 Sample Input 2

```
1. Enter your student id:
20201003

2. Minimum and Maximum value for the range of negative HP:
5 20
```

---

## ✅ Sample Output 2

```
1. Depth and Branches ratio is 4:2
2. Terminal States(Leaf Nodes) are 18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18.
3. Left life(HP) of the defender after maximum damage caused by the attacker is 22
4. After Alpha-Beta Pruning Leaf Node Comparisons 13
```

|




|



# Lab Assignment 3

## 🏦 Strange Bank Problem: Genetic Algorithm

---

## 🧩 Problem Description

Suppose, you are the owner of a bank that operates in a strange way.
Customers can lend money from your bank (just like a normal bank) and
they can also deposit money in your bank. A register is maintained to track
the daily transactions. However, being the strange owner of a strange bank,
you have a fascination with finding out whether a portion of your daily
transactions (in/out) balance out to zero.



---

### 🧾 Example:



For example, given the following transaction log:

| Transaction ID | Type    | Amount |
| :------------- | :------ | :----- |
| 1              | Lend    | 100    |
| 2              | Deposit | 150    |
| 3              | Lend    | 400    |
| 4              | Lend    | 500    |
| 5              | Deposit | 1000   |
| 6              | Lend    | 460    |
| 7              | Deposit | 160    |
| 8              | Deposit | 200    |
| 9              | Lend    | 500    |
| 10             | Deposit | 100    |

In this case, there is a portion of the transactions that would balance itself
out. (6th, 7th, 8th, and 10th transactions would amount to 0).

---
## 🤖 Your Task: Use a Genetic Algorithm

### Task Breakdown:

1. **Model** the transaction register in a way suitable for the problem.
2. Write a **fitness function**.  
   > Hint: It is the **sum of the non-zero elements** of a register.
3. Write the **crossover function**.
4. Write the **mutation function**.
5. Create a **population** of randomly generated registers.
6. Run the **genetic algorithm** on the population until:
   - Highest fitness is reached  
   **OR**
   - Maximum iterations have been reached.

---

## 📥 Input

- The **first line** has a number `N` denoting the number of daily transactions.  
- The following `N` lines each start with:
  - `l` (for Lend)
  - `d` (for Deposit)
  - Followed by an integer `S` denoting the amount of transaction.

**Constraints:**

- `1 ≤ N ≤ 10^2`
- `1 ≤ S ≤ 10^5`

---

## 📤 Output

The output would be a binary string denoting the specific transactions that
balance themselves to zero or -1 if such a string cannot be formed. String
consisting of all zeros won’t be accepted.



## 🧪 Sample Input 1
```
7
l 120
l 289
d 475
l 195
d 6482
l 160
d 935
```
## 🧪 Sample Output 1

1011010

## 🧪 Sample Input 2
```
5
l 100
l 450
d 500
l 7923
d 9055
```
## 🧪 Sample Output 2

-1


