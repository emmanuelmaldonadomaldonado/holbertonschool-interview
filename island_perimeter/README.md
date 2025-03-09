The `island_perimeter` function calculates the perimeter of an island represented by a grid. The grid is a list of lists of integers where 0 represents water and 1 represents land. The function returns the total perimeter of the island.

## Usage

To use the `island_perimeter` function, you need to pass a grid as an argument. The grid should be a rectangular list of lists containing only 0s and 1s.

### Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 16
```
