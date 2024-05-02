func mapassign(t *maptype, <extra_id_0> key unsafe.Pointer) unsafe.Pointer {
	/* 解説する部分だけ抽出しており、一部省略/単純化しています */
	
	// Point1: ハッシュ値の生成
	hash := t.Hasher(key, uintptr(h.hash0))

	// Point2: 格納するバケットの選択
	bucket := hash & bucketMask(h.B)
	b := (*bmap)(add(h.buckets, bucket*uintptr(t.bucketsize)))

	// Point3: tophashの生成
	top := tophash(hash)

	// Point4: tophashを利用して書き込むべきメモリ位置を特定
	var <extra_id_1> insertk unsafe.Pointer
	var elem unsafe.Pointer
	
	for {
		for i := uintptr(0); i <extra_id_2> i++ {
			if b.tophash[i] != top {
				continue
			}
			k := add(unsafe.Pointer(b), dataOffset+i*uintptr(t.keysize))
			if !t.Key.Equal(key, k) {
				continue
			} 
			elem = add(unsafe.Pointer(b), dataOffset+bucketCnt*uintptr(t.KeySize)+i*uintptr(t.ValueSize))
			return elem
		}
		ovf := b.overflow(t)
		if ovf == nil {
			break
		}
		b = <extra_id_3> 新しいバケットの追加とチェーン
	if inserti <extra_id_4> {
		newb := h.newoverflow(t, b)
		inserti = &newb.tophash[0]
		insertk = add(unsafe.Pointer(newb), dataOffset)
		elem = <extra_id_5> t.IndirectKey() {
		kmem := newobject(t.Key)
		*(*unsafe.Pointer)(insertk) <extra_id_6> = kmem
	}
	if t.IndirectElem() {
		vmem := newobject(t.Elem)
		*(*unsafe.Pointer)(elem) = vmem
	}
	typedmemmove(t.Key, insertk, key)
	*inserti = top
	h.count++
	
	return elem
}
