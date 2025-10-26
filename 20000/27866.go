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

	var n int
	var str string

	fmt.Fscan(reader, &str)
	fmt.Fscan(reader, &n)

	fmt.Fprint(writer, str[n-1:n])
}