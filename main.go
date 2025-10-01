package main

import (
	"fmt"
)

func main() {
	var grid [9][9]int

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Scan(&grid[i][j])
		}
	}

	maxVal := -1
	row, col := 0, 0

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if grid[i][j] > maxVal {
				maxVal = grid[i][j]
				row = i + 1
				col = j + 1
			}
		}
	}

	fmt.Printf("%d\n", maxVal)
	fmt.Printf("%d %d\n", row, col)
}
