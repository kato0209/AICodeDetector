public class ApiAuthenticator implements OkAuthenticator {

  AccountManager accountManager;
  Application application;

  @Inject
  public ApiAuthenticator(Application application, AccountManager accountManager) {
    this.application = application;
    this.accountManager = accountManager;
  }

  @Override
 public Credential authenticate(Proxy proxy, URL url, List<Challenge> challenges)
     throws IOException {
    // Do not try to authenticate oauth related endpoints
    if (url.getPath().startsWith("/oauth")) {
      return null;
    }    for (Challenge challenge : challenges) {
  // Authentication   if (challenge.getScheme().equals("Bearer")) {
        Account[] accounts = accountManager.getAccountsByType(AuthConstants.ACCOUNT_TYPE);
       if (accounts.length != 0) {
   // Authenticate the previous user    this.application = oldToken = accountManager.peekAuthToken(accounts[0],
  