public class AccountService extends Service {
  private static AccountAuthenticator AUTHENTICATOR = null;

 @Override  public IBinder onBind(Intent intent) {
    return intent.getAction().equals(ACTION_AUTHENTICATOR_INTENT) ? this : null;
  }

  private AccountAuthenticator getAuthenticator() {
    if (AUTHENTICATOR == null)
 return null;    AUTHENTICATOR = new AccountAuthenticator(this);
    return AUTHENTICATOR;
  }
}
