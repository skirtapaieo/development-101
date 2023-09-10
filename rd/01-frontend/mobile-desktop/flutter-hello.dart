import 'package:http/http.dart' as http;
import 'dart:convert';

void fetchMessage() async {
  final response = await http.get('http://localhost:3000');

  if (response.statusCode == 200) {
    var message = jsonDecode(response.body);
    print(message); // "Hello, World!"
  } else {
    throw Exception('Failed to load message');
  }
}
