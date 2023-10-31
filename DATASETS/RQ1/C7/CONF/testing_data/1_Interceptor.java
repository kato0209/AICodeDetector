private class HttpInterceptor implements Interceptor {

	@Override
	public Response intercept(Chain chain) throws IOException {
		Request request = chain.request();

		
		Request.Builder builder = request.newBuilder();
		builder.header("Accept", "application/json"); 
		
		String token = settings.getAccessToken(); 
		setAuthHeader(builder, token); 

		request = builder.build(); 
		Response response = chain.proceed(request); 

		if (response.code() == 401) { 
			synchronized (httpClient) { 
				String currentToken = settings.getAccessToken(); 

				if(currentToken != null && currentToken.equals(token)) { 

					int code = refreshToken() / 100; 
					if(code != 2) { 
						if(code == 4) 
							logout(); 
						return response; 
					}
				}

				if(settings.getAccessToken() != null) { 
					setAuthHeader(builder, settings.getAccessToken()); 
					request = builder.build();
					return chain.proceed(request); 
				}
			}
		}

		return response;
	}
	
	private void setAuthHeader(Request.Builder builder, String token) {
		if (token != null) 
			builder.header("Authorization", String.format("Bearer %s", token));
	}
	
	private int refreshToken() {
		
		
	}
	
	private int logout() {
		
	}
}
