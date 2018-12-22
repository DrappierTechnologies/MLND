# Machine Learning Engineer Nanodegree

## Capstone Project

### Setup

#### This setup is for a Windows Python 3 environment.

You will need multiple libraries to run this notebook, namely:
* numpy
* pandas
* torch
* nltk
* zipfile
* fasttext
* plotly
* pathlib
* InferSent (included as a submodule)
* sklearn

```
pip install numpy pandas torch zipfile fasttext plotly pathlib sklearn nltk
```

Running in a Windows Python 3 environment there is an issue with the InferSent library that requires two minor code changes. I could not include the fix as part of the submodule so this will have to be manually performed in order to get it working.

### IMPORTANT NOTE: THIS CODE CHANGE MAY NOT BE NECESSARY IN A LINUX PYTHON 3 ENVIRONMENT BUT I CANNOT CONFIRM THIS SINCE I HAVE NOT TESTED IT.

  * Open the InferSent local repo in your editor of choice
  * Open the `models.py` file
  * Change these:
  ```
     def get_w2v(self, word_dict):
        assert hasattr(self, 'w2v_path'), 'w2v path not set'
        # create word_vec with w2v vectors
        word_vec = {}
        with open(self.w2v_path) as f:
  ```
  ```
      def get_w2v_k(self, K):
        assert hasattr(self, 'w2v_path'), 'w2v path not set'
        # create word_vec with k first w2v vectors
        k = 0
        word_vec = {}
        with open(self.w2v_path) as f:
  ```
  * To this:
  ```
      def get_w2v(self, word_dict):
        assert hasattr(self, 'w2v_path'), 'w2v path not set'
        # create word_vec with w2v vectors
        word_vec = {}
        with open(self.w2v_path, encoding="utf-8") as f:
  ```
  ```
      def get_w2v_k(self, K):
        assert hasattr(self, 'w2v_path'), 'w2v path not set'
        # create word_vec with k first w2v vectors
        k = 0
        word_vec = {}
        with open(self.w2v_path, encoding="utf-8") as f:
  ```
## Prepping Datasets & Models

In cell 2 and 3 there are commands to download and extract the dataset and model files needed for fastText and InferSent. If for any reason these do not function as expected please follow these steps to achieve the same result manually.

* In the "project" folder create a new folder named "fastText"
* Download the dataset from https://s3-us-west-1.amazonaws.com/fasttext-vectors/crawl-300d-2M.vec.zip (THIS WILL TAKE A WHILE)
* Extract `crawl-300d-2M.vec.zip` into the "fastText" folder you created earlier
* In the "project" folder create a new folder named "encoder"
* Download the pretrained model from https://s3.amazonaws.com/senteval/infersent/infersent2.pkl
* Place the `infersent2.pkl` file in the "encoder" folder you created earlier

## Now You're Ready To Roll
