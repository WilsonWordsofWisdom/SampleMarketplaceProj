import pandas as pd
import pytest


def game(input):
    if input % 15==0:
        return 'fizzbuzz'
    elif input % 5==0:
        return 'buzz'
    elif input % 3==0:
        return 'fizz'
    else:
        return input

testdata = [
    (3, 'fizz'),
    (2, 2),
    (5, 'buzz'),
    (15, 'fizzbuzz'),
    (90, 'fizzbuzz'),
    (-5,'buzz'),
    (0,'fizzbuzz'),
]


@pytest.mark.parametrize("input, output", testdata)
def test_airline_clean_process(input, output):
    assert game(input)==output

    #
    # wordcloud_model.tfidf_generator(
    #     "/Users/peter/PycharmProjects/de-adapt/batch_processing/input_with_all_stop_word_in_one_tweet.csv",
    #     "/Users/peter/PycharmProjects/de-adapt/batch_processing/output.csv",
    #     "/Users/peter/PycharmProjects/de-wordcloud/output.png",
    #     hide_list=[],
    #     num_words=50,
    #     wordcloud_params=None,
    # )
