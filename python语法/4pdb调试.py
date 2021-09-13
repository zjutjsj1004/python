# pdb --- Python 的调试器:https://docs.python.org/zh-cn/3/library/pdb.html
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

# 调试: 
# 1. python3 -m pdb 4pdb调试.py 
# 2.  b 4pdb调试.py:8    第八行添加断点
# 3. c   运行
# 4. p n  / p s   打印变量值