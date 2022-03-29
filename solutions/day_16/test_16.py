import pytest
import solution


testdata_1 = [("8A004A801A8002F478", 16), ("620080001611562C8802118E34", 12), ("C0015000016115A2E0802F182340", 23), ("A0016C880162017C3686B18A3D4780", 31)]
testdata_2 = [("C200B40A82", 3), ("04005AC33890", 54), ("880086C3E88112", 7), ("CE00C43D881120", 9), ("D8005AC2A8F0", 1), ("F600BC2D8F", 0), ("9C005AC2F8F0", 0), ("9C0141080250320F1802104A08", 1)]
testdata = [(1, x[0], x[1]) for x in testdata_1] + [(2, x[0], x[1]) for x in testdata_2]

@pytest.mark.parametrize(("part", "input", "output"), testdata)
def test_solver(part, input, output):
    solver = "solve_first" if part == 1 else "solve_second"
    if hasattr(solution, solver):
        solve = getattr(solution, solver)
        assert solve(input) == output
