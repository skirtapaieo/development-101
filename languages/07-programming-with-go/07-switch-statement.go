package main

import "fmt"

func main() {
	a := 1
	switch a {
	case 1:
		fmt.Println("a is 1")
		fallthrough
	case a < 2:
		fmt.Println("a is 2")
	}
}
