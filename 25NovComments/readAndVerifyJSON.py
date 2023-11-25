import numpy as np

class readAndVerifyJSON:
    filepath;
    filename;
    layout;
    exclusionlist; # array of arrays
    layoutrange, scaledlayoutrange;  #  store the top left and botm right
    exclusionrange, scaledexclusionrange; # array of arrays
    scalefactor;   # array value
    layoutmatrix; # construct the matrix containing '0's and '1's based on scaled layout. '0's indicates  exclusions

    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def readJSONData(self):
        jsondata = myjsonfile.read()
        obj = json.loads(jsondata)
        layout = obj['layout']
        exclusionlist = obj['ExclusionList'] #Array of Array

    def validateJSONData(self):

        if (layout[0] == layout[layout_len - 1]):
            print("the layout is a closed polygon ")
        else:
            print("the layout is not a closed polygon")
        if (Exclusion_1[0] == Exclusion_1[Ex1_len - 1]):
            print("the Exclusion 1 is a closed polygon ")
        else:
            print("the Exclusion 1 is not a closed polygon")
        if (Exclusion_2[0] == Exclusion_2[Ex2_len - 1]):
            print("the Exclusion 2 is a closed polygon ")
        else:
            print("the Exclusion 2 is not a closed polygon")

    def extractLayoutRange(self):
        arr = [
            [37, 78],
            [149, 78],
            [149, 12],
            [35, 12],
            [35, 78],
            [37, 78]
        ]
        # print(min(arr[0]))
        # print(max(arr[0]))
        # print(min(arr[1]))
        # print(max(arr[1]))

        print(np.min(arr, axis=0)[0])
        print(np.max(arr, axis=0)[0])

        print(np.min(arr, axis=0)[1])
        print(np.max(arr, axis=0)[1])
        # size of exclusionrange is equal to the size of exclusionlist

    def compute_hcf(x, y):
        while (y):
            x, y = y, x % y
        return x

    def computeScalingFactor(self):
        hcf_x = compute_hcf(layout_scale[0], compute_hcf(Ex_1_scale[0], Ex_2_scale[0]))
        hcf_y = compute_hcf(layout_scale[1], compute_hcf(Ex_1_scale[1], Ex_2_scale[1]))
        scalling_factor=[hcf_x,hcf_y]
        print("the scalling factor is:")
        print(scalling_factor)

if __name__ == "__main__":
    app = readAndVerifyJSONData("","employee.json")