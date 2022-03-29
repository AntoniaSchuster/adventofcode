import pytest
import solution

testdata = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".split("\n")
testdata = [line.strip() for line in testdata if line]

@pytest.mark.parametrize(("part", "output"), [(1, 5), (2, 12)])
def test_solver(part, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(testdata) == output