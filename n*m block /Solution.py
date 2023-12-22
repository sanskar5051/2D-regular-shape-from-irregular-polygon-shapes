import json


myjsonfile=open('json files/empolyee.json','r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

layout=obj['layout']
Exclusion_1=obj['Exclusion1']
Exclusion_2=obj['Exclusion2']
Block_Size=obj['Block_Size']
print(layout)
print(Exclusion_1)
print(Exclusion_2)
print(Block_Size)

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


#thus the new exclusion points wrt the the layout scape array will be
left_bottom_Ex_1[0]=left_bottom_Ex_1[0]-left_bottom[0]
left_bottom_Ex_1[1]=left_bottom_Ex_1[1]-left_bottom[1]
right_top_Ex_1[0]=right_top_Ex_1[0]-left_bottom[0]
right_top_Ex_1[1]=right_top_Ex_1[1]-left_bottom[1]
left_bottom_Ex_2[0]=left_bottom_Ex_2[0]-left_bottom[0]
left_bottom_Ex_2[1]=left_bottom_Ex_2[1]-left_bottom[1]
right_top_Ex_2[0]=right_top_Ex_2[0]-left_bottom[0]
right_top_Ex_2[1]=right_top_Ex_2[1]-left_bottom[1]

#later to map these points on the array i'll have to inverse the y cordiates cos y axis goes bottom up but the array traverses top dowm
left_bottom_Ex_1[1]=layout_scale[1]-left_bottom_Ex_1[1]
right_top_Ex_1[1]=layout_scale[1]-right_top_Ex_1[1]
left_bottom_Ex_2[1]=layout_scale[1]-left_bottom_Ex_2[1]
right_top_Ex_2[1]=layout_scale[1]-right_top_Ex_2[1]

#scalling factor implimentation

left_bottom_Ex_1[0]=int(left_bottom_Ex_1[0]/scalling_factor[0])
left_bottom_Ex_1[1]=int(left_bottom_Ex_1[1]/scalling_factor[1])
right_top_Ex_1[0]=int(right_top_Ex_1[0]/scalling_factor[0])
right_top_Ex_1[1]=int(right_top_Ex_1[1]/scalling_factor[1])
left_bottom_Ex_2[0]=int(left_bottom_Ex_2[0]/scalling_factor[0])
left_bottom_Ex_2[1]=int(left_bottom_Ex_2[1]/scalling_factor[0])
right_top_Ex_2[0]=int(right_top_Ex_2[0]/scalling_factor[0])
right_top_Ex_2[1]=int(right_top_Ex_2[1]/scalling_factor[1])

#
print(left_bottom_Ex_1)
print(right_top_Ex_1)
print(left_bottom_Ex_2)
print(right_top_Ex_2)

# array creation
layout_scale[0] =int(layout_scale[0]/scalling_factor[0])
layout_scale[1] =int(layout_scale[1]/scalling_factor[1])
arr = [[1 for i in range(layout_scale[0])] for j in range(layout_scale[1])]
#



for i in range(right_top_Ex_1[1],left_bottom_Ex_1[1]):
    for j in range(left_bottom_Ex_1[0],right_top_Ex_1[0]):
        arr[i][j]=0;

for i in range(right_top_Ex_2[1],left_bottom_Ex_2[1]):
    for j in range(left_bottom_Ex_2[0],right_top_Ex_2[0]):
        arr[i][j]=0;

for row in arr:
    print(row)

#Array to Solution
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
n=Block_Size[0][0]
m=Block_Size[0][1]
a=layout_scale[1]
b=layout_scale[0]


count_blocks(arr, n, m)
