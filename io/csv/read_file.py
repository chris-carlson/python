from cac.io.text.read_file import ReadFile as TextReadFile
from cac.consumer import Consumer


class ReadFile:

    def __init__(self, file_name):
        self._file = TextReadFile(file_name)
        self._rows = []

    def __iter__(self):
        for row in self._rows:
            yield row

    @property
    def rows(self):
        return self._rows

    def read_data(self):
        self._file.read_lines()
        for line in self._file.get_stripped_lines():
            row = []
            consumer = Consumer(line)
            while consumer.has_input():
                if consumer.starts_with('\"'):
                    consumer.consume_char('\"')
                    row.append(consumer.consume_to('\"'))
                    consumer.consume_char('\"')
                    if consumer.has_input() and consumer.peek() == ',':
                        consumer.consume_char(',')
                elif consumer.contains(','):
                    row.append(consumer.consume_to(','))
                    consumer.consume_char(',')
                else:
                    row.append(consumer.consume_to_end())
            self._rows.append(row)

    def get_row(self, num):
        if num >= len(self._rows):
            raise ValueError('The file does not have ' + str(num) + ' rows')
        return self._rows[num]

    def get_column(self, num):
        column = []
        for row in self._rows:
            if num >= len(row):
                raise ValueError('A row in the file does not have ' + str(num) + ' columns')
            column.append(row[num])
        return column

    def close(self):
        self._file.close()
