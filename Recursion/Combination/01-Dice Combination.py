# Given a Dice, find how many ways are there to form the target with n face.

def diceComb(target, face, cur):
    if target == 0:
        return [cur]

    ways = []
    for i in range(1, face + 1):
        if i <= target:
            ways.extend(diceComb(target - i, face, cur+str(i)))

    return ways

