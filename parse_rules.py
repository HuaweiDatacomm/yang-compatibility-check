#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("C:\\Users\\00123726\\PycharmProjects\\pyang\\pyang\\rules1.xml")
rules = DOMTree.documentElement
if rules.hasAttribute("shelf"):
   print ("Root element : %s" % rules.getAttribute("shelf"))

# 在集合中获取所有rules
rulesss = rules.getElementsByTagName("rule")
fo = open("C:\\Users\\00123726\\PycharmProjects\\pyang\\pyang\\rules.txt", "w")
# 打印每个rule的详细信息
for rule in rulesss:
   fo.write ("***************Rule_start***************\n")
   rule_id = rule.getElementsByTagName('rule-id')[0]
   fo.write ("Rule-id: %s" % rule_id.childNodes[0].data)
   fo.write("\n")
   typesss = rule.getElementsByTagName('type')
   for type in typesss:
       fo.write ("Type: %s" % type.childNodes[0].data)
       fo.write("\n")
   condition = rule.getElementsByTagName('condition')[0]
   fo.write ("Condition: %s" % condition.childNodes[0].data)
   fo.write("\n")
   compatiable = rule.getElementsByTagName('compatiable')[0]
   fo.write ("Compatiable: %s" % compatiable.childNodes[0].data)
   fo.write("\n")
   description = rule.getElementsByTagName('description')[0]
   fo.write ("Description: %s" % description.childNodes[0].data)
   fo.write("\n")
   if (rule.getElementsByTagName('except-condition')):
      except_condition = rule.getElementsByTagName('except-condition')[0]
      fo.write("Except-condition: %s" % except_condition.childNodes[0].data)
      fo.write("\n")
   statementssss = rule.getElementsByTagName("statement")
   stmt_tag = 0
   for statement in statementssss:
       fo.write("Statement" + str(stmt_tag) + ": %s" % statement.childNodes[0].data)
       fo.write("\n")
       stmt_tag= stmt_tag+1
   fo.write("***************Rule_end***************")
   fo.write("\n")
