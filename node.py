from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
import json

# requires python3, json-rpc, werkzeug:
# sudo apt-get install python3.6
# sudo pip install json-rpc
# sudo pip install werkzeug
# OR
# sudo pip3 install json-rpc
# sudo pip3 install werkzeug

@dispatcher.add_method
def getwalletinfo():
    print("getwalletinfo")
    data = {
		"walletname": "wallet.dat",
		"walletversion": 139900,
		"balance": 0.00000000,
		"unconfirmed_balance": 0.00000000,
		"immature_balance": 0.00000000,
		"txcount": 0,
		"keypoololdest": 1516914220,
		"keypoolsize": 999,
		"keypoolsize_hd_internal": 1000,
		"paytxfee": 0.00500000,
		"hdmasterkeyid": "2cf2b103e080329b017dd8c524498c9eee36d032"
    }
    return data

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 10905, application)