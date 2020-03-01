import os
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import re
from collections import Counter
from string import punctuation
import string
import numpy as np

from craw.lstm import SentimentRNN

files = []
# f = open('review.txt').read()
vocab_to_int = {}
vocab = Counter()


def pre_process_text(text):
    text = text.splitlines()
    text = [re.sub(r'\d+', ' ', s) for s in text]
    text = [re.sub(r'[^\w\s]', ' ', s) for s in text]
    text = [re.sub('\s+', ' ', s) for s in text]

    # print(len(text))
    review_split = [c.translate(str.maketrans(' ', ' ', string.punctuation)) for c in text]
    # print(len(review_split))
    all_text = "\n".join(review_split)
    out = open("review2.txt", "w")
    out.write(all_text)
    # print(all_text)
    # words = all_text.split()  # Count all the words using Counter Method
    # count_words = Counter(words)
    # sorted_words = count_words.most_common()
    # vocab_to_int = {}
    # i = 1
    # for pair in sorted_words:
    #     vocab_to_int.update({pair[0]: i})
    #     i += 1
    # ## use the dict to tokenize each review in reviews_split
    # ## store the tokenized reviews in reviews_ints
    # reviews_ints = []
    # for review in review_split:
    #     word_list = review.split()
    #     num_list = []
    #     for word in word_list:
    #         num_list.append(vocab_to_int[word])
    #     reviews_ints.append(num_list)
    # print('Unique words: ', len((vocab_to_int)))  # should ~ 74000+
    # print()
    #
    # # print tokens in first review
    # print('Tokenized review: \n', reviews_ints[:1])


def test():
    file = open("review2.txt").read()
    review_split = file.splitlines()
    all_text = " ".join(review_split)
    words = all_text.split()  # Count all the words using Counter Method
    count_words = Counter(words)
    sorted_words = count_words.most_common()

    i = 1
    for pair in sorted_words:
        vocab_to_int.update({pair[0]: i})
        i += 1
    # print(len(vocab_to_int))
    ## use the dict to tokenize each review in reviews_split
    ## store the tokenized reviews in reviews_ints
    reviews_ints = []
    for review in review_split:
        word_list = review.split()
        num_list = []
        for word in word_list:
            num_list.append(vocab_to_int[word])
        reviews_ints.append(num_list)
    return reviews_ints


def pad_features(reviews_ints, seq_length):
    features = []

    ## implement function
    for review in reviews_ints:
        if len(review) < seq_length:
            features.append(list(np.zeros(seq_length - len(review))) + review)
        elif len(review) > seq_length:
            features.append(review[:seq_length])
        else:
            features.append(review)

    features = np.asarray(features, dtype=int)
    return features


batch_size = 50


def pre_data():
    split_frac = 0.8
    features = pad_features(test(), 200)
    encoded_labels = [int(i) for i in open("label.txt").read().splitlines()]

    ## split data into training, validation, and test data (features and labels, x and y)
    train_x, remaining_x, train_y, remaining_y = train_test_split(features, encoded_labels, test_size=0.2)
    test_x, valid_x, test_y, valid_y = train_test_split(remaining_x, remaining_y, test_size=0.5)
    # print(train_x)
    train_data = TensorDataset(torch.as_tensor(np.array(train_x).astype('long')), torch.as_tensor(np.array(train_y).astype('long')))
    valid_data = TensorDataset(torch.LongTensor(valid_x), torch.LongTensor(valid_y))
    # dataloaders
    # make sure to SHUFFLE your data
    train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size,drop_last=True)
    valid_loader = DataLoader(valid_data, shuffle=True, batch_size=batch_size,drop_last=True)
    return train_loader, valid_loader


vocab_size = len(vocab_to_int) + 1
print("size "+str(vocab_size))
output_size = 1
embedding_dim = 200
hidden_dim = 256
n_layers = 2

net = SentimentRNN(37549, output_size, embedding_dim, hidden_dim, n_layers)
train_on_gpu = torch.cuda.is_available()


def train():
    lr = 0.001

    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)
    epochs = 4  # 3-4 is approx where I noticed the validation loss stop decreasing

    counter = 0
    print_every = 100
    clip = 5  # gradient clipping
    train_loader, valid_loader = pre_data()
    # move model to GPU, if available
    if (train_on_gpu):
        net.cuda()

    net.train()
    # train for some number of epochs
    for e in range(epochs):
        # initialize hidden state
        h = net.init_hidden(batch_size)

        # batch loop
        for inputs, labels in train_loader:
            counter += 1
            # print(counter)

            if (train_on_gpu):
                inputs, labels = inputs.cuda(), labels.cuda()

            # Creating new variables for the hidden state, otherwise
            # we'd backprop through the entire training history
            h = tuple([each.data for each in h])

            # zero accumulated gradients
            net.zero_grad()
            # print(inputs)
            # get the output from the model
            output, h = net(inputs, h)

            # calculate the loss and perform backprop
            loss = criterion(output.squeeze(), labels.float())
            loss.backward()
            # `clip_grad_norm` helps prevent the exploding gradient problem in RNNs / LSTMs.
            nn.utils.clip_grad_norm_(net.parameters(), clip)
            optimizer.step()

            # loss stats
            if counter % print_every == 0:
                # Get validation loss
                val_h = net.init_hidden(batch_size)
                val_losses = []
                net.eval()
                for inputs, labels in valid_loader:

                    # Creating new variables for the hidden state, otherwise
                    # we'd backprop through the entire training history
                    val_h = tuple([each.data for each in val_h])

                    if (train_on_gpu):
                        inputs, labels = inputs.cuda(), labels.cuda()

                    output, val_h = net(inputs, val_h)
                    val_loss = criterion(output.squeeze(), labels.float())

                    val_losses.append(val_loss.item())

                net.train()
                # print("Epoch: {}/{}...".format(e + 1, epochs),
                #       "Step: {}...".format(counter),
                #       "Loss: {:.6f}...".format(loss.item()),
                #       "Val Loss: {:.6f}".format(np.mean(val_losses)))


train()


def preprocess(review, vocab_to_int):
    review = review.lower()
    word_list = review.split()
    num_list = []
    # list of reviews
    # though it contains only one review as of now
    reviews_int = []
    for word in word_list:
        if word in vocab_to_int.keys():
            num_list.append(vocab_to_int[word])
    reviews_int.append(num_list)
    return reviews_int


def predict(net, test_review, sequence_length=200):
    ''' Prints out whether a give review is predicted to be
        positive or negative in sentiment, using a trained model.

        params:
        net - A trained net
        test_review - a review made of normal text and punctuation
        sequence_length - the padded length of a review
        '''
    # change the reviews to sequence of integers
    int_rev = preprocess(test_review, vocab_to_int)
    # pad the reviews as per the sequence length of the feature
    features = pad_features(int_rev, seq_length=200)

    # changing the features to PyTorch tensor
    features = torch.from_numpy(features)

    # pass the features to the model to get prediction
    net.eval()
    val_h = net.init_hidden(1)
    val_h = tuple([each.data for each in val_h])

    if (train_on_gpu):
        features = features.cuda()

    output, val_h = net(features, val_h)

    # rounding the output to nearest 0 or 1
    pred = torch.round(output)

    # mapping the numeric values to postive or negative

    # print custom response based on whether test_review is pos/neg
    print(pred.item())


test_review = 'Hàng tốt giao hàng nhanh chong và đóng gói cẩn thận'
predict(net, test_review)
print(test_review)
