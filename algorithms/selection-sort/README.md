# Selection Sort

Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. If user wants to sort dictionary based on First Key 'A', Then Key 'B', they shall pass list of keys in the order of preference as a list ['A','B']. Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference

Example:
A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.

for this, one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]

For this, Given the following sequence List:

```
[
    {'First Name': 'Saif', 'Last Name': 'Nayeem'},
    {'First Name': 'Sayeed', 'Last Name': 'Ahmed'},
    {'First Name': 'Amin', 'Last Name': 'Mahmud'},
    {'First Name': 'Shobuj', 'Last Name': 'Hasan'},
    {'First Name': 'Rafi', 'Last Name': 'Talukdar'},
    {'First Name': 'Emon', 'Last Name': 'Khan'},
    {'First Name': 'Adnan', 'Last Name': 'Ahmed'},
    {'First Name': 'Mustafa', 'Last Name': 'Chowdhury'},
    {'First Name': 'Rafiq', 'Last Name': 'Hossain'},
    {'First Name': 'Jahid', 'Last Name': 'Bhuiyan'},
    {'First Name': 'Labib', 'Last Name': 'Abdullah'},
    {'First Name': 'Jahid', 'Last Name': 'Hassan'},
    {'First Name': 'Saif', 'Last Name': 'Ahmed'},
    {'First Name': 'Rafi', 'Last Name': 'Majumdar'},
]
```

Your algorithm should generate sorted list:

```
[
    {'First Name': 'Adnan', 'Last Name': 'Ahmed'},
    {'First Name': 'Amin', 'Last Name': 'Mahmud'},
    {'First Name': 'Emon', 'Last Name': 'Khan'},
    {'First Name': 'Jahid', 'Last Name': 'Bhuiyan'},
    {'First Name': 'Jahid', 'Last Name': 'Hassan'},
    {'First Name': 'Labib', 'Last Name': 'Abdullah'},
    {'First Name': 'Mustafa', 'Last Name': 'Chowdhury'},
    {'First Name': 'Rafi', 'Last Name': 'Majumdar'},
    {'First Name': 'Rafi', 'Last Name': 'Talukdar'},
    {'First Name': 'Rafiq', 'Last Name': 'Hossain'},
    {'First Name': 'Saif', 'Last Name': 'Ahmed'},
    {'First Name': 'Saif', 'Last Name': 'Nayeem'},
    {'First Name': 'Sayeed', 'Last Name': 'Ahmed'},
    {'First Name': 'Shobuj', 'Last Name': 'Hasan'},
]
```
