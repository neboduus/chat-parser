import re
from typing import List

MENTION_DELIMITER = ' : '
DATE_MAX_INDEX = 8
CUSTOMER_TYPE = 'customer'
AGENT_TYPE = 'agent'
DATE_REG_EX = r'\d{1,2}:\d{1,2}:\d{1,2}'


def is_customer(mention: str) -> bool:
    return 'Customer' in mention


def get_type(mention: str) -> str:
    return CUSTOMER_TYPE if is_customer(mention) else AGENT_TYPE


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


def split_chat(chat: str) -> List[str]:
    dates = re.findall(DATE_REG_EX, chat)
    dates_indexes = [chat.index(date) for date in dates] + [len(chat)]
    if len(dates_indexes) == 1:
        return [chat]
    window_size = 2
    lines_indexes = [
        dates_indexes[i: i + window_size]
        for i in range(len(dates_indexes) - window_size + 1)
    ]
    my_list = [chat[start:end] for start, end in lines_indexes]
    return my_list


class ChatParser:

    @classmethod
    def parse_chat(cls, chat: str) -> List[dict]:
        chat_lines = split_chat(chat)
        return [parse_line(line) for line in chat_lines]
