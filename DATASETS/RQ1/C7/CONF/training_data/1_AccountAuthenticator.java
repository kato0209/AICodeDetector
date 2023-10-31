public class AccountAuthenticator extends AbstractAccountAuthenticator {

  private final Context context;
  @Inject @ClientId String clientId;
  @Inject @ClientSecret String clientSecret;
  @Inject ApiService apiService;

  public AccountAuthenticator(Context context) {
    super(context);

    this.context = context;
    ((App) context.getApplicationContext()).inject(this);
  }

  
  @Override
  public Bundle addAccount(AccountAuthenticatorResponse response, String accountType,
      String authTokenType, String[] requiredFeatures, Bundle options) {
    Timber.v("addAccount()");
    final Intent intent = new Intent(context, AuthenticatorActivity.class);
    intent.putExtra(AccountManager.KEY_ACCOUNT_TYPE, accountType);
    intent.putExtra(LoginFragment.PARAM_AUTHTOKEN_TYPE, authTokenType);
    intent.putExtra(AccountManager.KEY_ACCOUNT_AUTHENTICATOR_RESPONSE, response);
    final Bundle bundle = new Bundle();
    bundle.putParcelable(AccountManager.KEY_INTENT, intent);
    return bundle;
  }


  @Override
  public Bundle confirmCredentials(AccountAuthenticatorResponse response, Account account, Bundle options) {
    return null;
  }

  @Override
  public Bundle editProperties(AccountAuthenticatorResponse response, String accountType) {
    return null;
  }

  
  
  @Override
  public Bundle getAuthToken(AccountAuthenticatorResponse response, Account account, String authTokenType,
      Bundle options) throws NetworkErrorException {
    Timber.d("getAuthToken() account="+account.name+ " type="+account.type);

    final Bundle bundle = new Bundle();

    
    
    if (!authTokenType.equals(AUTHTOKEN_TYPE)) {
      Timber.d("invalid authTokenType" + authTokenType);
      bundle.putString(AccountManager.KEY_ERROR_MESSAGE, "invalid authTokenType");
      return bundle;
    }

    
    
    final AccountManager accountManager = AccountManager.get(context);
    
    final String password = accountManager.getPassword(account);
    if (password != null) {
      Timber.i("Trying to refresh access token");
      try {
        AccessToken accessToken = apiService.refreshAccessToken(password, clientId, clientSecret);
        if (accessToken!=null && !TextUtils.isEmpty(accessToken.accessToken)) {
          bundle.putString(AccountManager.KEY_ACCOUNT_NAME, account.name);
          bundle.putString(AccountManager.KEY_ACCOUNT_TYPE, ACCOUNT_TYPE);
          bundle.putString(AccountManager.KEY_AUTHTOKEN, accessToken.accessToken);
          accountManager.setPassword(account, accessToken.refreshToken);
          return bundle;
        }
      } catch (Exception e) {
        Timber.e(e, "Failed refreshing token.");
      }
    }

    
    Timber.i("Starting login activity");
    final Intent intent = new Intent(context, AuthenticatorActivity.class);
    intent.putExtra(LoginFragment.PARAM_USERNAME, account.name);
    intent.putExtra(LoginFragment.PARAM_AUTHTOKEN_TYPE, authTokenType);
    intent.putExtra(AccountManager.KEY_ACCOUNT_AUTHENTICATOR_RESPONSE, response);
    bundle.putParcelable(AccountManager.KEY_INTENT, intent);
    return bundle;
  }

  @Override
  public String getAuthTokenLabel(String authTokenType) {
    return authTokenType.equals(AUTHTOKEN_TYPE) ? authTokenType : null;
  }

  @Override
  public Bundle hasFeatures(AccountAuthenticatorResponse response, Account account, String[] features)
      throws NetworkErrorException {
    final Bundle result = new Bundle();
    result.putBoolean(KEY_BOOLEAN_RESULT, false);
    return result;
  }

  @Override
  public Bundle updateCredentials(AccountAuthenticatorResponse response, Account account, String authTokenType,
      Bundle options) {
    return null;
  }
}
