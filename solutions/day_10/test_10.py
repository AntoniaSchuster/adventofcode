import pytest
import solution

testdata = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".split("\n")
testdata = [line.strip() for line in testdata if line]

@pytest.mark.parametrize(("part", "output"), [(1, 26397), (2, 288957)])
def test_solver(part, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(testdata) == output