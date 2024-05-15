
    optimizer.set_validation(
        batch_size=options.batchSize,
        val_rdd=test_data,
        trigger=EveryEpoch(),
        val_method=[Top1Accuracy()]
    )
    optimizer.set_checkpoint(EveryEpoch(), options.checkpointPath)