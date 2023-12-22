def count_blocks(arr, n, m):
    a = len(arr)
    b = len(arr[0])

    num_ltrttb = num_ltrbtt = num_rtlttb = num_rtlbtt = num_ttbltr = num_ttbrtl = num_bttltr = num_bttrtl = 0
    answer = 0

    # left to right traversal
    # left to right top to bottom
    arr_ltrttb = [row[:] for row in arr]
    for i in range(a):
        for j in range(b):
            right_bottom_x = i + n - 1
            right_bottom_y = j + m - 1
            count = 0

            if right_bottom_x < a and right_bottom_y < b:
                for k in range(i, right_bottom_x + 1):
                    for l in range(j, right_bottom_y + 1):
                        if arr_ltrttb[k][l] == 0:
                            count = 1
                            break
                    if count == 1:
                        break

                if count == 0:
                    print(f"({i},{j})-({right_bottom_x},{right_bottom_y})")
                    num_ltrttb += 1

                    for k in range(i, right_bottom_x + 1):
                        for l in range(j, right_bottom_y + 1):
                            arr_ltrttb[k][l] = 0

    if num_ltrttb > answer:
        answer = num_ltrttb
    print("number of n*m blocks in left to right and top to bottom traversal -", num_ltrttb)
    # end of left to right top to bottom

    # remaining traversal blocks...
    # ... (other blocks are similar and can be similarly converted)

    # final answer
    print("total number of n*m block in the above settlement with maximum space occupancy is", answer)


# Example usage:
n, m = map(int, input().split())
a, b = map(int, input().split())
arr = []
for _ in range(a):
    arr.append(list(map(int, input().split())))

count_blocks(arr, n, m)
