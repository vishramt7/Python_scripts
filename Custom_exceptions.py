class ConnectionError(Exception):
    pass

try:
    raise ConnectionError("Cannot connect .. its time to panic")

except ConnectionError as err:
    print ("Got:", str(err))
