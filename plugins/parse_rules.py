#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("rules.xml")
rules = DOMTree.documentElement
if rules.hasAttribute("shelf"):
   print ("Root element : %s" % rules.getAttribute("shelf"))

# 在集合中获取所有rules
rulesss = rules.getElementsByTagName("rule")

# 打印每个rule的详细信息
for rule in rulesss:
   print ("***************Rule***************")
   rule_id = rule.getElementsByTagName('rule-id')[0]
   print ("Rule-id: %s" % rule_id.childNodes[0].data)
   typesss = rule.getElementsByTagName('type')
   for type in typesss:
       print ("Type: %s" % type.childNodes[0].data)
   condition = rule.getElementsByTagName('condition')[0]
   print ("Condition: %s" % condition.childNodes[0].data)
   compatiable = rule.getElementsByTagName('compatiable')[0]
   print ("Compatiable: %s" % compatiable.childNodes[0].data)
   description = rule.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)
   if (rule.getElementsByTagName('except-condition')):
      except_condition = rule.getElementsByTagName('except-condition')[0]
      print("Except-condition: %s" % except_condition.childNodes[0].data)
   statementssss = rule.getElementsByTagName("statement")
   stmt_tag = 0
   for statement in statementssss:
       print("Statement" + str(stmt_tag) + ": %s" % statement.childNodes[0].data)
       stmt_tag= stmt_tag+1
