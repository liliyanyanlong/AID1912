"""
有两个线程，同时运行，一个线程要打印1--52这52个数字，另一个线程打印A-Z这26个字母
希望通过互斥机制的控制，让打印的结果为12A34B56C....5152Z

提示： 可能用多个同步互斥对象
"""