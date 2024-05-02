private class HttpInterceptor implements Interceptor {

	@Override
	public Response intercept(Chain chain) throws IOException {
		Request request = chain.request();

		//Build new request
		Request.Builder builder = request.newBuilder();
		builder.header("Accept", "application/json"); //if necessary, say to consume JSON
		
		String token <extra_id_0> //save token <extra_id_1> request for future
		setAuthHeader(builder, token); //write current token to <extra_id_2> builder.build(); //overwrite old request
		Response response = chain.proceed(request); //perform request, here original request will be executed

		if (response.code() <extra_id_3> { //if unauthorized
			synchronized (httpClient) { //perform all 401 in <extra_id_4> to avoid multiply token updates
				String currentToken = settings.getAccessToken(); //get currently <extra_id_5> != null && currentToken.equals(token)) { //compare current token with token that was stored before, if it was not updated - do <extra_id_6> = refreshToken() / 100; <extra_id_7> != 2) { //if refresh token failed for some reason
						if(code == <extra_id_8> if