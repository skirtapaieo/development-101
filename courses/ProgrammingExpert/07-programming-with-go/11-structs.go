package main

import "fmt"

type Person struct {
	Name string
	Age  uint
}

func main() {
	p1 := Person{"John", 20}
	fmt.Println(p1)
}
