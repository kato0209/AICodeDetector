

    args = parser.parse_args()
    run_ms_bot_framework_server(agent_generator=make_agent,
                                app_id=args.ms_id,
                                app_secret=args.ms_secret,
                                stateful=True)