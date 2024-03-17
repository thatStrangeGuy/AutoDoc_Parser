# AutoDoc_Parser
[![PyPI version](https://badge.fury.io/py/docxtpl.svg)](https://badge.fury.io/py/docxtpl)
[![PyPI version](https://badge.fury.io/py/PySide6.svg)](https://badge.fury.io/py/PySide6)
## AutoDoc_Parser is my study program for parsing and automatically creating docx/xls files
### Functionality planned is next:


1. First page allows to read raw xls file 
with ID of products, parse it with sqlite
database dictionary into new, fully parsed
xls file with description of products
2. Second page is database editor, 
where you can edit dictionaries for parsing
3. Third page is word docx creator, where you can browse parsed xls file, jinja2 - style syntax document template, and parse info from xls into your template, creating automatic documents
    - Using the checkbox, you can choose, use every row in the xls file for each document, or use all xls file for render one document
    - When using all rows for single docx document, this allows you to render tables use for in cycles
4. Settings page allows you to configure database default connection
