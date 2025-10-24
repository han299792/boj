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

	var a, b int

	for {
		fmt.Fscan(reader, &a)
		fmt.Fscan(reader, &b)
		if a == 0 && b == 0 {
			break
		}
		fmt.Fprintln(writer, a+b)
		
	}

}