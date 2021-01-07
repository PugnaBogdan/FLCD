%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token IS
%token PLUS
%token MINUS
%token READ
%token TIMES
%token SMALLER
%token SMALLER_OR_EQUAL
%token BIGGER
%token BIGGER_OR_EQUAL
%token DEVIDE
%token EQUALS
%token START
%token END
%token LOOP
%token NUMBER
%token DIGIT
%token IF
%token ELSE
%token SHOW
%token LETTER
%token FOR
%token ARRAYN 
%token STRING
%token SIZE

%token IDEN
%token CONST

%token OPEN_SQUARE
%token CLOSED_SQUARE 
%token OPEN_BRACKET
%token CLOSED_BRACKET
%token OPEN_FANCY
%token CLOSED_FANCY
%token DIEZ

%token COMMA 
%token SEMI_COLON
%token SPACE 

%start program 

%%
program : START cmpdstmt END
	 ;
cmpdstmt : stmtlist
	 ;
stmtlist :  stmt
	 ;
stmt :  simplstmt
     ;
simplstmt :  assignstmt | iostmt
	 ;
declaration :  type IDEN SEMI_COLON | type IDEN IS CONST SEMI_COLON
	;
assignstmt : IDEN IS expression 
	;
declstmt : declaration  | declaration COMMA declstmt  
	;
term : term TIMES | DEVIDE factor| factor 
	;
whilestmt :  LOOP OPEN_BRACKET condition CLOSED_BRACKET DIEZ stmt DIEZ
	  ;
type :  NUMBER | STRING | LETTER | ARRAYN
	   ;
expression : expression OPEN_BRACKET PLUS | MINUS CLOSED_BRACKET term | term SEMI_COLON
	   ;
forstmt :  FOR OPEN_BRACKET assignstmt | IDEN SEMI_COLON condition SEMI_COLON assignstmt CLOSED_BRACKET DIEZ stmtlist DIEZ 
       ;	
ifstmt :  IF OPEN_BRACKET condition CLOSED_BRACKET DIEZ stmt DIEZ OPEN_SQUARE ELSE DIEZ stmt DIEZ CLOSED_SQUARE
       ;
factor : OPEN_BRACKET expression CLOSED_BRACKET | CONST| IDEN
	;	
iostmt :   READ | SHOW | IDEN| CONST SEMI_COLON
      ; 
arraydecl : ARRAYN OPEN_SQUARE NUMBER CLOSED_SQUARE IS type
	;
relation : SMALLER | SMALLER_OR_EQUAL | EQUALS | BIGGER_OR_EQUAL | BIGGER
	;
condition : OPEN_BRACKET expression relation expression CLOSED_BRACKET
	;
%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}