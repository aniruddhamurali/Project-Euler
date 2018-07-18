def main():
    firstdigitDict = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
    seconddigitDict = {'0':0, '1':5, '2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
    thirddigitDict = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
    #fourthdigitDict = {'1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}

    total = 0

    for n in range(101,113):
        digits = list(map(int, str(n)))

        if len(digits) == 1:
            total = total + firstdigitDict[str(digits[0])]


        if len(digits) == 2:
            if digits == [1,0]:
                total = total + 3   # +3 is for ten

            elif digits == [1,1] or digits == [1,2]:
                total = total + 6   # +6 is for eleven or twelve

            elif digits[:] == [1,3]:
                total = total + 8   # +8 for thirteen

            elif digits[:] == [1,5]:
                total = total + 7   # +7 for fifteen

            elif digits[:] == [1,8]:
                total = total + 8   # +8 for eighteen

            elif digits[:] <= [1,9]:
                total = total + firstdigitDict[str(digits[1])] + 4   # +4 for teen

            else:
                total = total + seconddigitDict[str(digits[0])] + firstdigitDict[str(digits[1])]



        if len(digits) == 3:
            if digits[1:] == [1,0]:
                total = total + thirddigitDict[str(digits[0])] + 13   # +3 is for ten, +10 for 'hundred and'

            elif digits[1:] == [1,1] or digits == [1,2]:
                total = total + thirddigitDict[str(digits[0])] + 16   # +6 is for eleven or twelve, + 10 for 'hundred and'

            elif digits[1:] == [1,3]:
                total = total + thirddigitDict[str(digits[0])] + 18   # +8 for thirteen, + 10 for 'hundred and'

            elif digits[1:] == [1,5]:
                total = total + thirddigitDict[str(digits[0])] + 17   # +7 for fifteen, + 10 for 'hundred and'

            elif digits[:] <= [1,9]:
                total = total + thirddigitDict[str(digits[0])] + firstdigitDict[str(digits[2])] + 14   # +4 for teen, +10 for 'hundred and'
                
            else:
                total = total + thirddigitDict[str(digits[0])] + seconddigitDict[str(digits[1])] + firstdigitDict[str(digits[2])] + 10   # +10 is for 'hundred and'


        if digits == [1,0,0,0]:
            total = total + 11   # +11 for 'one thousand'

    return total
            


            

            
