# Jaja Asda Credit Card CSV Export

The Asda Credit Card (provided by Jaja) website does not provide a facility to export your transactions in any format other than a PDF statement. This makes it pretty useless if you use any financial application(s). Bad form Jaja & Asda.

https://asda.jaja.finance/asda/login

This simple Python script will extract the transactions from the webpage and save them as a CSV. Its messy and requires some technical know-how, as listed in the steps below.

1. Make sure you have the latest Python 3 installed on your system - see: https://docs.python-guide.org/starting/installation/
2. Install pip, the Python package manager if it is not already installed
3. Install Beautiful Soup 4 and html5lib using `pip3 install beautifulsoup4 html5lib` - see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
4. Download the .py file from this repo - https://github.com/BLBurgess/jaja-asda-creditcard-csv/blob/main/jaja-asda-creditcard-csv.py
5. Log onto the Asda Credit Card website here: https://asda.jaja.finance/asda/login
6. You should land on the **Activity | Transactions** page, scroll the page down to load all transactions fully
7. Open the developer tools pane - see how here: https://balsamiq.com/support/faqs/browserconsole/
8. Copy the **body** element to the clipboard
9. Save the contents of the clipboard to a file called **page.html** in the same directory as the .py file
10. Run the .py file - this will output a file called **JACCTP-YNAB-output.csv** which is a CSV formatted file of the transactions on your account. This uses the YNAB suggested format - https://support.youneedabudget.com/en_us/formatting-a-csv-file-an-overview-BJvczkuRq
