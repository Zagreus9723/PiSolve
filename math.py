#Convert img to LaTeX, solve with https://calculator-algebra.org/
#
from PIL import Image
from pix2tex.cli import LatexOCR
from io import StringIO
import sys
import requests
import json
import sympy
import math
import numpy
import numpy as np

rads = {
    ".87": "sqrt(3)/2",
    ".71": "sqrt(2)/2",
    ".5": "1/2",
    "1": "1"
}

reds = ['.87', '.71', '.5']

def unitCircTrig(sol):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    eval("print(math." + str(sol).replace('pi', 'math.pi') + ")")
    sys.stdout = old_stdout
    message = mystdout.getvalue().replace("\n", "")
    return message

img = Image.open('Screenshot 2024-02-20 213209.png')
model = LatexOCR()
ltx = model(img).replace("\ ", "")
print(ltx)

code = requests.get('https://api.computegpt.org/?q=' + "Solve. " + ltx).content
print(code.decode())
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()
exec(code)
sys.stdout = old_stdout
message = mystdout.getvalue().replace("\n", "")

try:
    if round(int(message), 2) in rads:
        message = f"{str(message)},,,{str(unitCircTrig(message))},,,{str(rads[str(round(float(unitCircTrig(message)), 2))])}"
except:
    pass

print(message)







#-----------------------------------------
# from sympy import init_printing
# import math
# from sympy.parsing.latex import parse_latex
# from sympy.abc import x
# from sympy import solve, solveset

# ltx = """3x^{7}+36x^{5}+108x^{3}"""
# equation = parse_latex(ltx)
# sol = solve(equation, x)
# for x in range(len(sol)):
#     if 'pi' in str(sol[x]):
#         sol[x] = f"{str(sol[x])},,,{str(unitCircTrig(sol[x]))},,,{str(rads[str(round(float(unitCircTrig(sol[x])), 2))])}"
# print(sol)