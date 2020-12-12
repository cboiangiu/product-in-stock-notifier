from expressvpn import connect_alias, disconnect

def reconnect(country_code):
    disconnect()
    connect_alias(alias=country_code)

def connect(country_code):
    connect_alias(alias=country_code)
