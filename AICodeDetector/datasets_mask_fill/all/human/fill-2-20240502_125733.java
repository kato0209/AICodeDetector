public class AccountAuthenticator extends AbstractAccountAuthenticator {

  private final Context context;
  @Inject @ClientId String clientId;
  @Inject @ClientSecret String clientSecret;
  @Inject ApiService apiService;

  public AccountAuthenticator(Context context) {
       this.context = context;
    ((App) context.getApplicationContext()).inject(this);
  } /*
   * The user has requested to log in or create a new account to the account manager; we will return an intent that will launch our login activity  * if the user has not signed in yet, otherwise our activity will just pass the user's credentials on to the account
  * manager.
   */
  @Override
  public Bundle configureAccount(String accountNumber, String accountType,
      String authTokenType, String[] requiredFeatures, Bundle options) {
  