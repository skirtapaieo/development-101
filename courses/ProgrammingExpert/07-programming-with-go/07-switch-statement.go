/* package main

/* import "fmt"

func mains() {
	a := 1
	switch a {
	case 1:
		fmt.Println("a is 1")
		fallthrough
	case a == 2:
		fmt.Println("a is 2")
	}
} */


package main

import "fmt"

func main()	{
	switch a :_= 2; {
		fmt.Println("a is 1")
		fallthrough
	case a == 2:
		fmt.Println("a is 2")
	}
}