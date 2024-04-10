from typing import Optional, List, Tuple


def find_queens_pos(start_pos: Optional[List[Tuple[int, int]]] = None) -> Optional[List[Tuple[int, int]]]:
    queens_pos = start_pos.copy() if start_pos is not None else []
    if len(queens_pos) == 8:
        return queens_pos
    queen_x = len(queens_pos)
    for queen_y in range(8):
        if not check_if_queen_is_under_attack(queens_pos, (queen_x, queen_y)):
            queens_pos.append((queen_x, queen_y))
            res = find_queens_pos(queens_pos)
            if res is not None:
                return res
            queens_pos.pop()
    return None


def check_if_queen_is_under_attack(queens_pos, queen_coords):
    for queen_pos in queens_pos:
        if queen_pos[0] == queen_coords[0]:
            return True
        if queen_pos[1] == queen_coords[1]:
            return True
        if abs(queen_pos[0] - queen_coords[0]) == abs(queen_pos[1] - queen_coords[1]):
            return True
    return False


def format_input(queens_pos):
    res = ""
    for pos in queens_pos:
        res += f"{'ABCDEFGH'[pos[0]]}{pos[1] + 1} "
    return res.strip()


print(format_input(find_queens_pos()))
