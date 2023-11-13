## Python Program made to count most frequently used words in .txt file.

Takes .txt file and return list of most often occurring words.

- `url` ********\********* url to the .txt file
- `textEncoding` **\*\*** type of character encoding, by default utf-8
- `minWordLength` **\*** minimal length of a word, by default 0
- `maxWordLength` **\*** maximal length of a word, by default 99
- `numOfEntities` **\*** how many words you want to return, by default 10
- `inConsole`
  if True, returns curated for console version of output
  if False, returns list of key-value pairs

## Example

### For the book "Fight Club" written by Chuck Palahniuk command:

`print(wordCounter(url=url, minWordLength=3, numOfEntities=10, inConsole=True))`

### will print into console:

```
 Tyler            appears  539 times
 with             appears  335 times
 Marla            appears  253 times
 your             appears  231 times
 that             appears  214 times
 have             appears  196 times
 fight            appears  195 times
 says,            appears  170 times
 this             appears  166 times
 This             appears  143 times
```

### for command

`print(wordCounter(url=url, minWordLength=3, numOfEntities=10, inConsole=False))`

### will return:

```
[['Tyler', 539], ['with', 335], ['Marla', 253], ['your', 231], ['that', 214], ['have', 196], ['fight', 195], ['says,', 170], ['this', 166], ['This', 143]]
```
