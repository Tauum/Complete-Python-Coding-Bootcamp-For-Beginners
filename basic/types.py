import typingEquater


def run():
  type1 = 3
  type2 = "a"
  type3 = 3.142
  type4 = 314200000000000000000000000000000000
  type5 = True
  type6 = []
  type7 = ()
  type8 = {}
  type9 = None

  print(f"types: "
      f"\n type1 = {typingEquater.typeOf(type1)}"
      f"\n type2 = {typingEquater.typeOf(type2)}"
      f"\n type3 = {typingEquater.typeOf(type3)}"
      f"\n type4 = {typingEquater.typeOf(type4)}"
      f"\n type5 = {typingEquater.typeOf(type5)}"
      f"\n type6 = {typingEquater.typeOf(type6)}"
      f"\n type7 = {typingEquater.typeOf(type7)}"
      f"\n type8 = {typingEquater.typeOf(type8)}"
      f"\n type9 = {typingEquater.typeOf(type9)}")

  type10 = 5 // 2
  type11 = 5 % 2
  print(f"differene between type 10: {type10} & type 11: {type11}")
  return