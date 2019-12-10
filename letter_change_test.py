import pandas as pd
import pytest

def process(x):
    if ord(x) in range(97, 122):
        return chr(ord(x) + 1)
    elif x == 'z':
        return 'a'
    else:
        return x

def letter_change(input):
    return pd.Series(list(input.lower())).apply(process).apply(lambda x: x.upper() if x in ['a','e', 'i','o','u'] else x).str.cat()


testdata = [
    ('z','A'),
    ('yz','zA'),
    ('hello*3', 'Ifmmp*3'),
    ('fun times!', 'gvO Ujnft!')
]


@pytest.mark.parametrize("input, output", testdata)
def test_airline_clean_process(input, output):
    assert letter_change(input)==output

    #
    # wordcloud_model.tfidf_generator(
    #     "/Users/peter/PycharmProjects/de-adapt/batch_processing/input_with_all_stop_word_in_one_tweet.csv",
    #     "/Users/peter/PycharmProjects/de-adapt/batch_processing/output.csv",
    #     "/Users/peter/PycharmProjects/de-wordcloud/output.png",
    #     hide_list=[],
    #     num_words=50,
    #     wordcloud_params=None,
    # )
