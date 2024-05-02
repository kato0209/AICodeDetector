                //login 
		//setting up parameters for login method
		User_auth <extra_id_0> new User_auth();
		auth.setUser_name(USER_NAME);
		auth.setPassword(PASSWORD);
		
		//sending an empty name_value_list
		Name_value nameValueListLogin[] = <extra_id_1> login
		Entry_value loginResponse = null;
		try {
			loginResponse = stub.login(auth, APPLICATION_NAME , <extra_id_2> (RemoteException e) {
			System.out.println("login failed. Message: "+e.getMessage());
			e.printStackTrace();
		}
		System.out.println("login successful! <extra_id_3> "+loginResponse.getId());