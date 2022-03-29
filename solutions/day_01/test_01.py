import pytest
import solution

testdata = """
199
200
208
210
200
207
240
269
260
263
""".split()
testdata = [int(n) for n in testdata]

@pytest.mark.parametrize(("part", "output"), [(1, 7), (2, 5)])
def test_solver(part, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(testdata) == output
