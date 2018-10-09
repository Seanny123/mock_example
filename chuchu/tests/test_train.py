from chuchu.train import train


def simple_iter(idx):
    return idx


def test_train(mocker):
    mocker.patch("chuchu.train.train_iter", side_effect=simple_iter)
    res = train(2)
    assert res == [0, 1]
