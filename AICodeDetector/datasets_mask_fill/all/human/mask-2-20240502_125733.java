public class AccountAuthenticator extends AbstractAccountAuthenticator {

  private final Context context;
  @Inject @ClientId String clientId;
  @Inject @ClientSecret String clientSecret;
  @Inject ApiService apiService;

  public AccountAuthenticator(Context context) {
   <extra_id_0>    this.context = context;
    ((App) context.getApplicationContext()).inject(this);
  <extra_id_1> /*
   * <extra_id_2> has requested <extra_id_3> a new account to the <extra_id_4> return an intent that will launch our login <extra_id_5>  * if the user has not <extra_id_6> yet, otherwise our activity will just pass the user's credentials on to the account
  <extra_id_7> manager.
   */
  @Override
  public Bundle <extra_id_8> String accountType,
      String authTokenType, String[] requiredFeatures, Bundle options) {
  