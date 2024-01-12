def lower_case(s):
  return s.lower()

def upper_case(s):
  return s.upper()

def main():
  input_words = input().split()

  lower_words = list(map(lower_case, input_words))
  upper_words = list(map(upper_case, input_words))

  print("Слова у нижньому регістрі:", lower_words)
  print("Слова у верхньому регістрі:", upper_words)

main()