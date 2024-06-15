# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,15,2,0,7,0,2,1,7,1,1,0,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,1,1,1,1,0,0,2,0,2,0,0,13,0,4,1,0,0,0,2,12,1,0,0,0,4,9,3,2,1,
        0,5,6,5,1,0,0,6,8,3,2,1,0,7,5,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,
        10,1,0,0,0,10,1,1,0,0,0,11,9,1,0,0,0,12,13,5,2,0,0,13,3,1,0,0,0,
        1,9
    ]

class recipesParser ( Parser ):

    grammarFileName = "recipes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WORD", "WS" ]

    RULE_query = 0
    RULE_ingredient = 1

    ruleNames =  [ "query", "ingredient" ]

    EOF = Token.EOF
    T__0=1
    WORD=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ingredient(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(recipesParser.IngredientContext)
            else:
                return self.getTypedRuleContext(recipesParser.IngredientContext,i)


        def getRuleIndex(self):
            return recipesParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = recipesParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.ingredient()
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 5
                self.match(recipesParser.T__0)
                self.state = 6
                self.ingredient()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IngredientContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(recipesParser.WORD, 0)

        def getRuleIndex(self):
            return recipesParser.RULE_ingredient

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIngredient" ):
                listener.enterIngredient(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIngredient" ):
                listener.exitIngredient(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIngredient" ):
                return visitor.visitIngredient(self)
            else:
                return visitor.visitChildren(self)




    def ingredient(self):

        localctx = recipesParser.IngredientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ingredient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(recipesParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





