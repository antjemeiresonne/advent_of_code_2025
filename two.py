import textwrap

puzzleInput = "3299143-3378031,97290-131156,525485-660941,7606-10180,961703-1031105,6856273537-6856492968,403537-451118,5330-7241,274725-384313,27212572-27307438,926609-954003,3035-3822,161-238,22625-31241,38327962-38415781,778-1155,141513-192427,2-14,47639-60595,4745616404-4745679582,1296-1852,80-102,284-392,4207561-4292448,404-483,708177-776613,65404-87389,5757541911-5757673432,21-38,485-731,1328256-1444696,11453498-11629572,41-66,2147-3014,714670445-714760965,531505304-531554460,4029-5268,3131222053-3131390224"

# puzzleInput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
inputArray = puzzleInput.split(",")
nestedInput = [list(map(int, pair.split("-"))) for pair in inputArray]

print(nestedInput)


def invalid_ids(range_list):
    invalid_sum = 0
    for pair in range_list:
        start, end = pair
        for number in range(start, end + 1):
            amount_of_repeats = 2
            while amount_of_repeats <= len(str(end)):
                if len(str(number)) % amount_of_repeats == 0:
                    wrapper = textwrap.TextWrapper(width=len(str(number)) // amount_of_repeats)
                    chunks = wrapper.wrap(str(number))
                    amount_of_repeats += 1
                    if len(set(chunks)) == 1:
                        invalid_sum += number
                        break
                else:
                    amount_of_repeats += 1
                    continue
    return invalid_sum

print(invalid_ids(nestedInput))
