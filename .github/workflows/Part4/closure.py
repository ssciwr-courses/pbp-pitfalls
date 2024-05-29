# modify the multiplier below so that it returns 
# the expected result: 
# [2, 4, 6, 8, 10]
def make_multiplier_of(n):
        def multiplier(j):
            return n * j
        return multiplier

# for testing purposes, we wrap this in a function
def main():
    times_x = [make_multiplier_of(i) for i in range(1,6)]
    times_table = []
    for times in times_x:
        print(times(2))
        times_table.append(times(2))
    return times_table

if __name__ == "__main__":
    main()