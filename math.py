#Convert img to LaTeX, solve with https://calculator-algebra.org/
#
from PIL import Image
from pix2tex.cli import LatexOCR
from sympy.parsing.latex import parse_latex
from sympy.abc import x
from sympy import solve, solveset
from io import StringIO
import sys
from sympy import init_printing
import math

rads = {
    "0.87": "sqrt(3)/2",
    "0.71": "sqrt(2)/2",
    "0.5": "1/2",
    "1.0": "1"
}

def unitCircTrig(sol):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    eval("print(math." + str(sol).replace('pi', 'math.pi') + ")")
    sys.stdout = old_stdout
    message = mystdout.getvalue().replace("\n", "")
    return message

img = Image.open('lagrida_latex_editor.png')
model = LatexOCR()
ltx = model(img).replace("\ ", "")
print(ltx)
# ltx = """3x^{7}+36x^{5}+108x^{3}"""
equation = parse_latex(ltx)
sol = solve(equation, x)
for x in range(len(sol)):
    if 'pi' in str(sol[x]):
        sol[x] = f"{str(sol[x])},,,{str(unitCircTrig(sol[x]))},,,{str(rads[str(round(float(unitCircTrig(sol[x])), 2))])}"
print(sol)