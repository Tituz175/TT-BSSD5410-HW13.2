def odd_bit_to_even(number):
    numberBin = str(bin(number)[2:].zfill(8))
    lenNumber = len(numberBin)
    result = ""

    i = 0
    while i < lenNumber:
        result += numberBin[i + 1]
        result += numberBin[i]
        i += 2
    return int(result, 2)
