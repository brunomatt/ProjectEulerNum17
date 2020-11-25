# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: DO NOT COUNT SPACES OR HYPHENS!!!!!
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
sum = 0
under_10_sum = 0
under_100_sum = 0
one_thousand = 11

under10_dict = {
    "one" : 3,
    "two" : 3,
    "three" : 5,
    "four" : 4,
    "five" : 4,
    "six" : 3,
    "seven" : 5,
    "eight" : 5,
    "nine" : 4
}
under20_dict = {
    "ten" : 3,
    "eleven" : 6,
    "twelve" : 6,
    "thirteen" : 8,
    "fourteen" : 8,
    "fifteen" : 7,
    "sixteen" : 7,
    "seventeen" : 9,
    "eighteen" : 8,
    "nineteen" : 8
}

ten_mults_dict = {
    "twenty" : 6,
    "thirty" : 6,
    "forty" : 5,
    "fifty" : 5,
    "sixty" : 5,
    "seventy" : 7,
    "eighty" : 6,
    "ninety" : 6
}

hundred_dict    = {
    "one hundred" : 10,
    "two hundred" : 10,
    "three hundred" : 12,
    "four hundred" : 11,
    "five hundred" : 11,
    "six hundred" : 10,
    "seven hundred" : 12,
    "eight hundred" : 12,
    "nine hundred" : 11
}

for key in under10_dict: # covers 1-9
    under_10_sum += under10_dict[key]
    under_100_sum += under10_dict[key]

for key in under20_dict: # covers 10-19
    under_100_sum += under20_dict[key]

for key in ten_mults_dict: # covers 20 - 99
    under_100_sum += ten_mults_dict[key] * 10 + under_10_sum

for key in hundred_dict: # covers 101- 199 , 201 - 299 , etc. 901 - 999
    sum += hundred_dict[key] * 100 + under_100_sum

sum += under_100_sum + one_thousand # covers 1-99 and 1000

and_total = 3 * 99 * 9 # three letters 99 times per hundred for nine hundreds

answer = sum + and_total

print(answer)