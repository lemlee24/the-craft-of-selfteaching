"""
演示 mycode.py 中 age 相关代码的执行效果
"""

print("=== 测试场景 1: 未成年人 (age = 15) ===")
age = 15
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')

print("\n=== 测试场景 2: 成年人 (age = 25) ===")
age = 25
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')

print("\n=== 测试场景 3: 刚好 18 岁 (age = 18) ===")
age = 18
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')

print("\n=== 如果需要交互式输入，请运行以下代码 ===")
print("age = input('Please tell me your age: ')")
print("age = int(age)")
print("if age < 18:")
print("    print('I can not sell you drinks...')")
print("else:")
print("    print('Have a nice drink!')")


import subprocess
subprocess.run(['/Users/lamlee/Desktop/Qorder/the-craft-of-selfteaching/.venv/bin/python', '/Users/lamlee/Desktop/Qorder/the-craft-of-selfteaching/test_age.py'])