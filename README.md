# BFS Alogorithms in Games

## Flood fill

```python
def floodFill_image(x, y):
    def neighbors(x, y, active_color):
        indices = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for x, y in indices if isValid(x, y) and field.get_at((x, y)) == (255, 255, 255)]


    def isValid(x, y):
        return x >= 0 and y >= 0 and x < 640 and y < 640
        
    start = scr.get_at((x, y))
    queue = [(x, y)]
    visited = set()
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        field.set_at((x, y), active_color)
        painting.append(((active_color), [x, y], active_size))
        for x, y in neighbors(x, y, active_color):
            if (x, y) not in visited:
                queue.append((x, y))
```

[Flood fill](https://leetcode.com/problems/flood-fill/description/) is used in drawing redactors - bucket tool fills outlines this way

`basic`

<span>
  <img src="images/Screenshot 2025-07-03 at 19.47.28.png" alt="game photo" width="450"/>
  <img src="images/Screenshot 2025-07-03 at 19.47.52.png" alt="game photo" width="450"/> 
</span>

`advanced`

<span>
  <img src="images/Screenshot 2025-07-03 at 19.20.10.png" alt="game photo" width="450"/>
  <img src="images/Screenshot 2025-07-03 at 19.20.20.png" alt="game photo" width="450"/> 
</span>

Also to find the distance to each square from some flag is achieved with BFS. For [example](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) more complicated problem

*cells' of same color distances to the flag are the same*

<span>
  <img src="images/Screenshot 2025-07-03 at 19.21.08.png" alt="game photo" width="450"/>
  <img src="images/Screenshot 2025-07-03 at 19.21.13.png" alt="game photo" width="450"/> 
</span>

## Possible moves

```python
def knight_bfs(image, sr, sc, color=0):
    def neighbors(image, sr, sc, start):
        indices = [
            (sr - 1, sc - 2),
            (sr - 1, sc + 2),
            (sr + 1, sc - 2),
            (sr + 1, sc + 2),
            (sr - 2, sc - 1),
            (sr - 2, sc + 1),
            (sr + 2, sc - 1),
            (sr + 2, sc + 1)
        ]
        return [(sr, sc) for sr, sc in indices if isValid(image, sr, sc) and image[sr][sc] == start]


    def isValid(image, sr, sc):
        return sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0])
        

    start = image[sr][sc]
    queue = deque([(sr, sc, color)])
    visited = set()
    while queue:
        sr, sc, col = queue.popleft()
        visited.add((sr, sc))
        image[sr][sc] = col
        for sr, sc in neighbors(image, sr, sc, start):
            if (sr, sc) not in visited:
                queue.append((sr, sc, col + 1))
    return image
```

This code shows how many moves it takes [knight](https://www.geeksforgeeks.org/minimum-steps-reach-target-knight-set-2/) to get to each square of chessboard. 

<span>
  <img src="images/Screenshot 2025-07-03 at 19.21.31.png" alt="game photo" width="450"/>
  <img src="images/Screenshot 2025-07-03 at 19.21.35.png" alt="game photo" width="450"/> 
</span>


# Installation

To run these games you need to install pygame library. Run in terminal

```bash
pip install pygame
```

Than either copy each file or run

```bash
git clone https://github.com/CrazyMikha2010/BFS_games.git
```
