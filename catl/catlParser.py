# Generated from catl.g4 by ANTLR 4.13.0
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


'''
 Copyright (C) 2018-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab (ERL), Autonomous and Intelligent Robotics (AIR) Lab,
 Lehigh University
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''

def serializedATN():
    return [
        4,1,21,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,38,8,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,57,8,0,10,0,12,0,
        60,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,71,8,1,1,1,1,1,1,
        1,3,1,76,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,85,8,2,1,2,1,2,3,2,
        89,8,2,1,2,1,2,3,2,93,8,2,1,3,1,3,1,3,1,3,5,3,99,8,3,10,3,12,3,102,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,116,8,5,
        10,5,12,5,119,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,0,1,0,7,0,
        2,4,6,8,10,12,0,1,1,0,19,20,137,0,37,1,0,0,0,2,75,1,0,0,0,4,92,1,
        0,0,0,6,94,1,0,0,0,8,105,1,0,0,0,10,111,1,0,0,0,12,122,1,0,0,0,14,
        15,6,0,-1,0,15,16,5,1,0,0,16,17,3,0,0,0,17,18,5,2,0,0,18,38,1,0,
        0,0,19,38,3,2,1,0,20,38,3,4,2,0,21,22,5,13,0,0,22,38,3,0,0,7,23,
        24,5,14,0,0,24,25,5,3,0,0,25,26,7,0,0,0,26,27,5,4,0,0,27,28,7,0,
        0,0,28,29,5,5,0,0,29,38,3,0,0,6,30,31,5,15,0,0,31,32,5,3,0,0,32,
        33,7,0,0,0,33,34,5,4,0,0,34,35,7,0,0,0,35,36,5,5,0,0,36,38,3,0,0,
        5,37,14,1,0,0,0,37,19,1,0,0,0,37,20,1,0,0,0,37,21,1,0,0,0,37,23,
        1,0,0,0,37,30,1,0,0,0,38,58,1,0,0,0,39,40,10,4,0,0,40,41,5,12,0,
        0,41,57,3,0,0,5,42,43,10,3,0,0,43,44,5,10,0,0,44,57,3,0,0,4,45,46,
        10,2,0,0,46,47,5,11,0,0,47,57,3,0,0,3,48,49,10,1,0,0,49,50,5,16,
        0,0,50,51,5,3,0,0,51,52,7,0,0,0,52,53,5,4,0,0,53,54,7,0,0,0,54,55,
        5,5,0,0,55,57,3,0,0,2,56,39,1,0,0,0,56,42,1,0,0,0,56,45,1,0,0,0,
        56,48,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,1,1,0,
        0,0,60,58,1,0,0,0,61,62,5,6,0,0,62,63,5,1,0,0,63,64,7,0,0,0,64,65,
        5,4,0,0,65,66,5,18,0,0,66,67,5,4,0,0,67,70,3,6,3,0,68,69,5,4,0,0,
        69,71,3,10,5,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,
        2,0,0,73,76,1,0,0,0,74,76,5,17,0,0,75,61,1,0,0,0,75,74,1,0,0,0,76,
        3,1,0,0,0,77,78,5,7,0,0,78,79,5,1,0,0,79,80,5,18,0,0,80,84,5,4,0,
        0,81,85,3,6,3,0,82,83,5,8,0,0,83,85,5,9,0,0,84,81,1,0,0,0,84,82,
        1,0,0,0,85,88,1,0,0,0,86,87,5,4,0,0,87,89,3,10,5,0,88,86,1,0,0,0,
        88,89,1,0,0,0,89,90,1,0,0,0,90,93,5,2,0,0,91,93,5,17,0,0,92,77,1,
        0,0,0,92,91,1,0,0,0,93,5,1,0,0,0,94,95,5,8,0,0,95,100,3,8,4,0,96,
        97,5,4,0,0,97,99,3,8,4,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,
        0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,5,9,
        0,0,104,7,1,0,0,0,105,106,5,1,0,0,106,107,5,18,0,0,107,108,5,4,0,
        0,108,109,5,20,0,0,109,110,5,2,0,0,110,9,1,0,0,0,111,112,5,8,0,0,
        112,117,3,12,6,0,113,114,5,4,0,0,114,116,3,12,6,0,115,113,1,0,0,
        0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,
        0,119,117,1,0,0,0,120,121,5,9,0,0,121,11,1,0,0,0,122,123,5,1,0,0,
        123,124,5,18,0,0,124,125,5,4,0,0,125,126,7,0,0,0,126,127,5,2,0,0,
        127,13,1,0,0,0,10,37,56,58,70,75,84,88,92,100,117
    ]

class catlParser ( Parser ):

    grammarFileName = "catl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'['", u"','", u"']'", 
                     u"'T'", u"'L'", u"'{'", u"'}'", u"<INVALID>", u"<INVALID>", 
                     u"'=>'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'U'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"AND", u"OR", u"IMPLIES", 
                      u"NOT", u"EVENT", u"ALWAYS", u"UNTIL", u"BOOLEAN", 
                      u"VARIABLE", u"RATIONAL", u"INT", u"WS" ]

    RULE_catlProperty = 0
    RULE_predicate = 1
    RULE_limit = 2
    RULE_capabilities = 3
    RULE_capabilityRequest = 4
    RULE_resources = 5
    RULE_resourceRequest = 6

    ruleNames =  [ u"catlProperty", u"predicate", u"limit", u"capabilities", 
                   u"capabilityRequest", u"resources", u"resourceRequest" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    AND=10
    OR=11
    IMPLIES=12
    NOT=13
    EVENT=14
    ALWAYS=15
    UNTIL=16
    BOOLEAN=17
    VARIABLE=18
    RATIONAL=19
    INT=20
    WS=21

    def __init__(self, input, output=sys.stdout):
        super(catlParser, self).__init__(input, output=output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CatlPropertyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.CatlPropertyContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return catlParser.RULE_catlProperty

     
        def copyFrom(self, ctx):
            super(catlParser.CatlPropertyContext, self).copyFrom(ctx)


    class CatlPredicateContext(CatlPropertyContext):

        def __init__(self, parser, ctx): # actually a catlParser.CatlPropertyContext)
            super(catlParser.CatlPredicateContext, self).__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(catlParser.PredicateContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatlPredicate"):
                listener.enterCatlPredicate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatlPredicate"):
                listener.exitCatlPredicate(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCatlPredicate"):
                return visitor.visitCatlPredicate(self)
            else:
                return visitor.visitChildren(self)


    class CatlLimitContext(CatlPropertyContext):

        def __init__(self, parser, ctx): # actually a catlParser.CatlPropertyContext)
            super(catlParser.CatlLimitContext, self).__init__(parser)
            self.copyFrom(ctx)

        def limit(self):
            return self.getTypedRuleContext(catlParser.LimitContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterCatlLimit"):
                listener.enterCatlLimit(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCatlLimit"):
                listener.exitCatlLimit(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCatlLimit"):
                return visitor.visitCatlLimit(self)
            else:
                return visitor.visitChildren(self)


    class FormulaContext(CatlPropertyContext):

        def __init__(self, parser, ctx): # actually a catlParser.CatlPropertyContext)
            super(catlParser.FormulaContext, self).__init__(parser)
            self.left = None # CatlPropertyContext
            self.op = None # Token
            self.child = None # CatlPropertyContext
            self.low = None # Token
            self.high = None # Token
            self.right = None # CatlPropertyContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(catlParser.NOT, 0)
        def catlProperty(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(catlParser.CatlPropertyContext)
            else:
                return self.getTypedRuleContext(catlParser.CatlPropertyContext,i)

        def EVENT(self):
            return self.getToken(catlParser.EVENT, 0)
        def RATIONAL(self, i=None):
            if i is None:
                return self.getTokens(catlParser.RATIONAL)
            else:
                return self.getToken(catlParser.RATIONAL, i)
        def INT(self, i=None):
            if i is None:
                return self.getTokens(catlParser.INT)
            else:
                return self.getToken(catlParser.INT, i)
        def ALWAYS(self):
            return self.getToken(catlParser.ALWAYS, 0)
        def IMPLIES(self):
            return self.getToken(catlParser.IMPLIES, 0)
        def AND(self):
            return self.getToken(catlParser.AND, 0)
        def OR(self):
            return self.getToken(catlParser.OR, 0)
        def UNTIL(self):
            return self.getToken(catlParser.UNTIL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterFormula"):
                listener.enterFormula(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFormula"):
                listener.exitFormula(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFormula"):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)


    class ParpropContext(CatlPropertyContext):

        def __init__(self, parser, ctx): # actually a catlParser.CatlPropertyContext)
            super(catlParser.ParpropContext, self).__init__(parser)
            self.child = None # CatlPropertyContext
            self.copyFrom(ctx)

        def catlProperty(self):
            return self.getTypedRuleContext(catlParser.CatlPropertyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParprop"):
                listener.enterParprop(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParprop"):
                listener.exitParprop(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParprop"):
                return visitor.visitParprop(self)
            else:
                return visitor.visitChildren(self)



    def catlProperty(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = catlParser.CatlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_catlProperty, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = catlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(catlParser.T__0)
                self.state = 16
                localctx.child = self.catlProperty(0)
                self.state = 17
                self.match(catlParser.T__1)
                pass

            elif la_ == 2:
                localctx = catlParser.CatlPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.predicate()
                pass

            elif la_ == 3:
                localctx = catlParser.CatlLimitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.limit()
                pass

            elif la_ == 4:
                localctx = catlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                localctx.op = self.match(catlParser.NOT)
                self.state = 22
                localctx.child = self.catlProperty(7)
                pass

            elif la_ == 5:
                localctx = catlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                localctx.op = self.match(catlParser.EVENT)
                self.state = 24
                self.match(catlParser.T__2)
                self.state = 25
                localctx.low = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    localctx.low = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 26
                self.match(catlParser.T__3)
                self.state = 27
                localctx.high = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    localctx.high = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.match(catlParser.T__4)
                self.state = 29
                localctx.child = self.catlProperty(6)
                pass

            elif la_ == 6:
                localctx = catlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                localctx.op = self.match(catlParser.ALWAYS)
                self.state = 31
                self.match(catlParser.T__2)
                self.state = 32
                localctx.low = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    localctx.low = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.match(catlParser.T__3)
                self.state = 34
                localctx.high = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    localctx.high = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.match(catlParser.T__4)
                self.state = 36
                localctx.child = self.catlProperty(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = catlParser.FormulaContext(self, catlParser.CatlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_catlProperty)
                        self.state = 39
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 40
                        localctx.op = self.match(catlParser.IMPLIES)
                        self.state = 41
                        localctx.right = self.catlProperty(5)
                        pass

                    elif la_ == 2:
                        localctx = catlParser.FormulaContext(self, catlParser.CatlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_catlProperty)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        localctx.op = self.match(catlParser.AND)
                        self.state = 44
                        localctx.right = self.catlProperty(4)
                        pass

                    elif la_ == 3:
                        localctx = catlParser.FormulaContext(self, catlParser.CatlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_catlProperty)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        localctx.op = self.match(catlParser.OR)
                        self.state = 47
                        localctx.right = self.catlProperty(3)
                        pass

                    elif la_ == 4:
                        localctx = catlParser.FormulaContext(self, catlParser.CatlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_catlProperty)
                        self.state = 48
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 49
                        localctx.op = self.match(catlParser.UNTIL)
                        self.state = 50
                        self.match(catlParser.T__2)
                        self.state = 51
                        localctx.low = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.low = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.match(catlParser.T__3)
                        self.state = 53
                        localctx.high = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.high = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.match(catlParser.T__4)
                        self.state = 55
                        localctx.right = self.catlProperty(2)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.PredicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token
            self.duration = None # Token
            self.proposition = None # Token

        def capabilities(self):
            return self.getTypedRuleContext(catlParser.CapabilitiesContext,0)


        def VARIABLE(self):
            return self.getToken(catlParser.VARIABLE, 0)

        def RATIONAL(self):
            return self.getToken(catlParser.RATIONAL, 0)

        def INT(self):
            return self.getToken(catlParser.INT, 0)

        def resources(self):
            return self.getTypedRuleContext(catlParser.ResourcesContext,0)


        def BOOLEAN(self):
            return self.getToken(catlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return catlParser.RULE_predicate

        def enterRule(self, listener):
            if hasattr(listener, "enterPredicate"):
                listener.enterPredicate(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPredicate"):
                listener.exitPredicate(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPredicate"):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = catlParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_predicate)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                localctx.op = self.match(catlParser.T__5)
                self.state = 62
                self.match(catlParser.T__0)
                self.state = 63
                localctx.duration = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    localctx.duration = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64
                self.match(catlParser.T__3)
                self.state = 65
                localctx.proposition = self.match(catlParser.VARIABLE)
                self.state = 66
                self.match(catlParser.T__3)
                self.state = 67
                self.capabilities()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 68
                    self.match(catlParser.T__3)
                    self.state = 69
                    self.resources()


                self.state = 72
                self.match(catlParser.T__1)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                localctx.op = self.match(catlParser.BOOLEAN)
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


    class LimitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.LimitContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token
            self.proposition = None # Token

        def VARIABLE(self):
            return self.getToken(catlParser.VARIABLE, 0)

        def capabilities(self):
            return self.getTypedRuleContext(catlParser.CapabilitiesContext,0)


        def resources(self):
            return self.getTypedRuleContext(catlParser.ResourcesContext,0)


        def BOOLEAN(self):
            return self.getToken(catlParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return catlParser.RULE_limit

        def enterRule(self, listener):
            if hasattr(listener, "enterLimit"):
                listener.enterLimit(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLimit"):
                listener.exitLimit(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLimit"):
                return visitor.visitLimit(self)
            else:
                return visitor.visitChildren(self)




    def limit(self):

        localctx = catlParser.LimitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_limit)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                localctx.op = self.match(catlParser.T__6)
                self.state = 78
                self.match(catlParser.T__0)
                self.state = 79
                localctx.proposition = self.match(catlParser.VARIABLE)
                self.state = 80
                self.match(catlParser.T__3)
                self.state = 84
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 81
                    self.capabilities()
                    pass

                elif la_ == 2:
                    self.state = 82
                    self.match(catlParser.T__7)
                    self.state = 83
                    self.match(catlParser.T__8)
                    pass


                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 86
                    self.match(catlParser.T__3)
                    self.state = 87
                    self.resources()


                self.state = 90
                self.match(catlParser.T__1)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                localctx.op = self.match(catlParser.BOOLEAN)
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


    class CapabilitiesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.CapabilitiesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def capabilityRequest(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(catlParser.CapabilityRequestContext)
            else:
                return self.getTypedRuleContext(catlParser.CapabilityRequestContext,i)


        def getRuleIndex(self):
            return catlParser.RULE_capabilities

        def enterRule(self, listener):
            if hasattr(listener, "enterCapabilities"):
                listener.enterCapabilities(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCapabilities"):
                listener.exitCapabilities(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCapabilities"):
                return visitor.visitCapabilities(self)
            else:
                return visitor.visitChildren(self)




    def capabilities(self):

        localctx = catlParser.CapabilitiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_capabilities)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(catlParser.T__7)
            self.state = 95
            self.capabilityRequest()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 96
                self.match(catlParser.T__3)
                self.state = 97
                self.capabilityRequest()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(catlParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapabilityRequestContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.CapabilityRequestContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.cap = None # Token
            self.count = None # Token

        def VARIABLE(self):
            return self.getToken(catlParser.VARIABLE, 0)

        def INT(self):
            return self.getToken(catlParser.INT, 0)

        def getRuleIndex(self):
            return catlParser.RULE_capabilityRequest

        def enterRule(self, listener):
            if hasattr(listener, "enterCapabilityRequest"):
                listener.enterCapabilityRequest(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCapabilityRequest"):
                listener.exitCapabilityRequest(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCapabilityRequest"):
                return visitor.visitCapabilityRequest(self)
            else:
                return visitor.visitChildren(self)




    def capabilityRequest(self):

        localctx = catlParser.CapabilityRequestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_capabilityRequest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(catlParser.T__0)
            self.state = 106
            localctx.cap = self.match(catlParser.VARIABLE)
            self.state = 107
            self.match(catlParser.T__3)
            self.state = 108
            localctx.count = self.match(catlParser.INT)
            self.state = 109
            self.match(catlParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourcesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.ResourcesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def resourceRequest(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(catlParser.ResourceRequestContext)
            else:
                return self.getTypedRuleContext(catlParser.ResourceRequestContext,i)


        def getRuleIndex(self):
            return catlParser.RULE_resources

        def enterRule(self, listener):
            if hasattr(listener, "enterResources"):
                listener.enterResources(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResources"):
                listener.exitResources(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitResources"):
                return visitor.visitResources(self)
            else:
                return visitor.visitChildren(self)




    def resources(self):

        localctx = catlParser.ResourcesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_resources)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(catlParser.T__7)
            self.state = 112
            self.resourceRequest()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 113
                self.match(catlParser.T__3)
                self.state = 114
                self.resourceRequest()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(catlParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceRequestContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(catlParser.ResourceRequestContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.res = None # Token
            self.quantity = None # Token

        def VARIABLE(self):
            return self.getToken(catlParser.VARIABLE, 0)

        def RATIONAL(self):
            return self.getToken(catlParser.RATIONAL, 0)

        def INT(self):
            return self.getToken(catlParser.INT, 0)

        def getRuleIndex(self):
            return catlParser.RULE_resourceRequest

        def enterRule(self, listener):
            if hasattr(listener, "enterResourceRequest"):
                listener.enterResourceRequest(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitResourceRequest"):
                listener.exitResourceRequest(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitResourceRequest"):
                return visitor.visitResourceRequest(self)
            else:
                return visitor.visitChildren(self)




    def resourceRequest(self):

        localctx = catlParser.ResourceRequestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_resourceRequest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(catlParser.T__0)
            self.state = 123
            localctx.res = self.match(catlParser.VARIABLE)
            self.state = 124
            self.match(catlParser.T__3)
            self.state = 125
            localctx.quantity = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                localctx.quantity = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 126
            self.match(catlParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.catlProperty_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def catlProperty_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




