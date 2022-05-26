from tinkoff.invest import Client

FIGI = 'FUTSBRF06220'

MOVE_PERCENT = 1

MODE = [
    'wait',
    'open order',
    'close order',
    'delete order',
]

with open('sec_token.data', mode='r') as fl:
    TOKEN = fl.read()

with open('sec_account_number.data', mode='r') as fl:
    ACCOUNT = fl.read()


def main():
    with Client(token=TOKEN) as client:
        pass

        # 1. получили текущие цены
        # 2. считаем аск и бид для входа по разнице в 1%
        # 3. ставим туда лимитник


if __name__ == '__main__':
    main()
