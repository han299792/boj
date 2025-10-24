// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// )

// func main() {
// 	reader := bufio.NewReader(os.Stdin)
// 	writer := bufio.NewWriter(os.Stdout)
// 	defer writer.Flush()

// 	var n, num int
// 	var min, max int

// 	fmt.Fscan(reader, &n)

// 	fmt.Fscan(reader, &num)
// 	min = num
// 	max = num

// 	for i := 1; i < n; i++ {
// 		fmt.Fscan(reader, &num)

// 		if num > max {
// 			max = num
// 		}
// 		if num < min {
// 			min = num
// 		}
// 	}

// 	fmt.Fprint(writer, min, " ", max)
// }