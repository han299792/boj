package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var num, n  int
	max := 0
	idx := 0

	fmt.Fscan(reader, &n)
	
	for i := 0; i < 9; i++ {
		fmt.Fscan(reader, &num)
		if num > max {
			max = num
			idx = i 
		}
	}

	fmt.Fprint(writer, max, "\n", idx+1)
}