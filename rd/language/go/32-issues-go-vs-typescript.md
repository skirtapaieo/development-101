
# Reddit comments


1] nil pointers could blow up the code anywhere and the compiler does nothing to prevent accessing something which can be nil.

2] Error handling (or lackthereof) at every line is insanely painful to see and if you forget to check any error then the code could blow up and the compiler WILL NOT stop you at all

3] No union/sum types is also a BIG problem.

4] poor OOPish implementation using receiver functions instead of just having proper OOP if that's what they wanted to enable in the first place.

5] implicit interface implementation means you have to read the entire declaration of the file just to know which interface is implemented instead of just allowing "x implements y,z..." like EVERY other language.

6] Zero default values do not play well with JSON serialization/deserialization and are a source of MANY MANY bugs. Workaround is to convert a field to a pointer and then do the nil check, but this means you have to convert all the struct keys to a pointer as you can receive an entire empty struct so how will you identify what was set and what was not set without all struct keys being set to pointer and doing the nil checks, it just never ends.

7] Cannot access keys of struct dynamically using a variable which is so easy in typescript (also very securely as well due to powerful type system) and in GO one has to convert the struct to a map or use reflect boilerplate code just to access a key of a struct using a variable.

8] Cannot create a new struct by picking/omitting few keys from other struct. The code is never DRY in GO

9] PAINFUL JSON handling - especially deeply nested (or dynamic) JSON as the JSON mapping logic is inside strings (struct string tags) where there is no autocomplete and no compile error

10] Code littered with pointer/nonpointer/slice/capacity/interface{} madness everywhere.

11] No function overloading

12] No ternary operator

13] No enums

14] no optional/multi value JSON keys possible to express and you have to resort to interface{} and do the typecasting later on which is difficult to read if the JSON is big and the code is big

15] Beyond just JSON, if you have to do JSON validation for incoming requests then you add more and more validation logic using third party library to the json struct tags which is a string where there is no type completion and custom functions are also a a pain to write and customise error messages.

16] On top of point 15 if you have to also support GraphQL/Websocket alongside REST api's and database schemas then its an absolute hell and the code becomes an absolute mess with so so much logic in the json string tags on top of data validation.

17] No meta framework like Nest.js, PHP laravel, C# .NET core, Java spring or Python DJango etc. so you will have to reinvent the wheel especially in any enterprise server by implementing the solutions on your own. GO community calls having NO options and NO features in the language an INNOVATION and the toxic GO community downvotes anyone to oblivion who dares expect improvements or say "but its better in Typescript/kotlin etc".

18] Capitalise to export instead of using "export" keyword which is searchable and easily readable as capitalized variables have different meaning in universally all languages except GO for no apparent reason.

19] Poor generics implementation, that too after 10 years of constant crying from the community.

20] No default function arguments, no optional function arguments (only variadic's are possible)

21] No error stack traces (as error's are not thrown but returned) and you will have to accumulate and build an entire stack on your own and for that you have to use a third party library. You have to use. THIRD PARTY LIBRARY to create an error stack trace is absolute bonkers.

22] No try/catch/finally and throwing NAMED errors like MOST mainstream languages.

23] strconv is the stupidest thing ever thought.

24] You can shadow global functions and will get surprising results directly in the runtime without any errors as the globals are overridden (ex. len() function can be overridden if you create a len variable which is a number and you will not get any runtime exception). For all the hate which Javascript gets, even JS throws an exception if you try to use a reserved keyword as a variable name.

25] Magic init method

26] Slice/capacity gotcha with pass by value/reference

27] Easy to shoot yourself on foot with Go channel/routine by getting a deadlock or out of hand go routines. The compiler does not do much to prevent race conditions

28] On a lesser note no map/filter/reduce/forEach/find/findIndex etc. quality of life methods which enhances the productivity.

29] Async communication and interrupting the parallel operations is not easy i.e. no Promise.all/race/allSettled/any etc. kinda tooling provided and anytime you have to do parallel/concurrent operations and do error handling/break the operations then its not easy and language provides no quality of life tools like we have in Javascript world with Promise api's.

30] Creating a non trivial Higher order function that can satisfy the type system (again beyond trivial case) is not easy as the type system is too rigid. Hence currying/partial functions are very difficult to get it right in GO even though it is a functional language.

31] GO promotes imperative and mutable code patterns (by passing pointers) for a functional language which makes code predictability harder.

