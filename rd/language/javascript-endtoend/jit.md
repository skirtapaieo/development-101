# From bytecode

After the AST has been traversed we have bytecode for add(a,b)-function:

```
0x0     StackCheck
0x1     LdaSmi #0
0x3     Star r0
0x4     Ldar a1
0x5     Add r0
0x6     Return
```

:smile
