import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential, EnvironmentCredential

#os.environ['AZURE_SUBSCRIPTION_ID'] = '886ee2a4-e790-43c5-bfa4-5c8db2e433f6'
#os.environ['AZURE_TENANT_ID'] = '715d2561-2f89-4446-bbc9-6daacf798724'
#os.environ['AZURE_CLIENT_ID'] = '306f2689-10dc-4c03-84af-f3bcba42e5c7'
#os.environ['AZURE_CLIENT_SECRET'] = ''


def main():
    akv_url = 'https://testslkv.vault.azure.net'
    credential = DefaultAzureCredential()
    print("Pass Default credential configuration")
    #print out the token value used to access the keyvault
    try:
        tokenValue = credential.credentials[1].get_token('https://vault.azure.net/.default')
    except Exception as ex:
        print("Failed to get token: " + ex)
    else:
        print(tokenValue)
    print("Pass tokenValue")

    secret = 'secret1'
    client = SecretClient(vault_url=akv_url, credential=credential)
    try:
        KEY = client.get_secret(secret).value
    except Exception as ex:
        print("Failed to get secret: " + ex)
    else:
        print(KEY)
    print("Pass secret key")

if __name__ == '__main__':
    main()

