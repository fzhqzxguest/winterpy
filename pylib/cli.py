#!/usr/bin/env python3
# vim:fileencoding=utf-8

'''一些在命令行上使用的便捷函数'''

import os
from path import path

def findbroken(p):
  '''递归寻找断掉的软链接'''
  ret = []

  for i in p.list():
    if i.isdir():
      ret.extend(findbroken(i))
    elif not i.exists():
      ret.append(i)

  return ret

def delbroken(p=path('.')):
  '''删掉该目录下断掉的软链接'''
  l = [x for x in p.list() if not x.exists()]
  for i in l:
    i.unlink()
    print('已删除', i)

def repl(local, histfile=None):
  import readline
  import rlcompleter
  readline.parse_and_bind('tab: complete')
  if histfile is not None and os.path.exists(histfile):
    readline.read_history_file(histfile)
  import code
  code.interact(local=local)
  if histfile is not None:
    readline.write_history_file(histfile)

