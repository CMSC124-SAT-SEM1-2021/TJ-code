
Create a grammar for a small language using BNF that accepts a program code that
- Starts with the special word begin
- Followed by one or more assignment statements, wherein each statement ends with a semicolon 
- After the last statement, the code should end with the special word end

Grammar:
```
<programcode> 	-> 	begin <stmts> end
      <stmts> 	-> 	<assign> ; | <assign> ; <stmts>
     <assign> 	-> 	<var> = <expr> | <var> = ( <expr> )
       <expr> 	-> 	<var> + <var> | <var> - <var> | <var> * <var> | <var> | <var> + <expr> | <var> - <expr> | <var> * <expr>
        <var> 	-> 	A | B | C
```



Derive the statement below and create a parse tree for it:
```
begin B = C * A + B * B ; C = ( B * C + A ) ; end
```

Derivation:
```
<programcode>	->	begin <stmts> end
				-> 	begin <assign> ; <stmts> end
				->	begin <var> = <expr> ; <stmts> end
				->	begin B = <expr> ; <stmts> end
				->	begin B = <var> * <expr> ; <stmts> end
				->	begin B = C * <expr> ; <stmts> end
				->	begin B = C * <var> + <expr> ; <stmts> end
				->	begin B = C * A + <expr> ; <stmts> end
				->	begin B = C * A + <var> * <expr> ; <stmts> end
				->	begin B = C * A + B * <expr> ; <stmts> end
				->	begin B = C * A + B * <var> ; <stmts> end
				->	begin B = C * A + B * B ; <stmts> end
				->	begin B = C * A + B * B ; <assign> ; end
				->	begin B = C * A + B * B ; <var> = ( <expr> ) ; end
				->	begin B = C * A + B * B ; C = ( <var> * <expr> ) ; end
				->	begin B = C * A + B * B ; C = ( B * <expr> ) ; end
				->	begin B = C * A + B * B ; C = ( B * <var> + <expr> ) ; end
				->	begin B = C * A + B * B ; C = ( B * C + <expr> ) ; end
				->	begin B = C * A + B * B ; C = ( B * C + <var> ) ; end
				->	begin B = C * A + B * B ; C = ( B * C + A ) ; end
```