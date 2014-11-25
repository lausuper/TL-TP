# coding: utf-8

class Node:
  def __init__(self):
    self.children = []

  def __len__(self):
    return len(self.children)

  def __getitem__(self, index):
    return self.children[index]

class Rule(Node):
  def __init__(self, name, element):
    Node.__init__(self)
    self.name = name
    self.children.append(element)

  def __str__(self):
    return self.name

class FinalRule(Rule): pass

class StartRule(Rule):
  def __init__(self, element):
    Rule.__init__(self, '$', element)

class ArithExpr(Node):
  def value(self):
    raise NotImplementedError()

class Number(ArithExpr):
  def __init__(self, value):
    ArithExpr.__init__(self)
    self._value = value

  def value(self):
    return self._value

  def __str__(self):
    return str(self._value)

class UnaryOp(ArithExpr):
  def __init__(self, child):
    ArithExpr.__init__(self)
    self.children.append(child)

class UPlus(UnaryOp):
  def value(self):
    return self.children[0].value()

class UMinus(UnaryOp):
  def value(self):
    return -1 * self.children[0].value()

class BinaryOp(ArithExpr):
  def __init__(self, left, right):
    ArithExpr.__init__(self)
    self.children.append(left)
    self.children.append(right)

class Plus(BinaryOp):
  def value(self):
    return self.children[0].value() + self.children[1].value()

class Minus(BinaryOp):
  def value(self):
    return self.children[0].value() + self.children[1].value()

class Times(BinaryOp):
  def value(self):
    return self.children[0].value() * self.children[1].value()

class Divide(BinaryOp):
  def value(self):
    return self.children[0].value() / self.children[1].value()

class Parenthesis(ArithExpr):
  def __init__(self, child):
    ArithExpr.__init__(self)
    self.children.append(child)

  def value(self):
    return self.children[0].value()

class Element(Node): pass

class Box(Element): pass

class Ball(Element): pass

class Underscore(Element): pass

class RuleElement(Element):
  def __init__(self, name):
    Element.__init__(self)
    self.name = name

  def __str__(self):
    return self.name

class Transform(Element):
  def __init__(self, child, param):
    Element.__init__(self)
    self.children.append(child)
    self.param = param

class RX(Transform): pass

class RY(Transform): pass

class RZ(Transform): pass

class SX(Transform): pass

class SY(Transform): pass

class SZ(Transform): pass

class S(Transform): pass

class TX(Transform): pass

class TY(Transform): pass

class TZ(Transform): pass

class CR(Transform): pass

class CG(Transform): pass

class CB(Transform): pass

class D(Transform): pass

class And(Element):
  def __init__(self, left, right):
    Element.__init__(self)
    self.children.append(left)
    self.children.append(right)

class Or(Element):
  def __init__(self, left, right):
    Element.__init__(self)
    self.children.append(left)
    self.children.append(right)

class Power(Element):
  def __init__(self, child, power):
    Element.__init__(self)
    self.children.append(child)
    self.power = power

class Group(Element):
  def __init__(self, child):
    Element.__init__(self)
    self.children.append(child)

class Optional(Element):
  def __init__(self, child):
    Element.__init__(self)
    self.children.append(child)