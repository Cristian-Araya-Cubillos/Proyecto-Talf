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
        4,1,6,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,0,
        14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,3,2,27,
        8,2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,2,1,2,4,2,37,8,2,11,2,12,2,
        38,1,2,1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,4,1,4,1,4,0,0,5,
        0,2,4,6,8,0,0,52,0,10,1,0,0,0,2,23,1,0,0,0,4,26,1,0,0,0,6,47,1,0,
        0,0,8,49,1,0,0,0,10,15,3,2,1,0,11,12,5,5,0,0,12,14,3,2,1,0,13,11,
        1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,
        15,1,0,0,0,18,24,3,4,2,0,19,20,5,1,0,0,20,21,3,0,0,0,21,22,5,2,0,
        0,22,24,1,0,0,0,23,18,1,0,0,0,23,19,1,0,0,0,24,3,1,0,0,0,25,27,3,
        6,3,0,26,25,1,0,0,0,26,27,1,0,0,0,27,31,1,0,0,0,28,30,3,8,4,0,29,
        28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,
        0,33,31,1,0,0,0,34,44,5,3,0,0,35,37,3,8,4,0,36,35,1,0,0,0,37,38,
        1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,5,3,0,0,
        41,43,1,0,0,0,42,36,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,
        0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,48,5,4,0,0,48,7,1,0,0,0,49,50,
        5,3,0,0,50,9,1,0,0,0,6,15,23,26,31,38,44
    ]

class recipesParser ( Parser ):

    grammarFileName = "recipes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WORD", "NUMBER", 
                      "LOGICAL_OP", "WS" ]

    RULE_query = 0
    RULE_condition = 1
    RULE_ingredient = 2
    RULE_quantity = 3
    RULE_descriptor = 4

    ruleNames =  [ "query", "condition", "ingredient", "quantity", "descriptor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WORD=3
    NUMBER=4
    LOGICAL_OP=5
    WS=6

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

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(recipesParser.ConditionContext)
            else:
                return self.getTypedRuleContext(recipesParser.ConditionContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(recipesParser.LOGICAL_OP)
            else:
                return self.getToken(recipesParser.LOGICAL_OP, i)

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
            self.state = 10
            self.condition()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 11
                self.match(recipesParser.LOGICAL_OP)
                self.state = 12
                self.condition()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ingredient(self):
            return self.getTypedRuleContext(recipesParser.IngredientContext,0)


        def query(self):
            return self.getTypedRuleContext(recipesParser.QueryContext,0)


        def getRuleIndex(self):
            return recipesParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = recipesParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_condition)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.ingredient()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(recipesParser.T__0)
                self.state = 20
                self.query()
                self.state = 21
                self.match(recipesParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

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

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(recipesParser.WORD)
            else:
                return self.getToken(recipesParser.WORD, i)

        def quantity(self):
            return self.getTypedRuleContext(recipesParser.QuantityContext,0)


        def descriptor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(recipesParser.DescriptorContext)
            else:
                return self.getTypedRuleContext(recipesParser.DescriptorContext,i)


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
        self.enterRule(localctx, 4, self.RULE_ingredient)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 25
                self.quantity()


            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.descriptor() 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 34
            self.match(recipesParser.WORD)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 36 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 35
                        self.descriptor()

                    else:
                        raise NoViableAltException(self)
                    self.state = 38 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 40
                self.match(recipesParser.WORD)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(recipesParser.NUMBER, 0)

        def getRuleIndex(self):
            return recipesParser.RULE_quantity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantity" ):
                listener.enterQuantity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantity" ):
                listener.exitQuantity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity" ):
                return visitor.visitQuantity(self)
            else:
                return visitor.visitChildren(self)




    def quantity(self):

        localctx = recipesParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(recipesParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(recipesParser.WORD, 0)

        def getRuleIndex(self):
            return recipesParser.RULE_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescriptor" ):
                listener.enterDescriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescriptor" ):
                listener.exitDescriptor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescriptor" ):
                return visitor.visitDescriptor(self)
            else:
                return visitor.visitChildren(self)




    def descriptor(self):

        localctx = recipesParser.DescriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(recipesParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





