def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise AssertionError("lists should be in the same height")
    if any(h == 0 for h in height):
        raise AssertionError("l3adam ya dinek")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise AssertionError("weight should containe only numbers")
    if not all(isinstance(h, (int, float)) for h in height):
        raise AssertionError("height should containe only numbers")
    BMi: list = []
    for i in range(len(height)):
        BMi.append(weight[i] / (height[i] ** 2))
    return BMi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise AssertionError("bmi should containe only numbers")
    return [b > limit for b in bmi]
