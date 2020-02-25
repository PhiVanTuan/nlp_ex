
import numpy as np
import nltk
import os

from lstm.SentimentLSTM import SentimentLSTM

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="1,2"
import torch

from torchtext import datasets
from torch.utils.data import DataLoader, TensorDataset
from torch import nn
from string import punctuation
from collections import Counter

from lstm.SentimentalLSTM import SentimentalLSTM

path_test_p = '/home/phivantuan/Downloads/aclImdb_v1/aclImdb/test/pos/'
path_test_n = '/home/phivantuan/Downloads/aclImdb_v1/aclImdb/test/neg/'
###############################################################################
#######################  1. LOAD THE TRAINING TEXT  ###########################
###############################################################################
with open("reviews.txt") as f:
    reviews = f.read()

with open("labels.txt") as f:
    labels = f.read()


def preprocess(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in punctuation])
    all_reviews = text.split("\n")
    text = "".join(text)

    all_words = text.split()

    return all_reviews, all_words


all_reviews, all_words = preprocess(reviews)
###############################################################################
##################  3. CREATE DICTIONARIES & ENCODE REVIEWS  ##################
###############################################################################

# print(all_words)
word_counts = Counter(all_words)
total_words = len(all_words)
word_list = word_counts.most_common(total_words)
vocab_to_int = {word: idx + 1 for idx, word in enumerate(word_list)}
# int_to_vocab = {idx:word for word, idx in vocab_to_int.items()}
def pad_text(encoded_reviews, seq_length):
    reviews = []

    for review in encoded_reviews:
        if len(review) >= seq_length:
            reviews.append(review[:seq_length])
        else:
            reviews.append([0] * (seq_length - len(review)) + review)

    return np.array(reviews)


encoded_reviews = list()
for review in all_reviews:
    encoded_review = list()
    for word in review.split():
        if word not in vocab_to_int.keys():
            # if word is not available in vocab_to_int put 0 in that place
            encoded_review.append(0)
        else:
            encoded_review.append(vocab_to_int[word])
    encoded_reviews.append(encoded_review)
sequence_length=200
features=np.zeros((len(encoded_reviews), sequence_length), dtype=int)
for i, review in enumerate(encoded_reviews):
  review_len=len(review)
  if (review_len<=sequence_length):
    zeros=list(np.zeros(sequence_length-review_len))
    new=zeros+review
  else:
    new=review[:sequence_length]
features[i,:]=np.array(new)
labels=[1 if label.strip()=='positive' else 0 for label in labels.splitlines()]


train_x=features[:int(0.8*len(features))]
train_y=labels[:int(0.8*len(features))]
valid_x=features[int(0.8*len(features)):int(0.9*len(features))]
valid_y=labels[int(0.8*len(features)):int(0.9*len(features))]
test_x=features[int(0.9*len(features)):]
test_y=labels[int(0.9*len(features)):]
# print(train_x)

#create Tensor Dataset
train_data=TensorDataset(torch.FloatTensor(train_x), torch.FloatTensor(train_y))
valid_data=TensorDataset(torch.FloatTensor(valid_x), torch.FloatTensor(valid_y))
# test_data=TensorDataset(torch.FloatTensor(test_x), torch.FloatTensor(test_y))

#dataloader
batch_size=50
train_loader=DataLoader(train_data, batch_size=batch_size, shuffle=True)
valid_loader=DataLoader(valid_data, batch_size=batch_size, shuffle=True)
# test_loader=DataLoader(test_data, batch_size=batch_size, shuffle=True)

###############################################################################
################  9. INSTANTIATE THE MODEL W/ HYPERPARAMETERS #################
###############################################################################
vocab_size = len(vocab_to_int)
print(vocab_size)
output_size = 1
embedding_dim = 512
hidden_dim = 256
n_layers = 2

net = SentimentLSTM(vocab_size, output_size, embedding_dim, hidden_dim, n_layers)
print(net)
from torch import optim

criterion = nn.BCELoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)

###############################################################################
##########################  11. TRAIN THE NETWORK!  ###########################
###############################################################################
lr=0.001



# check if CUDA is available
train_on_gpu = torch.cuda.is_available()

# training params

epochs = 3 # 3-4 is approx where I noticed the validation loss stop decreasing

counter = 0
print_every = 100
clip=5 # gradient clipping

# move model to GPU, if available
if(train_on_gpu):
    net.cuda()

net.train()
# train for some number of epochs
for e in range(epochs):
    # initialize hidden state
    h = net.init_hidden(batch_size)

    # batch loop
    for inputs, labels in train_loader:
        counter += 1

        if(train_on_gpu):
            inputs=inputs.cuda()
            labels=labels.cuda()
        # Creating new variables for the hidden state, otherwise
        # we'd backprop through the entire training history
        h = tuple([each.data for each in h])

        # zero accumulated gradients
        net.zero_grad()

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

                inputs, labels = inputs.cuda(), labels.cuda()
                output, val_h = net(inputs, val_h)
                val_loss = criterion(output.squeeze(), labels.float())

                val_losses.append(val_loss.item())

            net.train()
            print("Epoch: {}/{}...".format(e+1, epochs),
                  "Step: {}...".format(counter),
                  "Loss: {:.6f}...".format(loss.item()),
                  "Val Loss: {:.6f}".format(np.mean(val_losses)))


def predict(net, review, seq_length=200):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    words = preprocess(review)
    encoded_words = [vocab_to_int[word] for word in words]
    padded_words = pad_text([encoded_words], seq_length)
    padded_words = torch.from_numpy(padded_words).to(device)

    if (len(padded_words) == 0):
        "Your review must contain at least 1 word!"
        return None

    net.eval()
    h = net.init_hidden(1)
    output, h = net(padded_words, h)
    pred = torch.round(output.squeeze())
    msg = "This is a positive review." if pred == 0 else "This is a negative review."

    return msg
review1 = "It made me cry."
review2 = "It was so good it made me cry."
review3 = "It's ok."
review4 = "This movie had the best acting and the dialogue was so good. I loved it."
review5 = "Garbage"
                       ### OUTPUT ###
predict(net, review1)  ## negative ##
predict(net, review2)  ## positive ##
predict(net, review3)  ## negative ##
predict(net, review4)  ## positive ##
predict(net, review5)  ## negative ##