import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("-------------------------------")
    print("          journal App ")
    print("-------------------------------")


def run_event_loop():
    print("what do you want to do with your journal? ")
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    while cmd != 'x' and cmd:
        cmd = input("(L)ist Enteries, (A)dd an entry, E(x)it: ")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("sorry we dont understand '{}'".format(cmd))

    print('Done, goodbye')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your Journal Entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
