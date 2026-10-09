def get_number_of_words(text: str):
   text = text
   all_words = text.split()
   return len(all_words)


def get_character_counts(text: str) -> dict[str, int]:
    character_counts = {}
    for character in text:
        character = character.lower()
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts


def sort_on(entry: tuple[str, int]) -> int:
    return entry[1]


def chars_dict_to_sorted_list(character_counts: dict[str, int]) -> list[tuple[str, int]]:
    character_list = []
    for character in character_counts:
        character_list.append((character, character_counts[character]))
    character_list_sorted = sorted(character_list, reverse=True, key=sort_on)
    return character_list_sorted
