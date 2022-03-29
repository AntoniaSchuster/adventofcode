import pytest
import solution

testdata = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".split("\n")
testdata = [line.strip() for line in testdata if line]
testdata = (testdata[0], testdata[1:])
print(testdata)

@pytest.mark.parametrize(("part", "output"), [(1, 1588), (2, 2188189693529)])
def test_solver(part, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(testdata) == output