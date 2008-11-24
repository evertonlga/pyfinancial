#****************************************************************************
# libraryTests.py, This module contains unit tests for our library 
#
# pyFinancial, a financial library for python users
# Copyright (C) 2008, Felipe Leal, David Candeia, Everton Leandro and Diego Dantas
#*****************************************************************************

from financialLibrary.pyFinancialLibrary import *
import unittest

class LibraryTestCase (unittest.TestCase):
    
    def testAdd(self):
        """ Verifies the add method of pyFinancialLibrary.py """
        
        assert add(1, 2) == 3
        assert add(0, 0) == 0
        assert add(-5, 5) == 0
        assert add(-0.3, 5) == 4.7
        assert add(-0.3, -5) == -5.3
        assert add(-0.2372, 0.0001) == -0.2371
        assert add(-0.2372, -0.00001) == -0.23721
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #self.assertEquals(e.message, "Incompatibility of types.")
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        
    
    def testMinus(self):
        """ Verifies the sub method of pyFinancialLibrary.py """
        
        assert sub(2, 1) == 1
        assert sub(0, 0) == 0
        assert sub(5, -5) == 10
        assert sub(5, -0.3) == 5.3
        assert sub(-5, -0.3) == -4.7
#        assert sub(-0.2372, 0.0001) == -0.2373
#        assert sub(-0.2372, -0.00001) == -0.23719
        
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
    
    def testMult(self):
        """ Verifies the mult method of pyFinancialLibrary.py """
        
        assert mult(1, 2) == 2
        assert mult(0, 0) == 0
        assert mult(-5, 5) == -25
        assert mult(-0.3, 5) == -1.5
        assert mult(-0.3, -5) == 1.5
        assert mult(-0.2372, 0.0001) == -0.00002372
#        assert mult(-0.2372, -0.00001) == 0.000002372
        
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."

    def testDiv(self):
        """ Verifies the div method of pyFinancialLibrary.py """
        
        assert div(1, 2) == 0.5
        assert div(2, 1) == 2
        assert div(-5, 5) == -1
        assert div(-0.3, 5) == -0.06
        assert div(-0.3, -5) == 0.06
        assert div(-0.2372, 0.0001) == -2372
#        assert div(-0.2372, -0.00001) == 23720
        try:
            add(3, "-5as")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, "*")           
            self.fail("Expected a ValueError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        try:
            add(3, list())           
            self.fail("Expected a TypeError")
        except TypeError, e:
            pass
            #assert e.message == "Incompatibility of types."
        
        try:
            div(3, 0)           
            self.fail("Expected a ZeroDivisionError")
        except ZeroDivisionError, e:
            pass
            #assert e.message == "Zero division."
        