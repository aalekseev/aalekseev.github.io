Title: Python: split list into chunks
Date: 2018-05-04T13:57:35+03:00
Summary: Today I found [30 sec. of python code](https://github.com/kriadmin/30-seconds-of-python-code "GitHub") repository, that claims that every snippet there can be easily understood and copy/pasted by new developers.

Today I found [30 sec. of python code](https://github.com/kriadmin/30-seconds-of-python-code "GitHub") repository, that claims that every snippet there can be easily understood and copy/pasted by new developers.

> This project contains plenty of useful snippets which can help beginners and newcomers quickly ramp-up on grasping python 3's syntax.

In which I strongly disagree. Take this example - a function to split list to an equal chunks

```python
from math import ceil

def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))
```

If I was reviewing this code, I definitely recommend refactoring it. In my opinion, it is not clear enough what is going on and more - confusing to a newbie, because division in Python 2 and Python 3 works differently.

How can we make it better? This is how I feel to rewrite it:

```python
from __future__ import division
from math import ceil

def chunk(items, size):
    # ceil returns float and range don't like it
    stop = int(ceil(len(items) / size))
    return [
        items[slice(i * size, i * size + size)]
        for i in range(0, stop)
    ]

chunk([1, 2, 3], 2)  # [[1, 2], [3]]
```

As a bonus, the same concept in JavaScript (yes, I know that original repository was about JavaScript all along). Sometimes I feel like switching languages clears the mind.

```javascript
const range = function(n) {
    return Array.from(n).keys()
};

const chunk = function(items, size) {
    const stop = Math.ceil(items.length / size);
    return range(stop).map(function(i) {
        return list.slice(i * size, i * size + size)
    })
};

chunk([1, 2, 3], 2)  // [[1, 2], [3]]
```
