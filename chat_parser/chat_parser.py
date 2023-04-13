from typing import List

MENTION_SPLIT_CHARACTER = ' : '
DATE_MAX_INDEX = 8
CUSTOMER_TYPE = 'customer'
AGENT_TYPE = 'agent'


def is_customer(mention: str) -> bool:
    return 'Customer' in mention


def get_type(mention: str) -> str:
    return CUSTOMER_TYPE if is_customer(mention) else AGENT_TYPE


def parse_line(line: str) -> dict:
    date = line[:DATE_MAX_INDEX]
    mention = f'{line.split(MENTION_SPLIT_CHARACTER)[0]}' \
              f'{MENTION_SPLIT_CHARACTER}'
    sentence = line.split(MENTION_SPLIT_CHARACTER)[1]
    type = get_type(mention)
    return {
        'date': date,
        'mention': mention,
        'sentence': sentence,
        'type': type
    }


class ChatParser:

    @classmethod
    def parse_chat(cls, chat: str) -> List[dict]:
        return [parse_line(chat)]

