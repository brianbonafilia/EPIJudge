from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # TODO - you fill in here.
    results = [[1] + [0] * final_score for _ in individual_play_scores]
    for score_index, score in enumerate(individual_play_scores):
        for index in range(1, final_score + 1):
            without_this_play = results[score_index - 1][index] if score_index >= 1 else 0
            with_this_play = results[score_index][index - score] if index >= score else 0
            results[score_index][index] = without_this_play + with_this_play
    return results[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
