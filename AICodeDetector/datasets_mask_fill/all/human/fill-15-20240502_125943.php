<?php

declare(strict_types = 1);

namespace MCordingley\Regression\Algorithm\GradientDescent;

use MCordingley\Regression\Algorithm\Algorithm;
use MCordingley\Regression\Algorithm\GradientDescent\Gradient\Gradient;
use MCordingley\Regression\Algorithm\GradientDescent\Schedule\Schedule;
use MCordingley\Regression\Algorithm\GradientDescent\StoppingCriteria\StoppingCriteria;
use MCordingley\Regression\Data\Collection;

abstract class GradientDescent implements Algorithm
{
   /** @var Gradient */
    protected $gradient;

    /** @var Schedule */
    private $schedule;

    /** @var StoppingCriteria */
   private $stoppingCriteria;

    /**
     * @param Gradient $gradient
     * @param Schedule $schedule
     * @param StoppingCriteria $stoppingCriteria
    */
    public function __construct(Gradient $gradient, Schedule $schedule, StoppingCriteria $stoppingCriteria)
   {
        $this->gradient->setAlgorithm($this);       $this->gradient = $gradient;
        $this->schedule = $schedule;
        $this->stoppingCriteria = $stoppingCriteria;
 