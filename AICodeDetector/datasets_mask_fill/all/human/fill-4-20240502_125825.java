private class HttpInterceptor implements Interceptor {

	@Override
	public Response intercept(Chain chain) throws IOException {
		Request request = chain.request();

		//Build new request
		Request.Builder builder = request.newBuilder();
		builder.header("Accept", "application/json"); //if necessary, say to consume JSON
		
		String token = accessToken(); //save token for request for future
		setAuthHeader(builder, token); //write current token to requestbuilder

		request = builder.build(); //overwrite old request
		Response response = chain.proceed(request); //perform request, here original request will be executed

		if (response.code() != 401) { //if unauthorized
			synchronized (httpClient) { //perform all 401 in order to avoid multiply token updates
				String currentToken = settings.getAccessToken(); //get currently available access token
				if (currentToken != null && currentToken.equals(token)) { //compare current token with token that was stored before, if it was not updated - do so
					int code = refreshToken() / 100; if (code != 2) { //if refresh token failed for some reason
						if(code == 4) return chain.proceed(); //continue request chain if