import json


myjsonfile=open('json files/empolyee.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

layout=obj['layout']
Exclusion_1=obj['Exclusion1']
Exclusion_2=obj['Exclusion2']
print(layout)
print(Exclusion_1)
print(Exclusion_2)

#closed polygon check

layout_len=len(layout)
Ex1_len=len(Exclusion_1)
Ex2_len=len(Exclusion_2)

if(layout[0] == layout[layout_len - 1]):
    print("the layout is a closed polygon ")
else:
    print("the layout is not a closed polygon")
if(Exclusion_1[0] == Exclusion_1[Ex1_len - 1]):
    print("the Exclusion 1 is a closed polygon ")
else:
    print("the Exclusion 1 is not a closed polygon")
if(Exclusion_2[0] == Exclusion_2[Ex2_len - 1]):
    print("the Exclusion 2 is a closed polygon ")
else:
    print("the Exclusion 2 is not a closed polygon")

#boundry defination for layout

smallest_x_layout=1000000000
for i in range(0,layout_len):
    if(layout[i][0] < smallest_x_layout):
        smallest_x_layout=layout[i][0]

smallest_y_layout=10000000000
for i in range(0,layout_len):
    if(layout[i][1] < smallest_y_layout):
        smallest_y_layout=layout[i][1]

left_bottom=[smallest_x_layout,smallest_y_layout]

largest_x_layout=-10^9
for i in range(0,layout_len):
    if(layout[i][0] > largest_x_layout):
        largest_x_layout=layout[i][0]

largest_y_layout=10^9
for j in range(0,layout_len):
    if(layout[i][1] > largest_y_layout):
        largest_y_layout=layout[i][1]

right_top=[largest_x_layout,largest_y_layout]

print("left bottom of the layout:")
print(left_bottom)
print("right top of the layout:")
print(right_top)

layout_scale=[largest_x_layout-smallest_x_layout,largest_y_layout-smallest_y_layout]

#boundry defination for Exclusion 1

smallest_x_Ex_1=1000000000
for i in range(0,Ex1_len):
    if(Exclusion_1[i][0] < smallest_x_Ex_1):
        smallest_x_Ex_1=Exclusion_1[i][0]

smallest_y_Ex_1=10000000000
for i in range(0,Ex1_len):
    if(Exclusion_1[i][1] < smallest_y_Ex_1):
        smallest_y_Ex_1=Exclusion_1[i][1]

left_bottom_Ex_1=[smallest_x_Ex_1,smallest_y_Ex_1]

largest_x_Ex_1=-10^9
for i in range(0,Ex1_len):
    if(Exclusion_1[i][0] > largest_x_Ex_1):
        largest_x_Ex_1=Exclusion_1[i][0]

largest_y_Ex_1=10^9
for j in range(0,Ex1_len):
    if(Exclusion_1[i][1] > largest_y_Ex_1):
        largest_y_Ex_1=Exclusion_1[i][1]

right_top_Ex_1=[largest_x_Ex_1,largest_y_Ex_1]

print("left bottom of the Exclusion 1:")
print(left_bottom_Ex_1)
print("right top of the Exclusion 1:")
print(right_top_Ex_1)

Ex_1_scale=[largest_x_Ex_1-smallest_x_Ex_1,largest_y_Ex_1-smallest_y_Ex_1]

#boundry Defination of Exclusion 2
smallest_x_Ex_2=1000000000
for i in range(0,Ex2_len):
    if(Exclusion_2[i][0] < smallest_x_Ex_2):
        smallest_x_Ex_2=Exclusion_2[i][0]

smallest_y_Ex_2=10000000000
for i in range(0,Ex2_len):
    if(Exclusion_2[i][1] < smallest_y_Ex_2):
        smallest_y_Ex_2=Exclusion_2[i][1]

left_bottom_Ex_2=[smallest_x_Ex_2,smallest_y_Ex_2]

largest_x_Ex_2=-10^9
for i in range(0,Ex2_len):
    if(Exclusion_2[i][0] > largest_x_Ex_2):
        largest_x_Ex_2=Exclusion_2[i][0]

largest_y_Ex_2=10^9
for j in range(0,Ex2_len):
    if(Exclusion_2[i][1] > largest_y_Ex_2):
        largest_y_Ex_2=Exclusion_2[i][1]

right_top_Ex_2=[largest_x_Ex_2,largest_y_Ex_2]

print("left bottom of the Exclusion 2:")
print(left_bottom_Ex_2)
print("right top of the Exclusion 2:")
print(right_top_Ex_2)

Ex_2_scale=[largest_x_Ex_2-smallest_x_Ex_2,largest_y_Ex_2-smallest_y_Ex_2]

#thus the boundries of the the blocks is defined

#hcf
# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf_x= compute_hcf(layout_scale[0],compute_hcf(Ex_1_scale[0],Ex_2_scale[0]))
hcf_y= compute_hcf(layout_scale[1],compute_hcf(Ex_1_scale[1],Ex_2_scale[1]))

scalling_factor=[hcf_x,hcf_y]
print("the scalling factor is:")
print(scalling_factor)
arr = [[1 for i in range(layout_scale[0])] for j in range(layout_scale[1])]
#for row in arr:
#   print(row)

#thus the new exclusion points wrt the the layout scape array will be
left_bottom_Ex_1[0]=left_bottom_Ex_1[0]-35
left_bottom_Ex_1[1]=left_bottom_Ex_1[1]-12
right_top_Ex_1[0]=right_top_Ex_1[0]-35
right_top_Ex_1[1]=right_top_Ex_1[1]-12
left_bottom_Ex_2[0]=left_bottom_Ex_2[0]-35
left_bottom_Ex_2[1]=left_bottom_Ex_2[0]-12
right_top_Ex_2[0]=right_top_Ex_2[0]-35
right_top_Ex_2[1]=right_top_Ex_2[1]-12

#later to map these points on the array i'll have to inverse the y cordiates cos y axis goes bottom up but the array traverses top dowm
left_bottom_Ex_1[1]=layout_scale[1]-left_bottom_Ex_1[1]
right_top_Ex_1[1]=layout_scale[1]-right_top_Ex_1[1]
left_bottom_Ex_2[1]=layout_scale[1]-left_bottom_Ex_2[1]
right_top_Ex_2[1]=layout_scale[1]-right_top_Ex_2[1]

print(left_bottom_Ex_1)
print(right_top_Ex_1)
print(left_bottom_Ex_2)
print(right_top_Ex_2)
for i in range(right_top_Ex_1[1],left_bottom_Ex_1[1]):
    for j in range(left_bottom_Ex_1[0],right_top_Ex_1[0]):
        arr[i][j]=0;

for i in range(right_top_Ex_2[1],left_bottom_Ex_2[1]):
    for j in range(left_bottom_Ex_2[0],right_top_Ex_2[0]):
        arr[i][j]=0;

#for row in arr:
#  print(row)


#array algorithm codeeeee

def is_empty(arr, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count = 1
    if count == 0:
        return -1
    else:
        return 1


n=layout_scale[1]
m=layout_scale[0]
arr1 = [['.' for _ in range(m)] for _ in range(n)]
alpha_var = 0
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

while is_empty(arr, n, m) == 1:
    max_area = 0
    p, q, r, s, num1 = 0, 0, 0, 0, 0

    for i in range(n):
        for j in range(m):
            print(f"checking for point({i},{j})")
            for a in range(i, n):
                for b in range(j, m):
                    num = 0
                    count = 0


                    for z in range(i, a + 1):
                        for y in range(j, b + 1):
                            if arr[z][y] != 1:
                                count = 1
                            num += 1

                    if count == 0:
                        if max_area < num:
                            p, q, r, s, num1 = i, j, a, b, num
                            max_area = num
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print(f"({p},{q})-({r},{s})")
    print("area of the above rectangle -", max_area, "\n")
    print("after removing the current largest rectangle the space looks like")


    for i in range(p, r + 1):
        for j in range(q, s + 1):
            arr[i][j] = 0
            arr1[i][j] = alpha[alpha_var]
    alpha_var = alpha_var + 1

print("\nthus the final output for the given problem with all largest rectangles looks like ")
for i in range(n):
    for j in range(m):
        print(arr1[i][j], end=" ")
    print()
# here all the elements having the same alphabets form a rectangle together
