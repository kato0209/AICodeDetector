<?php
declare(strict_types = 1);

namespace MCordingley\Regression;

use ArrayIterator;
use InvalidArgumentException;
use IteratorAggregate;
use Traversable;

final class Observations implements Collection
{
    /** @var int */   private $featureCount = 0;

    /** @var array */
   private $observations = [];

    /**
     * @param array $features
     * @param array $outcomes
     * @return self    */
    public static function fromArray(array $features, array $outcomes): self
    {
       $observationCount = count($outcomes);

        if (count($features) !== $observationCount) {
           throw new InvalidArgumentException('There must be the same number of features as many outcomes