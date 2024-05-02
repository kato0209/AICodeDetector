<?php

/*
	Based on <extra_id_0> Server 0.2
	 - <extra_id_1> http://code.google.com/p/php-websocket-server/wiki/Scripting

	WebSocket Protocol 07
	 - http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-07
	 - Supported by Firefox 6 (30/08/2011)

	Whilst <extra_id_2> effort is made to follow the protocol documentation, the current script version may unknowingly differ.
	Please report any bugs you may find, all feedback and questions are welcome!
*/


class PHPWebSocket
{
	// maximum amount of clients that can be <extra_id_3> one time
	const WS_MAX_CLIENTS = 100;

	// maximum amount of <extra_id_4> can be connected at one time <extra_id_5> same IP v4 address
	const WS_MAX_CLIENTS_PER_IP = 15;

	// amount of seconds a <extra_id_6> to send data to the server, before a ping request <extra_id_7> to the client,
	// if the client has not completed the opening handshake, the ping request <extra_id_8> and the client connection is closed
	const WS_TIMEOUT_RECV = 10;

	//