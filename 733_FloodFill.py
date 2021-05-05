'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

'''

class Solution:
    def floodFill(self, image, sr, sc, newColor):

        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]
        neighbours = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(i, j):
            # nonlocal image # if uncommented, it makes code slow
            # nonlocal visited
            image[i][j] = newColor
            for ni, nj in neighbours:
                x = i + ni
                y = j + nj

                if 0 <= x < rows and 0 <= y < cols and image[x][y] == original_color and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)

        dfs(sr, sc)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

s = Solution()
print(s.floodFill(image, sr, sc, newColor))