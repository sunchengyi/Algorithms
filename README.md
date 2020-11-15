# Algorithms
This repository is about some small algorithms implemented by me or my own understanding 
about some alorithms.

Now it includes the following files.

- k-means.py

    It implements a k-means class in Python with an interface similar to Scikit-Learn. 
    Two of the methods of the class are "fit()" and "predict()". And in "fit()", the 
    tatol distance is used as the metric to stop the iterations. Of course, the maximum
    number of iterations also plays its role.
    
- sort_merge.py

    It implements the algorithm of merge sort in Python. It includes two funcions, 
    'sort_merge_recursion()' and 'sort_mrege_iteration.py'. As indicated by their name,
    the two functions use the recursion and iteration, respectively. Some tests are done.
    And it was found that both of them have a similar performance and 
    'sort_merge_recursion()' is a little slower. Of course, they are much slower that the
    built-in sort method in Python.

- maths_behind_PCA_with_SVD.ipynb

    This is a Jupyther notebook to explain briefly why the singular value decomposition
    (SVD) can be used to implement the principal component analysis.

- Intuition about the RMSprop and Adam optimizations.ipynb  
Give my understanding about the two optimizations (uncompleted). 
