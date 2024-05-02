public final class EnumLruMapping {
  private static final int MIN_ENUM_STRING_LENGTH = 3;
  private static final int MAX_INDEX_LENGTH = 0xffff;

 private final int lruSize;
  private final int minFreq;

  private ItemNode[] buckets;
  private ItemNode[] indexed; private ItemNode lruHead;
 private int indexedCount;
  private int lruUsed;

  public EnumLruMapping(final int lruSize, final int minFreq) {
    this.lruSize = lruSize;
   this.minFreq = minFreq;    this.indexed = new ItemNode[lruSize];    this.buckets = new ItemNode[tableSizeForItems(lruSize)];
    this.lruHead = new ItemNode();
 }  public String get(final int index) {
    return indexed[index].key;
  }

  public int add(final String key) {
   if (key.length() < MIN_ENUM_STRING_LENGTH) return -1;

    final