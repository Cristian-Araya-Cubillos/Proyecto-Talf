# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .recipesParser import recipesParser
else:
    from recipesParser import recipesParser

# This class defines a complete listener for a parse tree produced by recipesParser.
class recipesListener(ParseTreeListener):

    # Enter a parse tree produced by recipesParser#query.
    def enterQuery(self, ctx:recipesParser.QueryContext):
        pass

    # Exit a parse tree produced by recipesParser#query.
    def exitQuery(self, ctx:recipesParser.QueryContext):
        pass


    # Enter a parse tree produced by recipesParser#condition.
    def enterCondition(self, ctx:recipesParser.ConditionContext):
        pass

    # Exit a parse tree produced by recipesParser#condition.
    def exitCondition(self, ctx:recipesParser.ConditionContext):
        pass


    # Enter a parse tree produced by recipesParser#ingredient.
    def enterIngredient(self, ctx:recipesParser.IngredientContext):
        pass

    # Exit a parse tree produced by recipesParser#ingredient.
    def exitIngredient(self, ctx:recipesParser.IngredientContext):
        pass


    # Enter a parse tree produced by recipesParser#quantity.
    def enterQuantity(self, ctx:recipesParser.QuantityContext):
        pass

    # Exit a parse tree produced by recipesParser#quantity.
    def exitQuantity(self, ctx:recipesParser.QuantityContext):
        pass


    # Enter a parse tree produced by recipesParser#descriptor.
    def enterDescriptor(self, ctx:recipesParser.DescriptorContext):
        pass

    # Exit a parse tree produced by recipesParser#descriptor.
    def exitDescriptor(self, ctx:recipesParser.DescriptorContext):
        pass



del recipesParser