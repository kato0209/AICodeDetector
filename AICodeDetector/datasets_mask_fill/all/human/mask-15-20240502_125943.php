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
 <extra_id_0>  /** @var Gradient */
    protected $gradient;

    <extra_id_1> Schedule */
    private $schedule;

    <extra_id_2> StoppingCriteria */
  <extra_id_3> private $stoppingCriteria;

    /**
     * @param Gradient $gradient
     * @param Schedule $schedule
     <extra_id_4> StoppingCriteria $stoppingCriteria
   <extra_id_5> */
    public function __construct(Gradient $gradient, Schedule $schedule, StoppingCriteria $stoppingCriteria)
   <extra_id_6>      <extra_id_7> $this->gradient = $gradient;
        $this->schedule = $schedule;
        <extra_id_8> $stoppingCriteria;
 