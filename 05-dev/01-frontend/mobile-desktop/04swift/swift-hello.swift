import Foundation

let url = URL(string: "http://localhost:3000")!
let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
    if let error = error {
        print("Error: \(error)")
    } else if let data = data {
        let str = String(data: data, encoding: .utf8)
        print("Received data:\n\(str!)") // "Hello, World!"
    }
}

task.resume()
