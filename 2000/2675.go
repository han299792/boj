package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, num int
	var str string
	fmt.Fscan(reader, &n)
	
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &num)
		fmt.Fscan(reader, &str)

		var para string

		for j := 0; j < len(str); j++ {
			para += strings.Repeat(string(str[j]), num)
		}
		fmt.Fprintln(writer, para) 
	}
}