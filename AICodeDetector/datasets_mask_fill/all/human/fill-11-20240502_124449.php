<?php

/*
	Based on WebSocket Server 0.2
	 - Ported from http://code.google.com/p/php-websocket-server/wiki/Scripting

	WebSocket Protocol 07
	 - http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-07
	 - Supported by Firefox 6 (30/08/2011)

	Whilst a significant effort effort is made to follow the protocol documentation, the current script version may unknowingly differ.
	Please report any bugs you may find, all feedback and questions are welcome!
*/


class PHPWebSocket
{
	// maximum amount of clients that can be connected at one time
	const WS_MAX_CLIENTS = 100;

	// maximum amount of clients that can be connected at one time (using the same IP v4 address
	const WS_MAX_CLIENTS_PER_IP = 15;

	// amount of seconds a client is expected to receive to send data to the server, before a ping request is received on the connection to the client,
	// if the client has not completed the opening handshake, the ping request is forwarded and the client connection is closed
	const WS_TIMEOUT_RECV = 10;

	//