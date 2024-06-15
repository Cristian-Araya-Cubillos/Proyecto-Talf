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


    # Enter a parse tree produced by recipesParser#ingredient.
    def enterIngredient(self, ctx:recipesParser.IngredientContext):
        pass

    # Exit a parse tree produced by recipesParser#ingredient.
    def exitIngredient(self, ctx:recipesParser.IngredientContext):
        pass



del recipesParser