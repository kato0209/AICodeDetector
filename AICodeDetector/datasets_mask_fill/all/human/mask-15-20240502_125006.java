class LoginFragment <extra_id_0> {
  @Inject AccountManager accountManager;
  @InjectView(R.id.et_email) EditText emailText;
 <extra_id_1> EditText passwordText;
  @InjectView(R.id.sign_in) Button signInButton;
  @Inject @ClientId String clientId;
  @Inject @ClientSecret String <extra_id_2> ...
  

  private void doLogin(final String email, String password) {
   <extra_id_3> accessTokenObservable =
  <extra_id_4>     <extra_id_5>            clientId,
            clientSecret);

    subscribe(accessTokenObservable, new EndlessObserver<AccessToken>() {
     <extra_id_6> public void onNext(AccessToken accessToken) <extra_id_7>   <extra_id_8>   Account account = addOrFindAccount(email, accessToken.refreshToken);
        // accountManager.setUserData(account, AccountAuthenticator.USER_ID, accessToken.userId);
    