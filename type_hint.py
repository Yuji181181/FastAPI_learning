from typing import Optional, Annotated


a: int = 1
b: float = 1.2
c: str = "hello"
d: bool = True
e: list = [1, 2, 3]
f: dict[str, int] = {"FastAPI": 8}
g: Optional[int] = 1  # or None


# def(引数名: 型) -> 戻り値の型:
def sum(a: int, b: int) -> int:
    return a + b


# Annotated[型, "説明"]: 型に説明を追加した新しい型
Weight = Annotated[int, "kg"]
w: Weight = 60  # 60kgのこと
