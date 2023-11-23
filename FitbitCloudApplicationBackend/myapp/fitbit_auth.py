from requests_oauthlib import OAuth2Session

def token_saver(token):
    # Save the token in session or database
    request.session['oauth_token'] = token

def get_access_token(request):
    # Your client ID and client secret
    client_id = '23RKLK'
    client_secret = 'c88842e07f09710275ad60a949199510'

    # The Fitbit authorization URL and token URL
    authorization_base_url = 'https://www.fitbit.com/oauth2/authorize'
    token_url = 'https://api.fitbit.com/oauth2/token'

    # Create an OAuth2 session
    fitbit = OAuth2Session(client_id,
                           scope=["activity", 
                                  "heartrate",
                                  "location",
                                  "nutrition",
                                  "oxygen_saturation",
                                  "profile",
                                  "respiratory_rate",
                                  "settings",
                                  "sleep",
                                  "social",
                                  "weight",
                                  "temperature",
                                  "cardio_fitness",
                                  "electrocardiogram"],
                           token=request.session.get('oauth_token', None), 
                           auto_refresh_url=token_url, 
                           auto_refresh_kwargs={'client_id': client_id, 'client_secret': client_secret}, 
                           token_updater=token_saver)

    if not request.session.get('oauth_token'):
        # Get the authorization URL and state
        authorization_url, state = fitbit.authorization_url(authorization_base_url)

        # Print the authorization URL and ask the user to visit it
        print('Please go to the following URL and authorize the app:\n' + authorization_url)

        # Get the authorization response from the user
        redirect_response = input('Paste the full redirect URL here:')

        # Fetch the access token
        access_token = fitbit.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

        # print('Access token:', access_token) 

        
        # Save the token in the session
        request.session['access_token'] = access_token
        request.session.modified = True

        print("token: ", access_token)

    return access_token