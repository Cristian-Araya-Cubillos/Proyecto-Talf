grammar recipes;

query       : ingredient (',' ingredient)* ;
ingredient  : WORD ;

WORD        : [a-zA-Z]+ ;
WS          : [ \t\n\r]+ -> skip ;
