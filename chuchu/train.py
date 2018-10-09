def train_iter(idx: int):
    # assume this is computationally intensive
    # so we want to mock it
    return 0.1*idx


def train(iter_num: int):
    iter_losses = []
    for idx in range(iter_num):
        iter_losses.append(train_iter(idx))

    return iter_losses
