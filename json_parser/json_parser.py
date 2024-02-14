import argparse
import sys
import json

class JSONParser:
    def __init__(self, input_str):
        self.input_str = input_str
        self.position = 0

    def parse(self):
        # print(f"input {self.input_str}, len {len(self.input_str)}")
        try:
            self.parse_object()
            print("Valid JSON")
            sys.exit(0)
        except Exception as e:
            print(f"Invalid JSON: {str(e)}")
            sys.exit(1)

    def parse_object(self):
        # print(f"11 next {self.peek_next_char()} postition {self.position}") 
        self.consume('{')
        self.parse_key_value_pairs()
        self.consume('}')
        self.check_end_of_input()
    
    def parse_key_value_pairs(self):
        if self.peek_next_char() == '}':
            # Empty object
            return
        else:
            while True:
                # print(f"next {self.peek_next_char()} postition {self.position}")
                self.parse_key_value_pair()
                if self.peek_next_char() == ',':
                    self.consume(',')
                elif self.peek_next_char() == '}':
                    break
                else:
                    raise ValueError(f"Expected ',' or '}}', found '{self.peek_next_char()}'")
    # Step 2
    # def parse_key_value_pair(self):
    #     key = self.parse_string()
    #     self.consume(':')
    #     value = self.parse_string()
    #     # You can handle the key-value pair as needed, for now, we just print them
    #     print(f"Key: {key}, Value: {value}")

    # def parse_string(self):
    #     self.consume('"')
    #     start_position = self.position
    #     while self.position < len(self.input_str) and self.input_str[self.position] != '"':
    #         self.position += 1
    #     if self.position == len(self.input_str):
    #         raise ValueError("Unterminated string")
    #     value = self.input_str[start_position:self.position]
    #     self.position += 1  # Consume the closing quote
    #     return value
    
    def parse_key_value_pair(self):
        key = self.parse_string()
        self.consume(':')
        value = self.parse_value()
        # You can handle the key-value pair as needed, for now, we just print them
        print(f"Key: {key}, Value: {value}")

    def parse_value(self):
        next_char = self.peek_next_char()
        if next_char == '"':
            return self.parse_string()
        elif next_char.isdigit() or (next_char == '-' and self.peek_next_char(1).isdigit()):
            return self.parse_number()
        elif next_char == 't' or next_char == 'f':
            return self.parse_boolean()
        elif next_char == 'n':
            return self.parse_null()
        else:
            raise ValueError(f"Invalid value starting with '{next_char}'")

    def parse_string(self):
        self.consume('"')
        start_position = self.position
        while self.position < len(self.input_str) and self.input_str[self.position] != '"':
            self.position += 1
        if self.position == len(self.input_str):
            raise ValueError("Unterminated string")
        value = self.input_str[start_position:self.position]
        self.position += 1  # Consume the closing quote
        return value

    def parse_number(self):
        start_position = self.position
        while self.position < len(self.input_str) and (self.input_str[self.position].isdigit() or self.input_str[self.position] == '.'):
            self.position += 1
        value = self.input_str[start_position:self.position]
        return float(value) if '.' in value else int(value)

    def parse_boolean(self):
        if self.input_str[self.position] == 't':
            self.consume('t')
            self.consume('r')
            self.consume('u')
            self.consume('e')
            return True
        elif self.input_str[self.position] == 'f':
            self.consume('f')
            self.consume('a')
            self.consume('l')
            self.consume('s')
            self.consume('e')
            return False
        else:
            raise ValueError(f"Invalid boolean value")

    def parse_null(self):
        self.consume('n')
        self.consume('u')
        self.consume('l')
        self.consume('l')
        return None

    def consume(self, expected_char):
        if self.position < len(self.input_str) and self.input_str[self.position] == expected_char:
            self.position += 1
        else:
            raise ValueError(f"Expected '{expected_char}', found '{self.input_str[self.position]}'")

    def check_end_of_input(self):
        if self.position < len(self.input_str):
            raise ValueError(f"Unexpected character '{self.input_str[self.position]}' after JSON object")
        
    def peek_next_char(self):
        if self.position < len(self.input_str):
            # print(f"peek next char {self.input_str[self.position]}")
            return self.input_str[self.position]
        else:
            return None

def trim_json(json_content):
    try:
        parsed_json = json.loads(json_content)
        trimmed_json = json.dumps(parsed_json, separators=(',', ':'))
        return trimmed_json
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {str(e)}")
    
def main():
    parser = argparse.ArgumentParser(description="JSON Parser")
    parser.add_argument("filename", help="Path to the JSON file")
    parser.add_argument("-v", "--validate", action="store_true", help="Validate JSON")

    args = parser.parse_args()

    with open(args.filename, "r") as file:
        json_content = file.read()
        trimmed_json = trim_json(json_content)

    if args.validate:
        json_parser = JSONParser(trimmed_json)
        json_parser.parse()

if __name__ == "__main__":
    main()
