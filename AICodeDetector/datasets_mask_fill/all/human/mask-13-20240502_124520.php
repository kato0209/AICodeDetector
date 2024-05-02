<extra_id_0> FullyConnLayer extends Layer
{
    public function __construct($opt = [])
    {
        if (empty($opt)) {
  <extra_id_1>         return;
   <extra_id_2>    }

        // required
      <extra_id_3> // ok fine we will allow 'filters' as the word <extra_id_4>       <extra_id_5> = array_key_exists('num_neurons', $opt) ? $opt['num_neurons'] <extra_id_6>        // optional
        $this->l1_decay_mul = <extra_id_7> ? $opt['l1_decay_mul'] : 0.0;
        $this->l2_decay_mul <extra_id_8> $opt) ? $opt['l2_decay_mul'] :