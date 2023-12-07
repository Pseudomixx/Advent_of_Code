import re


# ---------------------------------------------------------------------
# Part 1:

def sum_card_values(input: str):

    cards = input.splitlines()

    sum_values = 0
    for card in cards:
        sum_values += get_card_value(card)

    return sum_values


def get_card_value(card):

    winning = get_winning_numbers(card)
    your_numbers = get_your_numbers(card)

    matches = 0
    for i in winning:
        if i in your_numbers:
            matches += 1

    if matches == 0:
        card_value = 0
    else:
        card_value = 1 * 2**(matches - 1)

    return card_value



def get_your_numbers(card: str):

    your_part = card.split("|")[1].strip()
    pattern = re.compile(r" *(\d+ *)")
    your_numbers = [int(i.strip()) for i in re.findall(pattern, your_part)]
    return your_numbers


def get_winning_numbers(card: str):

    wn_part = card.split("|")[0].split(": ")[1].strip()
    pattern = re.compile(r" *(\d+ *)")
    winning_numbers = [int(i.strip()) for i in re.findall(pattern, wn_part)]
    return winning_numbers


# ---------------------------------------------------------------------------
# Part 2:

def total_scratchcards(input: str):

    cards = input.splitlines()
    card_copies = [1 for card in cards]

    cards_processed = 0
    for index, card in enumerate(cards):
        matches = get_matches(card)
        while card_copies[index] > 0:
            for i in range(1, matches + 1):
                card_copies[index + i] += 1
            
            card_copies[index] -= 1
            cards_processed += 1
    
    return cards_processed


def get_matches(card):

    winning = get_winning_numbers(card)
    your_numbers = get_your_numbers(card)

    matches = 0
    for i in winning:
        if i in your_numbers:
            matches += 1
    
    return matches

# ------------------------------------------------------------------------

file = open("day_4_data.txt")
content = file.read()


print(sum_card_values(content)) # Part 1 result
print(total_scratchcards(content)) # Part 2 result

