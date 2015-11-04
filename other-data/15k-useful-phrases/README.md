Fifteen Thousand Useful Phrases
====

This is a clean version of the following book from Project Gutenberg.

> "Fifteen Thousand Useful Phrases: A Practical Handbook Of 
> Pertinent Expressions, Striking Similes, Literary, Commercial, 
> Conversational, And Oratorical Terms, For The Embellishment Of 
> Speech And Literature, And The Improvement Of The Vocabulary Of 
> Those Persons Who Read, Write, And Speak English"

**Author**: Greenville Kleiser

**Retrieved from**: https://archive.org/details/fifteenthousandu18362gut

The raw text version of the corpus can be accessed with `python3`:


```python
import re
import urllib.request
link = 'https://ia801403.us.archive.org/3/items/fifteenthousandu18362gut/18362.txt'
response = urllib.request.urlopen(link)
text = response.read().decode()
print(text)
```
