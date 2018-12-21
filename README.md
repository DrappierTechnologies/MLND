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

The SNLI/MultiNLI datasets that fastText requires has already been included in both extracted and compressed formats and can be found in the fastText folder.(probably why the repo takes so long to pull down)

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
  * You're ready to roll