32] Mocking for tests is also clunky and not pretty.

This was a comprehensive list of criticisms of Go (Golang) and its comparison with TypeScript.

---

## 1] Nil Pointers

### Reddit question

1] nil pointers could blow up the code anywhere and the compiler does nothing to prevent accessing something which can be nil.

### How it could go wrong in Go
Accessing a field or method on a nil pointer will result in a runtime panic.

```go
var a *MyStruct
a.Method()  // Panic
```

### How it is normally managed in Go
Go encourages explicit nil checks before dereferencing pointers.

```go
if a != nil {
  a.Method()
}
```

### Managed in TypeScript
TypeScript has strict null checks that can catch potential errors during compile-time.

```typescript
if (a !== null && a !== undefined) {
  a.method();
}
```

---

## 2] Error Handling

### Reddit

2] Error handling (or lackthereof) at every line is insanely painful to see and if you forget to check any error then the code could blow up and the compiler WILL NOT stop you at all


### How it could go wrong in Go
Ignoring an error can lead to unexpected behavior.

```go
result, _ := someFunction()
```

### How it is normally managed in Go
Explicitly handle the error right after the function that might return it.

```go
result, err := someFunction()
if err != nil {
  // handle error
}
```

### Managed in TypeScript
TypeScript uses the try-catch syntax for error handling.

```typescript
try {
  const result = someFunction();
} catch (error) {
  // handle error
}
```

---

## 3] No Union/Sum Types

### Reddit

3] No union/sum types is also a BIG problem.

### How it is normally managed in Go
You can simulate union types using interfaces.

```go
type MyUnion interface{}
```

### Managed in TypeScript
Union types are native to TypeScript.

```typescript
type MyUnion = Type1 | Type2;
```

---

## 4] OOP Implementation

### Reddit

4] poor OOPish implementation using receiver functions instead of just having proper OOP if that's what they wanted to enable in the first place.

### How it is normally managed in Go
Go uses structs and receiver functions to simulate OOP.

```go
type MyStruct struct{}
func (m MyStruct) Method() {}
```

### Managed in TypeScript
TypeScript uses classes and inheritance for OOP.

```typescript
class MyClass {
  method() {}
}
```

---

## 5] Implicit Interface Implementation

### Reddit

5] implicit interface implementation means you have to read the entire declaration of the file just to know which interface is implemented instead of just allowing "x implements y,z..." like EVERY other language.


### How it is normally managed in Go
Interfaces are satisfied implicitly in Go. The Go community often considers this a feature, not a drawback.

```go
type MyInterface interface {
  Method()
}

type MyStruct struct{}
func (m MyStruct) Method() {}

var _ MyInterface = MyStruct{}  // Compiler will check
```

### Managed in TypeScript
Interfaces must be explicitly implemented.

```typescript
interface MyInterface {
  method(): void;
}

class MyClass implements MyInterface {
  method() {}
}
```



---

## 6] Zero Default Values and JSON Serialization

### Reddit question

6] Zero default values do not play well with JSON serialization/deserialization and are a source of MANY MANY bugs. Workaround is to convert a field to a pointer and then do the nil check, but this means you have to convert all the struct keys to a pointer as you can receive an entire empty struct so how will you identify what was set and what was not set without all struct keys being set to pointer and doing the nil checks, it just never ends.


### How it is normally managed in Go
Use pointers for optional fields to distinguish between zero value and unset.

```go
type MyStruct struct {
  Field *int `json:"field,omitempty"`
}
```

### Managed in TypeScript
Optional fields and null checks can be handled natively.

```typescript
interface MyInterface {
  field?: number;
}
```

---

## 7] Accessing Struct Keys Dynamically

### Reddit question

7] Cannot access keys of struct dynamically using a variable which is so easy in typescript (also very securely as well due to powerful type system) and in GO one has to convert the struct to a map or use reflect boilerplate code just to access a key of a struct using a variable.


### How it is normally managed in Go
Use the `reflect` package for dynamic field access, although it's considered non-idiomatic.

```go
val := reflect.ValueOf(myStruct).FieldByName(fieldName).Interface()
```

### Managed in TypeScript
TypeScript allows dynamic property access using index signature.

```typescript
const value = myObject[fieldName];
```

---

## 8] Struct Manipulation

### Reddit question

8] Cannot create a new struct by picking/omitting few keys from other struct. The code is never DRY in GO


