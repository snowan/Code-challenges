Code challenge [build your own wc](https://codingchallenges.fyi/challenges/challenge-wc/)

#### How to use command
1. print number of lines of given file, `python wc.py -l <file_path>` example `python wc.py -l test.tx`
```
python3 build-wc/wc.py -l Tests/test.txt
Lines: 7145, file path: Tests/test.txt
```
2. print number of words of given file, `python wc.py. -w <file_path>`
```
python3 build-wc/wc.py -w Tests/test.txt
Words: 58164, file path: Tests/test.txt
```
3. print number of bytes (characters) of given file `python wc.py -c <file_path>`
```
python3 build-wc/wc.py -c Tests/test.txt
Characters: 342190, file path: Tests/test.txt
```
4. check whether current locale support multibyte, print number of bytes of given file 
    - if yes, use `-m`, `python wc.py -m <file_path>`, 
    - else default to `-c`
```
python3 build-wc/wc.py -m Tests/test.txt
Characters: 342190, file path: Tests/test.txt
```
5. if no option from arg, default to print all `python wc.py <file_path>`
```
python3 build-wc/wc.py Tests/test.txt
Lines: 7145, Words: 58164, Characters: 342190 file path: Tests/test.txt
```