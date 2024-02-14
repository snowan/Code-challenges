### build json parser 

[build json parser](https://codingchallenges.fyi/challenges/challenge-json-parser/)

1. validate whether it is valid json 
`python3 json-parser.py -v test.json` 
```
# test invalid json
python3 json-parser/json-parser.py -v Tests/json_parser_tests/step1/invalid.json
Invalid JSON: string index out of range

# test valid json
python3 json-parser/json-parser.py -v Tests/json_parser_tests/step1/valid.json 
Valid JSON
```
2. valid key values
```
# Test valid json
python3 json_parser/json_parser.py -v Tests/json_parser_tests/step2/valid2.json
Key: key, Value: value
Key: key2, Value: value
Valid JSON

python3 json_parser/json_parser.py -v Tests/json_parser_tests/step2/valid.json 
Key: key, Value: value
Valid JSON

# test invalid json
python3 json_parser/json_parser.py -v Tests/json_parser_tests/step2/invalid.json
ValueError: Invalid JSON: Expecting property name enclosed in double quotes: line 1 column 17 (char 16)

python3 json_parser/json_parser.py -v Tests/json_parser_tests/step2/invalid2.json
ValueError: Invalid JSON: Expecting property name enclosed in double quotes: line 3 column 3 (char 22)
```
3.

#### How to Run unit test 

```
python3 -m unittest json_parser/json-parser-test.py
Invalid JSON: string index out of range
.Valid JSON
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
