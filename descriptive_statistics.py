"""

File    : descriptive_statistics.py
History : 5-Oct-2021

This program accepts two arguments: a text file containing tab-separated columns, and the column to
parse. It then parses that column and returns several pieces of statistical data.
"""
import sys
import math


def read(file, column_to_parse):
    """
    Reads the file given as argument 1, parses, and looks at column specified in column_to_parse
    :param file: file given
    :param column_to_parse: column being parsed
    :return: list of numbers and total number of lines
    """
    numbers = []
    counter = 0
    with open(file, 'r') as infile:
        for line in infile:
            counter = counter + 1
            try:
                num = line.split("\t")[int(column_to_parse)]
                try:
                    if num != "NaN":
                        numbers.append(float(num))
                except ValueError as err:
                    print("Skipping line number {} : {}".format(counter, err))
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(column_to_parse, counter, file))
                sys.exit(1)
    try:
        1/len(numbers)
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(column_to_parse, file))
        sys.exit(1)
    return numbers, counter


def variance(nums, avg):
    """
    Calculates the variance of the dataset given in nums
    :param nums: list of numbers in dataset
    :param avg: already calculated average of dataset
    :return:
    """
    numer = []  # Just numerator
    for i in nums:
        dif_sqr = (i - avg) ** 2
        numer.append(dif_sqr)
    try:
        varia = float(sum(numer) / (len(numer) - 1))  # Named variable 'varia' to keep it distinct
    except ZeroDivisionError:
        varia = 0
    return varia


def median(nums):
    """
    For calculating median
    :param nums: list of valid numbers from dataset
    :return: median value in dataset
    """
    sort = sorted(nums)
    length = len(sort)
    if length % 2 == 0:
        upper = sort[length // 2]
        lower = sort[length // 2 - 1]
        media = (upper + lower) / 2
    else:
        media = sort[length // 2]
    return media


if __name__ == "__main__":
    ARG_COUNT = (len(sys.argv) - 1)
    if ARG_COUNT != 2:
        raise Exception("This script takes 2 arguments: the input file and the column to parse.")
    IN_FILE = sys.argv[1]
    COLUMN = sys.argv[2]
    OUTPUT = read(IN_FILE, COLUMN)
    OUTPUT_N = OUTPUT[0]
    COUNT = OUTPUT[1]
    AVERAGE = float(sum(OUTPUT_N) / len(OUTPUT_N))
    VAR = variance(OUTPUT_N, AVERAGE)
    STD_DEV = math.sqrt(VAR)
    MED = median(OUTPUT_N)
    print("    Column: {}\n\n".format(str(COLUMN)))
    print("\tCount     ={:>11.3f}".format(float(COUNT)))
    print("\tValidNum  ={:>11.3f}".format(float(len(OUTPUT_N))))
    print("\tAverage   ={:>11.3f}".format(AVERAGE))
    print("\tMaximum   ={:>11.3f}".format(float(max(OUTPUT_N))))
    print("\tMinimum   ={:>11.3f}".format(float(min(OUTPUT_N))))
    print("\tVariance  ={:>11.3f}".format(float(VAR)))
    print("\tStd Dev   ={:>11.3f}".format(float(STD_DEV)))
    print("\tMedian    ={:>11.3f}\n".format(float(MED)))
