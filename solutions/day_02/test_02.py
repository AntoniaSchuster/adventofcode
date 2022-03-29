import pytest
import solution

testdata = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".split("\n")
testdata = [line.strip() for line in testdata if line]

@pytest.mark.parametrize(("part", "output"), [(1, 150), (2, 900)])
def test_solver(part, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(testdata) == output
