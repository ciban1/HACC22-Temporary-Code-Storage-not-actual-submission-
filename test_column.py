import js2py
# from script import *
#
# js2py.translate_file("hey.js", "temp.py")
# script.wish("GeeksforGeeks")

code_2 = "function f(x) {return x+x;}"
res_2 = js2py.eval_js(code_2)

print(res_2(5))