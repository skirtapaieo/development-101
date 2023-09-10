# factorial

package main

import "fmt"

// Factorial function calculates the factorial of n
func Factorial(n int) int {
	result := 1
	for i := 1; i <= n; i++ {
		result *= i
	}
	return result
}

func main() {
	n := 7
	fmt.Printf("Factorial of %d is %d\n", n, Factorial(n)) // Output: Factorial of 7 is 5040
}
