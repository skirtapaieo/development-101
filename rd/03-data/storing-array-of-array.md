
# Storing a data structure

## Option 0 - The initial data structure (in prototype)

```JavaScript
  const hierarchies = [
        ["Portfolio", "Program", "Project"],
        ["Cross-tribe", "Tribe", "Squad"],
        ["Department", "Line Management", "Line Reports"],
        ["Task force", "Mission", "Action groups"],
        ["Crew", "Standard process", "sub-crews"],
        ["Club", "Interest", "Activity groups"],
        ["Chapter", "Chapter lead", "Sub-chapters"],
        ["Guild", "Interest areas", "Guild group"],
        ["External stake", "Advisory groups", "N/A"],
        ["Board", "Board committees", "N/A"],
        ["Executive team", "Business units", "N/A"],
      ];
```


## Option 1 - JSON Objects

```JavaScript
const hierarchies = {
  "Level 1": ["Portfolio", "Cross-tribe", "Department", "Task force", "Crew", "Club", "Chapter", "Guild", "External stake", "Board", "Executive team"],
  "Level 2": ["Program", "Tribe", "Line Management", "Mission", "Standard process", "Interest", "Chapter lead", "Interest areas", "Advisory groups", "Board committees", "Business units"],
  "Level 3": ["Project", "Squad", "Line Reports", "Action groups", "sub-crews", "Activity groups", "Sub-chapters", "Guild group", "N/A", "N/A", "N/A"]
};
```

## Option 2 - Nested Objects

For easier traversal:

```JavaScript
const hierarchies = {
  "Board": {
    "Board committees": "N/A"
  },
  "Executive team": {
    "Business units": "N/A"
  },
  "Portfolio": {
    "Program": "Project"
  },
  //... (and so on)
};

```

## Option 3 - Database

## Accessing the data

Array - directly index to the array
JSON object - use keys to get to values
Nested objects - Traverse through nested keys
Database - SQL queries, or NoSQL queries (like MongoDB)


# Real world examples

Each storage method has its trade-offs:
- serialization is simplest but may be cumbersome for large or complex hierarchies.
- JSON objects offer more context but require deserialization.
- Databases provide the most flexibility but add complexity and dependency to your setup.

## Option 0: Array of Arrays (Serialization)

**Storage**: You can serialize the array of arrays into a string using `JSON.stringify()` and store it as a text field in a relational database or as a file.

```javascript
const serialized = JSON.stringify(hierarchies);
// Store `serialized` into a database or file
```

**Retrieval**: Deserialize the string back into an array of arrays using `JSON.parse()`.

```javascript
const retrieved = JSON.parse(serialized);
```

## Option 1: JSON Object

**Storage**: You can serialize the JSON object using `JSON.stringify()` and store it in a text field in a database or as a JSON file.

```javascript
const jsonString = JSON.stringify(hierarchies);
// Store `jsonString` into a database or file
```

**Retrieval**: Deserialize the string back into a JSON object using `JSON.parse()`.

```javascript
const retrievedJson = JSON.parse(jsonString);
```

## Option 2: Nested Objects

**Storage**: Similar to the JSON object, you can serialize the nested object and store it in a database or a JSON file.

```javascript
const nestedString = JSON.stringify(nestedHierarchies);
// Store `nestedString` into a database or file
```

**Retrieval**: Deserialize back into a nested object using `JSON.parse()`.

```javascript
const retrievedNested = JSON.parse(nestedString);
```

## Option 3: Database

### Relational Database (e.g., SQL)

**Storage**: Store each level and hierarchy as rows in a table. You can have columns like `HierarchyType`, `Level1`, `Level2`, etc.

**Retrieval**: Query the database to reconstruct your hierarchy or to get specific rows based on conditions.

### NoSQL Database (e.g., MongoDB)

**Storage**: You can store the entire nested object or JSON object as a single document.

**Retrieval**: Query the database to retrieve the document, which would contain your entire hierarchy. You can also perform more complex queries to get specific parts.

### Code Example for MongoDB
```javascript
// Assuming `hierarchies` is your JSON object
const MongoClient = require('mongodb').MongoClient;

async function run() {
  const client = new MongoClient('mongodb://localhost:27017');
  await client.connect();

  const db = client.db('testDB');
  const collection = db.collection('hierarchies');

  // Storage
  await collection.insertOne({ hierarchies });

  // Retrieval
  const doc = await collection.findOne({});
  const retrievedHierarchies = doc.hierarchies;

  console.log(retrievedHierarchies);

  client.close();
}

run().catch(console.dir);
```

# Local storage

You can store data locally in a browser using various web storage APIs. Below are some common options.

Each method has its trade-offs in terms of storage limits, data types, and ease of use. Choose based on the specific needs of your project.

Certainly, let's go over code examples for LocalStorage and IndexedDB, as these are the most commonly used for local storage in a browser. I'll provide simple snippets for storing and retrieving data.

### 1. LocalStorage

#### Storage

```javascript
const hierarchies = [
  ["Portfolio", "Program", "Project"],
  // ...
];

// Serialize and save to local storage
const serializedHierarchies = JSON.stringify(hierarchies);
localStorage.setItem("myHierarchies", serializedHierarchies);
```

#### Retrieval

```javascript
// Retrieve from local storage and deserialize
const retrievedHierarchies = JSON.parse(localStorage.getItem("myHierarchies"));
console.log(retrievedHierarchies);  // Should output the original hierarchies array
```

### 2. IndexedDB

IndexedDB is a bit more complicated but more powerful. Here is a simplified example:

#### Storage

```javascript
let openRequest = indexedDB.open("myDatabase", 1);

openRequest.onupgradeneeded = function(event) {
  let db = event.target.result;
  let store = db.createObjectStore("myStore", {keyPath: "id"});
};

openRequest.onsuccess = function(event) {
  let db = event.target.result;
  let transaction = db.transaction("myStore", "readwrite");
  let store = transaction.objectStore("myStore");

  // Save data
  store.add({id: 1, hierarchies: hierarchies});
};
```

#### Retrieval

```javascript
let openRequest = indexedDB.open("myDatabase", 1);

openRequest.onsuccess = function(event) {
  let db = event.target.result;
  let transaction = db.transaction("myStore", "readonly");
  let store = transaction.objectStore("myStore");

  // Retrieve data
  let getRequest = store.get(1);
  getRequest.onsuccess = function(event) {
    console.log(event.target.result.hierarchies);  // Should output the original hierarchies array
  };
};
```

Feel free to explore and integrate these into your project as needed!