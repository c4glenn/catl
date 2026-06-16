# Generated from catl.g4 by ANTLR 4.13.0
from antlr4 import *

'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab (ERL), Autonomous and Intelligent Robotics (AIR) Lab,
 Lehigh University
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''


# This class defines a complete generic visitor for a parse tree produced by catlParser.

class catlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by catlParser#catlPredicate.
    def visitCatlPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#catlLimit.
    def visitCatlLimit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#formula.
    def visitFormula(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#parprop.
    def visitParprop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#predicate.
    def visitPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#limit.
    def visitLimit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#capabilities.
    def visitCapabilities(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#capabilityRequest.
    def visitCapabilityRequest(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#resources.
    def visitResources(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by catlParser#resourceRequest.
    def visitResourceRequest(self, ctx):
        return self.visitChildren(ctx)