### How it is normally managed in Go
Go doesn't offer built-in manipulation; you have to create a new struct manually.

```go
newStruct := OldStruct{
  Field1: oldStruct.Field1,
}
```

### Managed in TypeScript
Destructuring and spread/rest syntax are available for object manipulation.

```typescript
const { fieldToRemove, ...newObject } = oldObject;
```

---

## 9] JSON Handling

### Reddit question

9] PAINFUL JSON handling - especially deeply nested (or dynamic) JSON as the JSON mapping logic is inside strings (struct string tags) where there is no autocomplete and no compile error


### How it is normally managed in Go
Go uses struct tags for mapping JSON keys.

```go
type MyStruct struct {
  Field string `json:"field"`
}
```

### Managed in TypeScript
Use native JavaScript methods like `JSON.parse` and `JSON.stringify`.

```typescript
const obj = JSON.parse(jsonString);
```

---

## 10] Code Complexity

### Reddit question

10] Code littered with pointer/nonpointer/slice/capacity/interface{} madness everywhere.


### How it is normally managed in Go
Go’s simplicity is a feature, but yes, it can lead to boilerplate.

```go
var a []int
a = append(a, 1)
```

### Managed in TypeScript
TypeScript has more high-level abstractions to handle complex patterns.

```typescript
const a: number[] = [];
a.push(1);
```

---

## 11] No Function Overloading

### How it is normally managed in Go
Use variadic parameters or different function names.

```go
func MyFunc(a int, optional ...int) {}
```

### Managed in TypeScript
TypeScript supports function overloading.

```typescript
function myFunction(x: number): number;
function myFunction(x: string): string;
```

Great! Let's proceed with the remaining points.

---

## 12] No Ternary Operator

### How it is normally managed in Go
Go doesn't support the ternary operator; you need to use if-else statements.

```go
var result int
if condition {
  result = 1
} else {
  result = 0
}
```

### Managed in TypeScript
TypeScript supports the ternary operator for compact conditionals.

```typescript
const result = condition ? 1 : 0;
```

---

## 13] No Enums

### How it is normally managed in Go
Go uses constants to simulate enumerations.

```go
const (
  Red = iota
  Green
  Blue
)
```

### Managed in TypeScript
TypeScript provides native support for enums.

```typescript
enum Color {
  Red,
  Green,
  Blue,
}
```

---

## 14] No Optional/Multi-Value JSON Keys

### How it is normally managed in Go
You can use `map[string]interface{}` for dynamic JSON or multiple value types.

```go
var obj map[string]interface{}
json.Unmarshal(jsonData, &obj)
```

### Managed in TypeScript
You can use union types or any.

```typescript
type MyType = string | number;
```

---

## 15] JSON Validation

### How it is normally managed in Go
Use third-party libraries like `go-validator`.

```go
type MyStruct struct {
  Field string `json:"field" validate:"required"`
}
```

### Managed in TypeScript
Use TypeScript type checking or libraries like `joi`.

```typescript
const schema = Joi.object({
  field: Joi.string().required(),
});
```

---

## 16] Supporting Multiple APIs

### How it is normally managed in Go
Build out separate logic; no integrated solution.

```go
// Separate structs and validation for REST, GraphQL, etc.
```

### Managed in TypeScript
Libraries like `Nest.js` offer more unified solutions.

```typescript
// Use decorators for REST, GraphQL in Nest.js
```

---

## 17] No Meta Framework

### How it is normally managed in Go
Standard library and third-party packages; no holistic framework.

### Managed in TypeScript
Nest.js, Angular, and other meta-frameworks exist for structured development.

---

## 18] Capitalization for Export

### How it is normally managed in Go
Use uppercase initials for exported variables and functions.

```go
var ExportedVar int
```

### Managed in TypeScript
Use `export` keyword to manage accessibility.

```typescript
export const myVariable = 42;
```

---

## 19] Generics Implementation

### How it is normally managed in Go
Recently added, but less powerful than in some other languages.

```go
func MyFunc[T any](arg T) T { return arg }
```

### Managed in TypeScript
TypeScript has a rich generics system.

```typescript
function myFunction<T>(arg: T): T { return arg; }
```

Certainly, let's continue.

---

## 20] No Default or Optional Function Arguments

### How it is normally managed in Go
Overloading isn't available. You may need to use variadic parameters and check within the function.

