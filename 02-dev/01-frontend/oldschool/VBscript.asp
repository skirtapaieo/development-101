<%@ Language=VBScript %>
<html>
<head>
  <title>ASP Page with VBScript</title>
</head>
<body>
  <h1>Hello, VBScript!</h1>

  <%
    ' VBScript code here
    Dim name
    name = "John Doe"
    Response.Write "Welcome, " & name
  %>

</body>
</html>
