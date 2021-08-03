# Apple's Human Interface Guidelines Word Count

Ever wanted to read up on Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), but didn't have the time? It turns out the number of words found in those guidelines for iOS and macOS rival that found in a short novel! 📕

This repository contains [functions](./words.py) to count the number of words found in the Human Interface Guidelines for iOS, macOS, watchOS, tvOS, and the other miscellaneous sections of their guidelines that tend to cross those boundaries. It includes a [Jupyter Notebook](./counting_words.ipynb) to interact with the data and understand the number of hours it would take the average reader to get through the different sections of the guidelines.

It uses the Python package `beautifulsoup` to parse Apple's HTML and features a loading bar from the `tqdm` package.