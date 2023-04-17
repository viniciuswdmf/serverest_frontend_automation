import re
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

# Available in the API tab of a server
api_key = "z3GUmHzyc4Y78OMF"
server_id = "zlp5m1hh"
server_domain = "zlp5m1hh.mailosaur.net"

mailosaur = MailosaurClient(api_key)

criteria = SearchCriteria()
criteria.sent_to = "case-dress@" + server_domain

email = mailosaur.messages.get(server_id, criteria)
#print(email.text.body)

match = re.search("([0-9]{4}[a-z]{2}[0-9]{3})", email.text.body)
print(match.group())
