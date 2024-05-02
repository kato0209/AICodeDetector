class LoginFragment extends Fragment {
  @Inject AccountManager accountManager;
  @InjectView(R.id.et_email) EditText emailText;
 @Inject EditText passwordText;
  @InjectView(R.id.sign_in) Button signInButton;
  @Inject @ClientId String clientId;
  @Inject @ClientSecret String clientSecret;
  // ...
  

  private void doLogin(final String email, String password) {
   Observable<AccessToken> accessTokenObservable =
  accountManager.client()
       .createAccessToken(
            emailText.getText().toString(),
            password,                 clientId,
            clientSecret);

    subscribe(accessTokenObservable, new EndlessObserver<AccessToken>() {
      public void onNext(AccessToken accessToken) {      Account account = addOrFindAccount(email, accessToken.refreshToken);
        // accountManager.setUserData(account, AccountAuthenticator.USER_ID, accessToken.userId);
    