# Generated from C:/Users/Yukihana/IdeaProjects/Trabajo/src/recipes.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .recipesParser import recipesParser
else:
    from recipesParser import recipesParser

# This class defines a complete generic visitor for a parse tree produced by recipesParser.

class recipesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by recipesParser#query.
    def visitQuery(self, ctx:recipesParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#condition.
    def visitCondition(self, ctx:recipesParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#ingredient.
    def visitIngredient(self, ctx:recipesParser.IngredientContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#quantity.
    def visitQuantity(self, ctx:recipesParser.QuantityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by recipesParser#descriptor.
    def visitDescriptor(self, ctx:recipesParser.DescriptorContext):
        return self.visitChildren(ctx)



del recipesParser