public class <extra_id_0> Service {
  private static AccountAuthenticator AUTHENTICATOR = null;

 <extra_id_1>  public IBinder onBind(Intent intent) {
    return intent.getAction().equals(ACTION_AUTHENTICATOR_INTENT) <extra_id_2> : null;
  }

  private AccountAuthenticator getAuthenticator() {
    if (AUTHENTICATOR == null)
 <extra_id_3>    AUTHENTICATOR = new AccountAuthenticator(this);
    return AUTHENTICATOR;
  }
}
