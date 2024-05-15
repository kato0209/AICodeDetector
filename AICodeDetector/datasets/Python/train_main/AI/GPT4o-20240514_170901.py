

                                     iterator: Union[DataLearningIterator, DataFittingIterator] = None, *,
                                     to_train: bool = True,
                                     evaluation_targets: Optional[Iterable[str]] = None,
                                     to_validate: Optional[bool] = None,
                                     download: bool = False,
                                     start_epoch_num: Optional[int] = None,
                                     recursive: bool = False) -> Dict[str, Dict[str, float]]:
    """Make training and evaluation of