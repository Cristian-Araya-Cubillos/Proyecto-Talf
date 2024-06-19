grammar recipes;

query          : condition (LOGICAL_OP condition)* ;
condition      : ingredient | '(' query ')' ;
ingredient     : quantity? descriptor* WORD (descriptor+ WORD)* ;
quantity       : NUMBER ;
descriptor     : WORD ;
WORD           : [a-zA-Z]+ ;
NUMBER         : [0-9]+ ;
LOGICAL_OP     : ',' | '|' ;
WS             : [ \t\n\r]+ -> skip ;


