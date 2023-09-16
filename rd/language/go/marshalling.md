
### Marshalling/Unmarshalling

#### What is it?

Marshalling and unmarshalling are the processes of converting data between different forms or data structures.

- **Marshalling**: It is the process of converting a data structure or object into a format that can be easily stored or sent and later reconstructed. In programming, this often means transforming complex data types like objects or structs into byte streams, JSON, XML, etc.

- **Unmarshalling**: This is the reverse process of marshalling. It involves taking a serialized format and converting it back into an object or data structure that a program can manipulate.

#### Why is it Important?

1. **Data Transmission**: Makes it possible to send complex data types over a network or save them in a database.
2. **Data Storage**: Allows for the easy storage of complex data structures in a serialized form.
3. **Interoperability**: Enables different systems or components to understand and exchange data.
4. **Data Integrity**: Provides a consistent way to manage complex data types, helping to maintain data integrity.

#### Example in Go

Here's an example in Go that shows how to marshal a struct to JSON and unmarshal JSON back to a struct.

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	// Marshalling
	p1 := Person{Name: "Alice", Age: 30}
	p1JSON, err := json.Marshal(p1)
	if err != nil {
		fmt.Println("Error marshalling:", err)
		return
	}
	fmt.Println("Marshalled data:", string(p1JSON))

	// Unmarshalling
	jsonStr := `{"name":"Bob","age":40}`
	var p2 Person
	err = json.Unmarshal([]byte(jsonStr), &p2)
	if err != nil {
		fmt.Println("Error unmarshalling:", err)
		return
	}
	fmt.Println("Unmarshalled data:", p2)
}
```

In this example, the `Person` struct is marshalled into a JSON string and then that JSON string is unmarshalled back into a `Person` struct. The `encoding/json` package in Go provides functionalities for both marshalling and unmarshalling.