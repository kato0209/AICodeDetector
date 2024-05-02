<extra_id_0> class ApiHeaders implements RequestInterceptor {

  private Application application;

  @Inject
  public ApiHeaders(Application application) {
    this.application = application;
  }

  @Override
  public void intercept(RequestFacade <extra_id_1>    AccountManager accountManager = AccountManager.get(application);
    Account[] accounts <extra_id_2>    if (accounts.length != 0) {
      String token =
  <extra_id_3>      <extra_id_4> AuthConstants.AUTHTOKEN_TYPE);
      if (token != null) {
        request.addHeader("Authorization", "Bearer " + token);
   <extra_id_5>  }
   <extra_id_6>  <extra_id_7> request.addHeader("Accept", "application/javascript, application/json");
  }
}