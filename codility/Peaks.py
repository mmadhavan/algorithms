# -*- coding: utf-8 -*-


class Peaks(object):

    """
    A non-empty array A consisting of N integers is given.

    A peak is an array element which is larger than its neighbours. More
    precisely, it is an index P such that
    0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

    For example, the following array A:

        A[0] = 1
        A[1] = 5
        A[2] = 3
        A[3] = 4
        A[4] = 3
        A[5] = 4
        A[6] = 1
        A[7] = 2
        A[8] = 3
        A[9] = 4
        A[10] = 6
        A[11] = 2

    has exactly four peaks: elements 1, 3, 5 and 10.

    You are going on a trip to a range of mountains whose relative heights are
    represented by array A, as shown in a figure below. You have to choose how
    many flags you should take with you. The goal is to set the maximum number
    of flags on the peaks, according to certain rules.


    Flags can only be set on peaks. What's more, if you take K flags, then the
    distance between any two flags should be greater than or equal to K. The
    distance between indices P and Q is the absolute value |P − Q|.

    For example, given the mountain range represented by array A, above, with
    N = 12, if you take:

    two flags, you can set them on peaks 1 and 5;
    three flags, you can set them on peaks 1, 5 and 10;
    four flags, you can set only three flags, on peaks 1, 5 and 10.
    You can therefore set a maximum of three flags in this case.

    Write a function:

    def solution(A)

    that, given a non-empty array A of N integers, returns the maximum number
    of flags that can be set on the peaks of the array.

    For example, the following array A:

        A[0] = 1
        A[1] = 5
        A[2] = 3
        A[3] = 4
        A[4] = 3
        A[5] = 4
        A[6] = 1
        A[7] = 2
        A[8] = 3
        A[9] = 4
        A[10] = 6
        A[11] = 2
    the function should return 3, as explained above.

    Assume that:

    N is an integer within the range [1..400,000];
    each element of array A is an integer within the range [0..1,000,000,000].
    Complexity:

    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(N) (not counting the storage
    required for input arguments).

    Note: Its important to take a peaks scan and store it in an boolean array,
    because if we take k flags we have to maintain k distance between two flags
    and we can find that by peaks[i] + k

    """

    @staticmethod
    def solution(A):
        # write your code in Python 3.6
        peaks = [0] * len(A)
        peak_count = 0

        if len(A) == 1:
            return 0

        for i, v in enumerate(A):
            if 0 < i < len(A) - 1:
                if A[i - 1] < A[i] > A[i + 1]:
                    peaks[i] = 1
                    peak_count += 1

        if peak_count:
            # Try for all possible flag count and return
            # if we can place all flags
            for flags in range(peak_count, 0, -1):
                k = 1
                no_of_flags = flags
                while no_of_flags and k < len(peaks):
                    if peaks[k]:
                        k += flags
                        no_of_flags -= 1
                    else:
                        k += 1

                # Just return the maximum number of flags
                if no_of_flags == 0:
                    return flags

        else:
            return 0


if __name__ == '__main__':
    p = Peaks()
    A = [0] * 12
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
    print p.solution(A)
