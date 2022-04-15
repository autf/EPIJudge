from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    from functools import cache
    @cache
    def dp(i, tot):
        if tot < 0:
            return 0
        if tot == 0:
            return 1
        d = individual_play_scores[i]
        if i == 0:
            return tot % d == 0
        i -= 1
        return sum(dp(i, t) for t in range(tot, -1, -d))
    return dp(len(individual_play_scores)-1, final_score)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
