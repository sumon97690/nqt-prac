array = [1,2,3,4,5]
shift = 2

def rightRotation(array,shift):
    for i in range(0,shift):
        temp = array[len(array)-1]
        for j in range(len(array)-1,0,-1):
            array[j] = array[j-1]
            
        array[0] = temp
    return array

rotatedArray = rightRotation(array,shift)
print(f"After rotation: {rotatedArray}")