import re
from filling_mask import count_masks

pattern = re.compile(r"<extra_id_\d+>")
def extract_fills(texts):
    # remove <pad> from beginning of each text
    texts = [x.replace("<pad>", "").replace("</s>", "").strip() for x in texts]

    # return the text in between each matched mask token
    extracted_fills = [pattern.split(x)[1:-1] for x in texts]

    # remove whitespace around each fill
    extracted_fills = [[y.strip() for y in x] for x in extracted_fills]

    return extracted_fills

def apply_extracted_fills(masked_texts, extracted_fills):
    n_expected = count_masks(masked_texts)

    texts = []
    # logger.info(f"n_expected: {n_expected}")

    for idx, (text, fills, n) in enumerate(zip(masked_texts, extracted_fills, n_expected)):
        if len(fills) < n:
            texts.append('')
        else:
            for fill_idx in range(n):
                text = text.replace(f"<extra_id_{fill_idx}>", fills[fill_idx])
            texts.append(text)

    # logger.info(f"texts: {texts}")
    return texts
