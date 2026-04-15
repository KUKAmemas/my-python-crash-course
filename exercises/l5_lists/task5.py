# Write the body of the function that returns
# a list which contains integers in a range [1; n]
def fill(n: int) -> list[int]:
    l = []
    for i in range(1, n+1):
        l.append(i)
    return l


# Do not change the below's code
if __name__ == "__main__":
    assert fill(3) == [1, 2, 3]
    assert fill(0) == []
    assert fill(4) == [1, 2, 3, 4]
    assert fill(1) == [1]
