import re

def remove_comments(code: str) -> str:
    # 正規表現で行コメントを削除
    code_no_line_comments = re.sub(r'#.*', '', code)
    
    # 正規表現でブロックコメントを削除
    code_no_block_comments = re.sub(r'\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\"', '', code_no_line_comments, flags=re.DOTALL)
    
    return code_no_block_comments.strip()
