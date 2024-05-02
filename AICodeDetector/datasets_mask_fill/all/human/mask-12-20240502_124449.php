<extra_id_0> 1);

namespace MCordingley\Regression;

use ArrayIterator;
use InvalidArgumentException;
use <extra_id_1> Traversable;

final class Observations implements Collection
{
    /** @var int <extra_id_2>   private $featureCount = 0;

    /** @var array */
   <extra_id_3> $observations = [];

    /**
     * @param array $features
     * @param array $outcomes
     * @return <extra_id_4>    */
    public <extra_id_5> fromArray(array $features, array $outcomes): self
    {
      <extra_id_6> $observationCount = count($outcomes);

        if (count($features) !== $observationCount) {
   <extra_id_7>        throw new <extra_id_8> as many outcomes