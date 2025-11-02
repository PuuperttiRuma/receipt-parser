import sys
import re

# Checks if str is a date


def is_date(test_str):
    patterns = [
        r"^\d{2}\.\d{2}\.\d{4}$",  # dd.mm.yyyy
    ]
    for pattern in patterns:
        if re.match(pattern, test_str):
            return True
    return False


def get_date(line):
    words = line.split()
    for str in words:
        if is_date(str):
            return str
    return None


def parse_transaction(line):
    words = line.split("    ")
    item = words[0]
    price = words[-1]

    return item.strip("* "), price.strip("* ")


def main():
    filename = sys.argv[1]

    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line in ["\n", "\r\n", ""]:
                continue
            lines.append(line)

    new_lines = []

    is_collecting = False
    date = ""

    for line in lines:
        line_date = get_date(line)
        if line_date:
            date = line_date
        elif line == "------------------------------------------":
            is_collecting = not is_collecting
        elif is_collecting:
            item, price = parse_transaction(line)
            new_lines.append(f"{date};{item};{price}")

    print(new_lines)


if __name__ == "__main__":
    main()
