import os
import pickle


def load_yoochoose():

    data_dir = "./data/yoochoose1_64"

    all_train_seq_file = "/all_train_seq.txt"
    train_file = "/train.txt"
    test_file = "/test.txt"

    with open(data_dir + all_train_seq_file, "rb") as f:
        all_train_seq = pickle.load(f)

    with open(data_dir + train_file, "rb") as f:
        train = pickle.load(f)

    with open(data_dir + test_file, "rb") as f:
        test = pickle.load(f)

    return all_train_seq, train, test

