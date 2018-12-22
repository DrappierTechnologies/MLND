
# stop word removal function
def generate_stop_word_free_dataset(dataframe):
    df = dataframe.copy()
    # iterate over every column
    for column in df.columns:
        # convert column values into an array where each row is an element in the array
        sentences = df[column].tolist()
        # remove stop words
        if isinstance(sentences[0], str):
            stop_wordless_sentences = []
            for sentence in sentences:
                split_sentence = sentence.split()
                new_words = [word for word in split_sentence if word not in stopwords.words('english')]
                # reconstruct the sentence
                new_sentence = " ".join(new_words)
                stop_wordless_sentences.append(new_sentence)
            # recolumnize into dataframe
            df[column] = stop_wordless_sentences
    return(df)

def split_data(x_data, y_data, test_percent_size):
    return train_test_split(x_data, y_data, test_size=test_percent_size, random_state=42)

def convert_sentences_to_vector_mean(dataframe):
    df = dataframe.copy()
    # iterate over every column
    for column in dataframe.columns:
        # convert column values into a list where each row is an element in the list
        sentences = dataframe[column].tolist()
        sentence_vectors = infersent.encode(sentences)
        sentence_vector_means = np.mean(sentence_vectors, axis=1)
        df[column] = sentence_vector_means
    return df