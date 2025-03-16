import hvac


class HashicorpVaultConnector:
    def __init__(self, vault_addr, vault_token):
        self.client = hvac.Client(url=vault_addr, token=vault_token)

    def is_user_authenticated(self):
        try:
            auth_status = self.client.is_authenticated()
            print(f"Client authentication status is: {auth_status}")
            return auth_status
        except Exception as e:
            print(f"An error occurred while checking authentication: {e}")
            return False
    
    def get_vault_status(self):
        try:
            vault_status = self.client.sys.read_health_status(method='GET')
            if vault_status:
                print(f"Vault status: {vault_status}")
                return vault_status
            else:
                print(f"Failed to retrieve Vault status: {vault_status}")
                return None
        except Exception as e:
            print(f"An error occurred while getting vault status: {e}")
            return None
    
    def read_vault_secret(self, mount_point, secret_path, secret_name):
        try:
            vault_secret = self.client.secrets.kv.v2.read_secret_version(mount_point=mount_point, path=secret_path)
            if vault_secret:
                secret_data = vault_secret.get('data', {}).get('data', {}).get(secret_name)
                if secret_data:
                    print(f"Secret retrieved")
                    return secret_data
                else:
                    print(f"No data found in the secret")
                    return None
            else:
                print(f"No secret found")
                return None
        except Exception as e:
            print(f"An error occurred while retrieving vault secret: {e}")
            return None

    def write_vault_secret(self, mount_point, secret_path, secret_data):
        try:
            self.client.secrets.kv.v2.create_or_update_secret(mount_point=mount_point, path=secret_path ,secret=secret_data )
            print("Secret added to vault")
            return True
        except Exception as e:
            print(f"An error occurred while writing secret to vault: {e}")
            return False
    
    def delete_vault_secret(self, mount_point, secret_path, secret_name):
        try:
            print()
        except Exception as e:
            print(f"An error occurred while deleting secret from vault: {e}")
            return False
