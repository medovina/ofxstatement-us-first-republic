import csv
from decimal import Decimal
from ofxstatement.parser import StatementParser
from ofxstatement.plugin import Plugin
from ofxstatement.statement import Statement, StatementLine

class FirstRepublicParser(StatementParser):
    date_format = '%m/%d/%Y'

    def __init__(self, filename):
        self.filename = filename

    def guess_type(self, description, amount):
        d = description.lower()
        if 'fee' in d: return 'FEE'
        if 'atm' in d: return 'ATM'
        if 'check' in d: return 'CHECK'
        if 'interest' in d: return 'INT'
           
        return 'CREDIT' if amount > 0 else 'DEBIT'

    def parse(self):
        statement = Statement(bank_id = '321081669', currency = 'USD')
        
        with open(self.filename) as f:
            for row in csv.DictReader(f):
                line = StatementLine(id = row['Transaction Number'],
                                        date = self.parse_datetime(row['Date']),
                                        memo = row['Statement Description'],
                                        amount = Decimal(row['Debit'] or row['Credit']))
                
                line.payee = row['Description']
                line.check_no = row['Check Number']
                line.trntype = self.guess_type(line.payee, line.amount)
                statement.lines.append(line)
                
        return statement

class FirstRepublicPlugin(Plugin):
    'First Republic Bank CSV'

    def get_parser(self, filename):
        return FirstRepublicParser(filename)
