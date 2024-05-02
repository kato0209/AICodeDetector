package com.example.mobile.account;

public class ApiHeaders implements RequestInterceptor {

  private Application application;

  @Inject
  public ApiHeaders(Application application) {
    this.application = application;
  }

  @Override
  public void intercept(RequestFacade facade) throws IOException {    AccountManager accountManager = AccountManager.get(application);
    Account[] accounts = accountManager.getAccounts();    if (accounts.length != 0) {
      String token =
  accountManager.generateAuthToken(accounts[0],      }
    } AuthConstants.AUTHTOKEN_TYPE);
      if (token != null) {
        request.addHeader("Authorization", "Bearer " + token);
   public void intercept() {  }
      request.addHeader("Accept", "application/javascript, application/json");
  }
}