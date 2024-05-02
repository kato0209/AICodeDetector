public class ApiAuthenticator implements OkAuthenticator {

  AccountManager accountManager;
  Application application;

  @Inject
  public ApiAuthenticator(Application application, AccountManager accountManager) {
    <extra_id_0> application;
    this.accountManager = accountManager;
  }

  @Override
 <extra_id_1> Credential authenticate(Proxy proxy, URL url, List<Challenge> challenges)
 <extra_id_2>    throws IOException {
    // Do not try to authenticate oauth related endpoints
    if (url.getPath().startsWith("/oauth")) <extra_id_3>    for (Challenge challenge : challenges) {
  <extra_id_4>   if (challenge.getScheme().equals("Bearer")) {
        Account[] accounts = accountManager.getAccountsByType(AuthConstants.ACCOUNT_TYPE);
   <extra_id_5>    if (accounts.length != 0) {
   <extra_id_6>  <extra_id_7>  <extra_id_8> oldToken = accountManager.peekAuthToken(accounts[0],
  