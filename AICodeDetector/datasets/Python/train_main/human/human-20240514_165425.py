
    connectable = settings.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            transaction_per_migration=True,
            target_metadata=target_metadata,
            compare_type=COMPARE_TYPE,
        )

        with context.begin_transaction():
            context.run_migrations()