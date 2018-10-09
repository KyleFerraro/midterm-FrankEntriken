import midterm as m
import math

def test_sequence_attribs():
    s = m.MysterySequence(2.5, x0 = 0.1, N = 10)
    assert math.isclose(s.r, 2.5), "r value not 2.5"
    assert math.isclose(s.x0, 0.1), "x0 value not 0.1"
    assert s.N == 10, "N value not 10"

def test_sequence_eval_1():
    s = m.MysterySequence(2.5)
    xs = s()
    assert math.isclose(xs[-1], 0.6), "100th element with r=2.5 is not correct"

def test_sequence_eval_2():
    s = m.MysterySequence(3.5441)
    s.evaluate()
    assert math.isclose(s.xs[-1], 0.5291470223555306), "100th element with r=3.5441 is not correct"
