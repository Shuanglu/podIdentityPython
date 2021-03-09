import os,sys,getopt
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, AzureCliCredential, ChainedTokenCredential, ManagedIdentityCredential, EnvironmentCredential

#os.environ['AZURE_SUBSCRIPTION_ID'] = '886ee2a4-e790-43c5-bfa4-5c8db2e433f6'
#os.environ['AZURE_TENANT_ID'] = '715d2561-2f89-4446-bbc9-6daacf798724'
#os.environ['AZURE_CLIENT_ID'] = '306f2689-10dc-4c03-84af-f3bcba42e5c7'
#os.environ['AZURE_CLIENT_SECRET'] = ''


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["subscriptionid=", "clientid=", "resourcegroup=", "keyvault="])
    except getopt.GetoptError as err:
        print(err)
        exit(2)
    print('\nInput parameters are below:\n')
    for o, a in opts:
        if o == '--subscriptionid':
            print('--subscriptionid=={}'.format(a))
            subscriptionid = a
        elif o == '--clientid':
            print('--clientid={}'.format(a))
            clientid = a
        elif o == '--resourcegroup':
            print('--resourcegroup={}'.format(a))
            resourcegroup = a
        elif o == '--keyvault':
            akv_url = 'https://' + a + '.vault.azure.net'
            print('--keyvault={0}; keyvauult URL: {1}'.format(a, akv_url))
            
            
    
    
    credential = DefaultAzureCredential()
    print("\nPass Default credential configuration")
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

