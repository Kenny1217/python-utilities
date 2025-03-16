import hvac

class HashicorpVaultConnector:
    def __init__(self, vault_addr, vault_token):
        self.client = hvac.Client(url=vault_addr, token=vault_token)
    
    

