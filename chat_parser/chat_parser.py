from typing import List

MENTION_DELIMITER = ' : '
CHAT_LINE_DELIMITER = '\n'
DATE_MAX_INDEX = 8
CUSTOMER_TYPE = 'customer'
AGENT_TYPE = 'agent'


def is_customer(mention: str) -> bool:
    return 'Customer' in mention


def get_type(mention: str) -> str:
    return CUSTOMER_TYPE if is_customer(mention) else AGENT_TYPE


def parse_line(line: str) -> dict:
    date = line[:DATE_MAX_INDEX]
    mention = f'{line.split(MENTION_DELIMITER)[0]}' \
              f'{MENTION_DELIMITER}'
    sentence = line.split(MENTION_DELIMITER)[1]
    type = get_type(mention)
    return {
        'date': date,
        'mention': mention,
        'sentence': sentence,
        'type': type
    }


def split_chat(chat: str) -> List[str]:
    lines = chat.split(CHAT_LINE_DELIMITER)
    return [
        f'{line}{CHAT_LINE_DELIMITER}'
        if idx != len(lines) - 1 else line
        for idx, line in enumerate(lines)
    ]


class ChatParser:

    @classmethod
    def parse_chat(cls, chat: str) -> List[dict]:
        chat_lines = split_chat(chat)
        return [parse_line(line) for line in chat_lines]
