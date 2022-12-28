from suds.client import Client
from suds import byte_str


def pochta():
    url = 'https://tracking.russianpost.ru/rtm34?wsdl'
    client = Client(url, headers={'Content-Type': 'application/soap+xml; charset=utf-8'})
    my_login = 'BIHKLqtAgNQnUk'
    my_password = 'LvHyKgiirbK7'
    barcode = input('Введите трек-номер посылки\n'
                    '>>> ')
    message = f"""<?xml version="1.0" encoding="UTF-8"?>
                        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:oper="http://russianpost.org/operationhistory" xmlns:data="http://russianpost.org/operationhistory/data" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
                        <soap:Header/>
                        <soap:Body>
                           <oper:getOperationHistory>
                              <data:OperationHistoryRequest>
                                 <data:Barcode> {barcode} </data:Barcode>  
                             <data:MessageType>0</data:MessageType>
                             <data:Language>RUS</data:Language>
                          </data:OperationHistoryRequest>
                          <data:AuthorizationHeader soapenv:mustUnderstand="1">
                             <data:login> {my_login} </data:login>
                             <data:password> {my_password} </data:password>
                          </data:AuthorizationHeader>
                       </oper:getOperationHistory>
                    </soap:Body>
                 </soap:Envelope>"""

    message = byte_str(message)
    result = client.service.getOperationHistory(__inject={'msg': message})

    for rec in result.historyRecord:
        print('Статистика для конкретной посылки:')
        print(
            str(rec.OperationParameters.OperDate) + ', ' + rec.AddressParameters.OperationAddress.Description + ', ' + rec.OperationParameters.OperAttr.Name)
        print()
