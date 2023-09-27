from time import sleep, time
from functools import wraps

def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper

@record_time
def example_function():
    """一个简单的示例函数"""
    sleep(2)  # 模拟函数执行的耗时操作
    print("示例函数执行完毕")

# 以下函数，包装器默认不会包装并执行
@record_time
def example2_function():
    """一个简单的示例函数"""
    sleep(3)  # 模拟函数执行的耗时操作
    print("示例函数执行完毕")

example_function()
example2_function()