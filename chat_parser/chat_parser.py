import re
from typing import List

MENTION_DELIMITER = ' : '
DATE_MAX_INDEX = 8
CUSTOMER_TYPE = 'customer'
AGENT_TYPE = 'agent'
DATE_REG_EX = r'\d{1,2}:\d{1,2}:\d{1,2}'
AGENTS = ['Emanuele Querzola', 'Agent']


def is_agent(mention: str) -> bool:
    return any([agent in mention for agent in AGENTS])


def get_type(mention: str) -> str:
    return AGENT_TYPE if is_agent(mention) else CUSTOMER_TYPE


def parse_line(line: str) -> dict:
    date = line[:DATE_MAX_INDEX]
    mention = f'{line.split(MENTION_DELIMITER)[0]}' \
              f'{MENTION_DELIMITER}'
    sentence = line.split(MENTION_DELIMITER)[1]
    the_type = get_type(mention)
    return {
        'date': date,
        'mention': mention,
        'sentence': sentence,
        'type': the_type
    }


def remove_invalid_dates_indexes(dates_indexes, chat):
    valid_dates_indexes = []
    for date_index in dates_indexes:
        if date_index == 0:
            valid_dates_indexes.append(date_index)
        elif chat[date_index - 1] != ' ':
            valid_dates_indexes.append(date_index)
    return valid_dates_indexes


def split_chat(chat: str) -> List[str]:
    dates = re.findall(DATE_REG_EX, chat)
    dates_indexes = [chat.index(date) for date in dates]
    dates_indexes = remove_invalid_dates_indexes(dates_indexes, chat)
    dates_indexes_intervals = dates_indexes + [len(chat)]
    if len(dates_indexes_intervals) == 2:
        return [chat]
    lines_indexes = get_list_indexes(dates_indexes_intervals)
    my_list = [chat[start:end] for start, end in lines_indexes]
    return my_list


def get_list_indexes(dates_indexes):
    window_size = 2
    lines_indexes = [
        dates_indexes[i: i + window_size]
        for i in range(len(dates_indexes) - window_size + 1)
    ]
    return lines_indexes


class ChatParser:

    @classmethod
    def parse_chat(cls, chat: str) -> List[dict]:
        chat_lines = split_chat(chat)
        return [parse_line(line) for line in chat_lines]
