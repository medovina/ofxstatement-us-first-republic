ofxstatement-us-first-republic
========================

This is an [ofxstatement](https://github.com/kedder/ofxstatement) plugin that can generate OFX files from CSV files exported by [First Republic Bank](https://www.firstrepublic.com).

First Republic can actually export .QFX files directly, but unfortunately these  QFX files have NAME and MEMO fields that look like this:

```
<NAME>DEBIT CARD #8248 01/02 HLU*HULU</NAME>
<MEMO>DEBIT CARD #8248 01/02 HLU*HULU 6062540 HULU.COM/BILLC</MEMO>
```

Those fields are ugly because they combine the payee, date, card number and other information into a single string.  You probably don't want to see information in this form in your accounting program.

Alternatively you can export a CSV file from First Republic Bank, then use this plugin to convert it
to an OFX file.  In this OFX file the payee names will be much easier to read:

```
<NAME>Hulu</NAME>
```

To install this plugin, download or clone the sources and run

```
$ python3 setup.py install
```

To download a CSV file from First Republic,
go to their [online banking site](https://www.firstrepublic.com/bankingonline) and log in.
On the Account Activity page, click the Filter tab, select a date range, and click Apply.
Then click the Export link above the transaction listing and choose CSV.

To convert to an OFX file, run

```
$ ofxstatement convert -t first_republic transactions.csv statement.ofx
```
