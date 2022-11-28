import re,  csv
from bs4 import BeautifulSoup

#open the HTML file copied from the webpage
with open("page.html") as JACCTF:
  #create the bs4 object Jaja Asda Credit Card Transaction Processor
  JACCTP = BeautifulSoup(JACCTF, 'html5lib')

#setup the CSV file headers - this is in YNAB format
csvheaders = ['Date', 'Payee', 'Memo', 'Amount']

#init the list used for conversion output to CSV
alltransactionslist = []

#get each of the transaction lists (there is one for each date)
for adate in JACCTP.find_all(['app-transactions-list']):
  #filter out the pending transactions list as they have no date set yet
  if not adate.get('data-jaja-id') == 'pending-transactions-group':
    #for each transaction do -
    for atransaction in adate.find_all(['app-transaction-card']):
      #format the transaction date
      transaction_date = adate.get('data-jaja-id').replace('transactions-group-','')
      #extract the transaction title, i.e. for payee details
      transaction_title = atransaction.find("p", attrs={"data-jaja-id": "transaction-title"})
      #extract the transaction amount
      transaction_amount_tag = atransaction.find("div", attrs={"data-jaja-id": "transaction-amount"})
      #detect if this is a refund or payment transaction
      if 'repayment' in transaction_amount_tag.get('class'):
        #this is a refund transaction
        transaction_amount = float(transaction_amount_tag.string.replace('£',''))
      else:
        #this is a payment transaction
        transaction_amount = "-" + str(float(transaction_amount_tag.string.replace('£','')))
      #write the transaction data to a list item
      transactionlist = [transaction_date, transaction_title.string, '', transaction_amount]
      #save the transaction to the overall transaction list
      alltransactionslist.append(transactionlist)

#close the HTML file
JACCTF.close

#open an output CSV file for writing
with open("JACCTP-YNAB-output.csv", 'w') as CSVoutputfile:
  #create the CSV writer object and set all fields to be fully quoted
  write = csv.writer(CSVoutputfile, quoting=csv.QUOTE_ALL)
  #write the CSV file header
  write.writerow(csvheaders)
  #write the transactions to the file
  write.writerows(alltransactionslist)

#close the CSV file
CSVoutputfile.close
