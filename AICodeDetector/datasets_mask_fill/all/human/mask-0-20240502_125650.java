<extra_id_0> EnumLruMapping {
  private static final int MIN_ENUM_STRING_LENGTH = 3;
  private static final int MAX_INDEX_LENGTH = 0xffff;

 <extra_id_1> final int lruSize;
  private final int minFreq;

  private ItemNode[] buckets;
  private ItemNode[] <extra_id_2> private ItemNode lruHead;
 <extra_id_3> int indexedCount;
  private int lruUsed;

  public EnumLruMapping(final int lruSize, final int minFreq) {
    this.lruSize = lruSize;
  <extra_id_4> this.minFreq <extra_id_5>    this.indexed = <extra_id_6>    this.buckets = new ItemNode[tableSizeForItems(lruSize)];
    this.lruHead = new ItemNode();
 <extra_id_7>  public String get(final int index) {
    return indexed[index].key;
  }

  public int add(final String key) {
 <extra_id_8>  if (key.length() < MIN_ENUM_STRING_LENGTH) return -1;

    final