```go
func myFunc(args ...int) {
  var a = 0
  if len(args) > 0 {
    a = args[0]
  }
  // Rest of the code
}
```

### Managed in TypeScript
TypeScript supports optional and default parameters.

```typescript
function myFunc(a: number = 0) {
  // Rest of the code
}
```

---

## 21] No Error Stack Traces

### How it is normally managed in Go
You might use third-party libraries to construct custom error stack traces.

```go
// Using a package like pkg/errors
err := errors.Wrap(originalError, "my context")
```

### Managed in TypeScript
TypeScript has native error stack traces, accessible via the `Error.stack` property.

```typescript
try {
  // code
} catch (e) {
  console.log(e.stack);
}
```

---

## 22] No try/catch/finally and Named Errors

### How it is normally managed in Go
Go prefers explicit error handling using `if err != nil`.

```go
err := someFunction()
if err != nil {
  // Handle error
}
```

### Managed in TypeScript
TypeScript uses try/catch/finally for error handling.

```typescript
try {
  someFunction();
} catch (e) {
  // Handle error
} finally {
  // Cleanup
}
```

---

## 23] strconv is Stupid

### How it is normally managed in Go
`strconv` is the standard way to convert strings to basic data types.

```go
i, err := strconv.Atoi("42")
```

### Managed in TypeScript
Native conversion functions are available.

```typescript
const i = Number("42");
```

---

## 24] Shadowing Global Functions

### How it is normally managed in Go
Be cautious with naming to avoid shadowing.

```go
// Avoid shadowing global functions
```

### Managed in TypeScript
TypeScript also requires careful naming but will usually catch these kinds of errors.

```typescript
// Compiler usually warns about shadowing
```

---

## 25] Magic init Method

### How it is normally managed in Go
`init` functions are automatically executed when the package is initialized.

```go
func init() {
  // Initialization code
}
```

### Managed in TypeScript
Initialization can be handled in constructor methods or at the beginning of your code.

```typescript
// Initialization logic here
```

Certainly, let's finish up the list.

---

## 26] Slice/Capacity Gotcha with Pass by Value/Reference

### How it is normally managed in Go
Be aware of Go's slice behavior and use `copy` when necessary.

```go
newSlice := make([]int, len(oldSlice))
copy(newSlice, oldSlice)
```

### Managed in TypeScript
In TypeScript, you can use slice or spread to duplicate arrays.

```typescript
const newSlice = [...oldSlice];
```

---

## 27] Easy to Shoot Yourself on Foot with Go Channels/Routines

### How it is normally managed in Go
Use Go's race detector and practice safe concurrent programming.

```go
// Use sync package or channels to coordinate
```

### Managed in TypeScript
TypeScript doesn't have Go-like channels and goroutines, so this is less of an issue.

```typescript
// Use Promises, async/await
```

---

## 28] No map/filter/reduce, etc.

### How it is normally managed in Go
Write custom functions or loops for these operations.

```go
// Custom map, filter, reduce logic
```

### Managed in TypeScript
These functions are built into JavaScript arrays.

```typescript
arr.map(x => x * 2);
```

---

## 29] Async Communication and Interrupting

### How it is normally managed in Go
Use channels and select statement for complex async operations.

```go
// Use select and channels
```

### Managed in TypeScript
Promises and async/await make this straightforward.

```typescript
Promise.all([asyncFunc1(), asyncFunc2()]);
```

---

## 30] Higher-Order Function Complexity

### How it is normally managed in Go
Go's type system can make higher-order functions tricky.

```go
// Custom type definitions for function arguments
```

### Managed in TypeScript
TypeScript has extensive type inference, making this easier.

```typescript
// TypeScript handles types well in higher-order functions
```

---

## 31] Promotes Imperative and Mutable Code Patterns

### How it is normally managed in Go
Use pointers carefully and try to minimize side-effects.

```go
// Minimize side-effects
```

### Managed in TypeScript
Immutable patterns are easier to enforce with `const` and other ES6+ features.

```typescript
// Use const, map, filter, etc.
```

---

## 32] Mocking for Tests is Clunky

### How it is normally managed in Go
Go offers interfaces for mocking, but it can be verbose.

```go
// Use interfaces and custom mock implementations
```

### Managed in TypeScript
TypeScript can use libraries like Jest for easier mocking.

```typescript
jest.mock('./myModule');
```


